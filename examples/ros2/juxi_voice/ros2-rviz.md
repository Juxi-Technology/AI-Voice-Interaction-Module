English | [简体中文](ros2-rviz_CN.md)
# ROS2-rviz2 Visualization (Type-C / UART / IIC All-in-One Version)

## 1. Environment Preparation

#### System Requirements

- **Operating System**: Ubuntu 22.04
- **ROS2 Version**: Humble

#### Install Dependency Libraries

```bash
# 1. 更新源
sudo apt update

# 2. 安装 ROS2 基础包
# (如果已安装ROS2，跳过)
# sudo apt install ros-humble-desktop -y

# 3. 安装本项目依赖（同时支持串口和I2C）
sudo apt install python3-pip ros-humble-rviz2 ros-humble-visualization-msgs -y
pip3 install pyserial smbus2

# 4. 如果使用 I2C 接线，额外安装
sudo apt install python3-smbus2 i2c-tools -y
```

---

## 2. The Three Wiring Methods

The AI voice interaction module supports the following three wiring methods:

| Wiring Method | Interface | Device File | Protocol | Baud Rate |
|---|---|---|---|---|
| **Type-C** | USB Type-C | `/dev/ttyUSB0` or `/dev/ttyACM0` | Serial frame `FE EF XX YY EE` | 115200 |
| **UART** | GPIO serial pins | `/dev/ttyAMA0` or `/dev/ttyS0` | Serial frame `FE EF XX YY EE` | 115200 |
| **IIC** | I2C bus (SDA/SCL) | `/dev/i2c-1` | Register read/write (0x2A) | — |

#### Auto-Detection Mechanism

When the ROS2 node starts, it automatically detects the wiring method in the following order:
1. First tries serial: checks `/dev/ttyUSB0` → `/dev/ttyACM0` → `/dev/ttyAMA0` → `/dev/ttyS0` in sequence
2. Then tries I2C: checks whether slave `0x2A` exists on `/dev/i2c-1`
3. Serial detection only requires the device file to exist and be openable to be considered usable; no additional verification is needed

Once any method is detected, detection stops and that method is locked in. No manual configuration is required.

---

## 3. IIC Protocol

#### IIC Slave Configuration

| Parameter | Value |
|---|---|
| IIC slave address | **0x2A** |
| IIC bus | /dev/i2c-1 |

#### Register Definitions

| Register Address | R/W | Description |
|---|---|---|
| **0xDA** | R | Recognition result register; reading 1 byte = command word ID |
| **0xD1** | W | Passive announcement voice register; write 1 byte |
| **0xD2** | W | Function word announcement voice register; write 1 byte |
| **0xD3** | W | Command word announcement voice register; write 1 byte |

---

## 4. Serial Protocol (Type-C / UART)

#### Frame Format

Each frame is fixed at **5 bytes**:

| Byte 0 | Byte 1 | Byte 2 | Byte 3 | Byte 4 |
|---|---|---|---|---|
| 0xFE | 0xEF | Command high byte | Command low byte | 0xEE |
| Frame header | Frame header | CMD_H | CMD_L | Frame tail |

#### Baud Rate

Fixed at **115200** bps.

---

## 5. Creating the Workspace and Directory Structure

#### Create the Directories

```bash
mkdir -p ~/juxi_speech_ws/src
cd ~/juxi_speech_ws/src
```

#### Create the ROS2 Package

```bash
ros2 pkg create --build-type ament_python juxi_voice --license MIT
```

#### Final Directory Structure

```
~/juxi_speech_ws/
├── build/
├── install/
├── log/
└── src/
    └── juxi_voice/
        ├── package.xml
        ├── setup.py           # (替换为本项目提供的)
        ├── juxi_voice.rviz    # (新建：RViz预配置文件)
        ├── resource/
        │   └── juxi_voice
        └── juxi_voice/
            ├── __init__.py
            ├── voice_node.py    # (新建：语音节点)
            └── rviz_control.py  # (新建：RViz控制节点)
```

---

## 6. File Contents and Placement

#### File 1: `voice_node.py` (voice control node)

**Location**: `~/juxi_speech_ws/src/juxi_voice/juxi_voice/voice_node.py`

**Core functions**:
- Auto-detect the Type-C / UART / IIC wiring method
- Unified command word mapping table (114 command words)
- Use the corresponding communication backend based on the wiring method

**Key architecture**:

```python
# 统一命令数据: ID → (串口字节2, 串口字节3, 命令文本, 播报模式)
CMD_DATA = {
    1:  (0x01, 0x00, "欢迎语", "被"),
    3:  (0x03, 0x00, "你好小犀", "主"),
    14: (0x00, 0x04, "小车前进", "主"),
    84: (0xFF, 0x5F, "这是红色", "被"),
    ...
}

# 自动检测函数
def detect_connection(logger):
    # 1. 尝试 I2C
    # 2. 尝试串口 /dev/ttyUSB0, /dev/ttyACM0, /dev/ttyAMA0, /dev/ttyS0
    ...
```

(For the complete code, see the `voice_node.py` file provided by the project.)

#### File 2: `rviz_control.py` (RViz control node)

**Location**: `~/juxi_speech_ws/src/juxi_voice/juxi_voice/rviz_control.py`

Subscribes to the `/juxi_voice_cmd` topic to receive command text, and updates the cube visualization according to the command.

(For the complete code, see the `rviz_control.py` file provided by the project.)

#### File 3: Modify `setup.py`

**Location**: `~/juxi_speech_ws/src/juxi_voice/setup.py`

```python
entry_points={
    'console_scripts': [
        'voice_node = juxi_voice.voice_node:main',
        'rviz_control = juxi_voice.rviz_control:main',
    ],
},
```

---

## 7. Building and Running

#### Build

```bash
cd ~/juxi_speech_ws
colcon build --symlink-install
```

#### Environment Variables

```bash
source ~/juxi_speech_ws/install/setup.bash
# 或写入 ~/.bashrc
echo "source ~/juxi_speech_ws/install/setup.bash" >> ~/.bashrc
```

#### Permissions

```bash
# I2C 权限
sudo chmod 666 /dev/i2c-1
# 串口权限
sudo chmod 666 /dev/ttyUSB0
sudo chmod 666 /dev/ttyACM0
sudo chmod 666 /dev/ttyAMA0
# 或加入用户组
sudo usermod -aG dialout $USER
sudo usermod -aG i2c $USER
```

#### Run the Nodes (3 terminals)

**Terminal 1**: voice node

```bash
cd ~/juxi_speech_ws
source install/setup.bash
ros2 run juxi_voice voice_node
```

On startup it displays the detected wiring method:
```
自动检测: IIC /dev/i2c-1 (从机地址 0x2A)
语音节点启动完成 - IIC /dev/i2c-1 (从机地址 0x2A)
```
or
```
自动检测: UART /dev/ttyUSB0
语音节点启动完成 - UART /dev/ttyUSB0
```

**Terminal 2**: RViz control node

```bash
cd ~/juxi_speech_ws
source install/setup.bash
ros2 run juxi_voice rviz_control
```

**Terminal 3**: RViz visualization (loads the pre-configured file directly; no manual setup needed)

```bash
rviz2 -d ~/juxi_speech_ws/src/juxi_voice/juxi_voice.rviz
```

Or open RViz first and then load:

```bash
rviz2
# 菜单栏: File → Open Config → 选择 juxi_voice.rviz
```

---

## 8. RViz Pre-configuration

`juxi_voice.rviz` comes pre-configured with the following, ready to use on startup without any manual operation:

- **Fixed Frame**: `map`
- **Marker display**: already subscribed to `/juxi_visual_marker` (single marker)
- **MarkerArray display**: already subscribed to `/juxi_visual_markers` (multiple markers: robotic arm, battery, alarm, etc.)
- **View**: viewed from an oblique upper angle, with the center at the origin

---

## 9. Usage

#### Wake-up
Say **"你好小犀"** to the module → the module replies "我在"

#### Send Commands
- "小车前进" → the cube moves forward
- "亮红灯" → the cube turns red
- "打开流水灯" → colors cycle
- "报警" → red pulsating sphere
- "显示电量" → battery text

#### Host-triggered Announcement

```bash
# 被动播报
ros2 topic pub /juxi_passive_play std_msgs/msg/String "data: '这是红色'"
# 功能词播报
ros2 topic pub /juxi_func_play std_msgs/msg/String "data: '欢迎语'"
# 命令词播报
ros2 topic pub /juxi_cmd_play std_msgs/msg/String "data: '小车前进'"
```

---

## 10. Command Word ID Reference Table

### Function Words (ID 1-10)

| ID | Command Word | Serial Frame | Playback Mode |
|---|---|---|---|
| 1 | 欢迎语 | FE EF 01 00 EE | 被 |
| 2 | 休息语 | FE EF 02 00 EE | 主 |
| 3 | 你好小犀 | FE EF 03 00 EE | 主 |
| 4 | 增大音量 | FE EF 04 00 EE | 主 |
| 5 | 减小音量 | FE EF 05 00 EE | 主 |
| 6 | 最大音量 | FE EF 06 00 EE | 主 |
| 7 | 中等音量 | FE EF 07 00 EE | 主 |
| 8 | 最小音量 | FE EF 08 00 EE | 主 |
| 9 | 开启播报 | FE EF 09 00 EE | 主 |
| 10 | 关闭播报 | FE EF 0A 00 EE | 主 |

### Command Words (ID 11-83, 113)

| ID | Command Word | Serial Frame | Playback Mode |
|---|---|---|---|
| 11 | 小车停止 | FE EF 00 01 EE | 主 |
| 12 | 停车 | FE EF 00 02 EE | 主 |
| 13 | 小车休眠 | FE EF 00 03 EE | 主 |
| 14 | 小车前进 | FE EF 00 04 EE | 主 |
| 15 | 小车后退 | FE EF 00 05 EE | 主 |
| 16 | 小车左转 | FE EF 00 06 EE | 主 |
| 17 | 小车右转 | FE EF 00 07 EE | 主 |
| 18 | 小车左旋 | FE EF 00 08 EE | 主 |
| 19 | 小车右旋 | FE EF 00 09 EE | 主 |
| 20 | 关灯 | FE EF 00 0A EE | 主 |
| 21 | 亮红灯 | FE EF 00 0B EE | 主 |
| 22 | 亮绿灯 | FE EF 00 0C EE | 主 |
| 23 | 亮蓝灯 | FE EF 00 0D EE | 主 |
| 24 | 亮黄灯 | FE EF 00 0E EE | 主 |
| 25 | 打开流水灯 | FE EF 00 0F EE | 主 |
| 26 | 打开渐变灯 | FE EF 00 10 EE | 主 |
| 27 | 打开呼吸灯 | FE EF 00 11 EE | 主 |
| 28 | 显示电量 | FE EF 00 12 EE | 主 |
| 29 | 导航去一号位 | FE EF 00 13 EE | 主 |
| 30 | 导航去二号位 | FE EF 00 14 EE | 主 |
| 31 | 导航去三号位 | FE EF 00 15 EE | 主 |
| 32 | 导航去四号位 | FE EF 00 20 EE | 主 |
| 33 | 回到原点 | FE EF 00 21 EE | 主 |
| 34 | 关闭巡线 | FE EF 00 16 EE | 主 |
| 35 | 巡红线 | FE EF 00 17 EE | 主 |
| 36 | 巡绿线 | FE EF 00 18 EE | 主 |
| 37 | 巡蓝线 | FE EF 00 19 EE | 主 |
| 38 | 巡黄线 | FE EF 00 1A EE | 主 |
| 39 | 开启跟随 | FE EF 00 1B EE | 主 |
| 40 | 关闭跟随 | FE EF 00 1C EE | 主 |
| 41 | 报警 | FE EF 00 26 EE | 主 |
| 42 | 向上 | FE EF 00 27 EE | 主 |
| 43 | 向下 | FE EF 00 28 EE | 主 |
| 44 | 向左 | FE EF 00 29 EE | 主 |
| 45 | 向右 | FE EF 00 2A EE | 主 |
| 46 | 夹紧 | FE EF 00 2B EE | 主 |
| 47 | 松开 | FE EF 00 2C EE | 主 |
| 48 | 鼓掌 | FE EF 00 2D EE | 主 |
| 49 | 点头 | FE EF 00 2E EE | 主 |
| 50 | 祈祷 | FE EF 00 2F EE | 主 |
| 51 | 跪下 | FE EF 00 30 EE | 主 |
| 52 | 初始位置 | FE EF 00 31 EE | 主 |
| 53 | 惊吓 | FE EF 00 32 EE | 主 |
| 54 | 叠罗汉 | FE EF 00 33 EE | 主 |
| 55 | 跳舞 | FE EF 00 34 EE | 主 |
| 56 | 夹方块 | FE EF 00 35 EE | 主 |
| 57 | 搬运 | FE EF 00 36 EE | 主 |
| 58 | 输入完成 | FE EF 00 37 EE | 主 |
| 59 | 输入结束 | FE EF 00 38 EE | 主 |
| 60 | 运动动作 | FE EF 00 39 EE | 主 |
| 61 | 清除动作 | FE EF 00 3A EE | 主 |
| 62 | 这是什么颜色 | FE EF 00 3C EE | 主 |
| 63 | 开始颜色分拣 | FE EF 00 3D EE | 主 |
| 64 | 开始颜色抓取 | FE EF 00 46 EE | 主 |
| 65 | 开始追踪人脸 | FE EF 00 47 EE | 主 |
| 66 | 开始追踪黄色 | FE EF 00 48 EE | 主 |
| 67 | 开始追踪红色 | FE EF 00 49 EE | 主 |
| 68 | 开始追踪绿色 | FE EF 00 4A EE | 主 |
| 69 | 开始追踪蓝色 | FE EF 00 4B EE | 主 |
| 70 | 取消追踪 | FE EF 00 4C EE | 主 |
| 71 | 夹取黄色 | FE EF 00 4D EE | 主 |
| 72 | 夹取红色 | FE EF 00 4E EE | 主 |
| 73 | 夹取绿色 | FE EF 00 4F EE | 主 |
| 74 | 夹取蓝色 | FE EF 00 50 EE | 主 |
| 75 | 放置完成 | FE EF 00 51 EE | 主 |
| 76 | 推倒 | FE EF 00 52 EE | 主 |
| 77 | 开始分拣 | FE EF 00 5C EE | 主 |
| 78 | 红色 | FE EF 00 57 EE | 主 |
| 79 | 绿色 | FE EF 00 58 EE | 主 |
| 80 | 蓝色 | FE EF 00 59 EE | 主 |
| 81 | 黄色 | FE EF 00 5A EE | 主 |
| 82 | 不要 | FE EF 00 5B EE | 主 |
| 83 | 这是什么垃圾 | FE EF 00 5E EE | 主 |
| 113 | 打扫房间 | FE EF 00 8B EE | 主 |

### Passive Announcement Words (ID 84-112, 114)

| ID | Command Word | Serial Frame | Playback Mode |
|---|---|---|---|
| 84 | 这是红色 | FE EF FF 5F EE | 被 |
| 85 | 这是蓝色 | FE EF FF 60 EE | 被 |
| 86 | 这是绿色 | FE EF FF 61 EE | 被 |
| 87 | 这是黄色 | FE EF FF 62 EE | 被 |
| 88 | 识别到黄色 | FE EF FF 63 EE | 被 |
| 89 | 识别到绿色 | FE EF FF 64 EE | 被 |
| 90 | 识别到蓝色 | FE EF FF 65 EE | 被 |
| 91 | 识别到红色 | FE EF FF 66 EE | 被 |
| 92 | 初始化完成 | FE EF FF 67 EE | 被 |
| 93 | 第一个要排序的颜色是 | FE EF FF 68 EE | 被 |
| 94 | 第二个要排序的颜色是 | FE EF FF 69 EE | 被 |
| 95 | 第三个要排序的颜色是 | FE EF FF 6A EE | 被 |
| 96 | 第四个要排序的颜色是 | FE EF FF 6B EE | 被 |
| 97 | 这是易拉罐,属于可回收垃圾 | FE EF FF 6C EE | 被 |
| 98 | 这是旧书包,属于可回收垃圾 | FE EF FF 6D EE | 被 |
| 99 | 这是报纸,属于可回收垃圾 | FE EF FF 6E EE | 被 |
| 100 | 这是书本,属于可回收垃圾 | FE EF FF 6F EE | 被 |
| 101 | 这是注射器,属于有毒垃圾 | FE EF FF 70 EE | 被 |
| 102 | 这是废旧电池,属于有毒垃圾 | FE EF FF 71 EE | 被 |
| 103 | 这是过期化妆品,属于有毒垃圾 | FE EF FF 72 EE | 被 |
| 104 | 这是过期药品,属于有毒垃圾 | FE EF FF 73 EE | 被 |
| 105 | 这是鱼骨,属于湿垃圾 | FE EF FF 74 EE | 被 |
| 106 | 这是西瓜皮,属于湿垃圾 | FE EF FF 75 EE | 被 |
| 107 | 这是苹果核,属于湿垃圾 | FE EF FF 76 EE | 被 |
| 108 | 这是鸡蛋壳,属于湿垃圾 | FE EF FF 77 EE | 被 |
| 109 | 这是一次性筷子,属于干垃圾 | FE EF FF 78 EE | 被 |
| 110 | 这是烟蒂,属于干垃圾 | FE EF FF 79 EE | 被 |
| 111 | 这是桃核,属于干垃圾 | FE EF FF 80 EE | 被 |
| 112 | 这是卫生纸,属于干垃圾 | FE EF FF 8A EE | 被 |
| 114 | 现在是晴天 | FE EF FF 8C EE | 被 |

---

## 11. ROS2 Topics

| Topic | Type | Direction | Description |
|---|---|---|---|
| `/juxi_voice_cmd` | String | Publish | Recognized command text |
| `/juxi_passive_play` | String | Subscribe | Passive announcement text → write to 0xD1 (I2C) or send a serial frame |
| `/juxi_func_play` | String | Subscribe | Function word announcement text → write to 0xD2 (I2C) or send a serial frame |
| `/juxi_cmd_play` | String | Subscribe | Command word announcement text → write to 0xD3 (I2C) or send a serial frame |
| `/juxi_visual_marker` | Marker | Publish | RViz visualization marker |

---

## 12. Troubleshooting

**"AI voice interaction module not detected" on startup**

Check whether the device file corresponding to the wiring method exists:
```bash
# I2C 接线
ls /dev/i2c-1
sudo i2cdetect -y 1   # 应看到 0x2A

# Type-C 接线
ls /dev/ttyUSB0 /dev/ttyACM0

# UART 接线
ls /dev/ttyAMA0 /dev/ttyS0
```

**Serial permission error**

```bash
sudo chmod 666 /dev/ttyUSB0   # 或 /dev/ttyACM0 等
```

**I2C permission error**

```bash
sudo chmod 666 /dev/i2c-1
```

**No cube in RViz**

- Check whether Fixed Frame is `map`
- Check whether Topic is `/juxi_visual_marker`

**No response to commands after wake-up**

```bash
ros2 topic echo /juxi_voice_cmd
```
Data present → RViz configuration issue; no data → wiring/communication problem.
