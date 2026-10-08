[English](ros1-rviz.md) | 简体中文

# ROS1-rviz可视化 (Type-C / UART / IIC 三合一版)

## 1、环境准备

#### 系统要求

- **操作系统**：Ubuntu 20.04 或 18.04
- **ROS1 版本**：Noetic (推荐) 或 Melodic

#### 安装依赖库

```bash
# 1. 更新源
sudo apt update

# 2. 安装 ROS1 桌面完整版
# (如果已安装ROS1，跳过)
# sudo apt install ros-noetic-desktop-full -y    # Ubuntu 20.04
# sudo apt install ros-melodic-desktop-full -y   # Ubuntu 18.04

# 3. 安装本项目依赖（同时支持串口和I2C）
sudo apt install python3-pip ros-noetic-rviz i2c-tools -y
pip3 install pyserial smbus2

# 如果是 Melodic (Python2)
# sudo apt install python-pip ros-melodic-rviz i2c-tools -y
# pip install pyserial smbus2

# 4. 如果使用 I2C 接线，额外安装
sudo apt install python3-smbus2 -y
```

---

## 2、三种接线方式说明

AI语音交互模块支持以下三种接线方式：

| 接线方式 | 接口 | 设备文件 | 协议 | 波特率 |
|---|---|---|---|---|
| **Type-C** | USB Type-C | `/dev/ttyUSB0` 或 `/dev/ttyACM0` | 串口帧 `FE EF XX YY EE` | 115200 |
| **UART** | GPIO 串口引脚 | `/dev/ttyAMA0` 或 `/dev/ttyS0` | 串口帧 `FE EF XX YY EE` | 115200 |
| **IIC** | I2C 总线 (SDA/SCL) | `/dev/i2c-1` | 寄存器读写 (0x2A) | — |

#### 自动检测机制

ROS1节点启动时会按以下顺序自动检测接线方式：
1. 先尝试串口：依次检测 `/dev/ttyUSB0` → `/dev/ttyACM0` → `/dev/ttyAMA0` → `/dev/ttyS0`
2. 再尝试 I2C：检测 `/dev/i2c-1` 上是否存在从机 `0x2A`
3. 串口检测只需设备文件存在且可打开即认为可用，无需额外验证

检测到任意一种方式后即停止检测并锁定使用该方式。无需任何手动配置。

---

## 3、IIC 协议说明

#### IIC 从机配置

| 参数 | 值 |
|---|---|
| IIC 从机地址 | **0x2A** |
| IIC 总线 | /dev/i2c-1 |

#### 寄存器定义

| 寄存器地址 | 读写 | 说明 |
|---|---|---|
| **0xDA** | R | 识别结果寄存器，读取1字节 = 命令词ID。未识别到时结果为 0x00。 |
| **0xD1** | W | 被动播报语音寄存器，写入1字节命令词ID。 |
| **0xD2** | W | 功能词播报语音寄存器，写入1字节命令词ID。 |
| **0xD3** | W | 命令词播报语音寄存器，写入1字节命令词ID。 |

---

## 4、串口协议说明 (Type-C / UART)

#### 帧格式

每帧固定为 **5字节**：

| 字节0 | 字节1 | 字节2 | 字节3 | 字节4 |
|---|---|---|---|---|
| 0xFE | 0xEF | 命令高字节 | 命令低字节 | 0xEE |
| 帧头 | 帧头 | CMD_H | CMD_L | 帧尾 |

#### 波特率

固定 **115200** bps。

---

## 5、创建工作空间与目录结构

#### 创建 catkin 工作空间

```bash
mkdir -p ~/juxi_speech_ws/src
cd ~/juxi_speech_ws/src
```

#### 创建 ROS 功能包

```bash
catkin_create_pkg juxi_voice rospy std_msgs visualization_msgs
```

#### 最终目录结构

将本项目提供的文件放置到对应位置：

```
~/juxi_speech_ws/
├── build/
├── devel/
└── src/
    └── juxi_voice/
        ├── CMakeLists.txt      # (替换为本项目提供的)
        ├── package.xml          # (替换为本项目提供的)
        ├── juxi_voice.rviz      # (新建：RViz预配置文件)
        ├── launch/
        │   └── juxi_voice.launch # (新建：一键启动文件)
        └── scripts/
            ├── voice_node.py     # (新建：语音节点)
            └── rviz_control.py   # (新建：RViz控制节点)
```

---

## 6、文件内容与放置

#### 文件 1：`voice_node.py` (语音控制节点)

**位置**：`~/juxi_speech_ws/src/juxi_voice/scripts/voice_node.py`

**核心功能**：
- 自动检测 Type-C / UART / IIC 接线方式
- 统一命令词映射表（114条命令词，与Excel协议表V1完全一致）
- 根据接线方式使用对应的通信后端（串口 / I2C）

**关键架构**：

```python
# 统一命令数据: ID → (串口字节2, 串口字节3, 命令文本, 播报模式)
CMD_DATA = {
    1:   (0x01, 0x00, "欢迎语", "被"),
    3:   (0x03, 0x00, "你好小犀", "主"),
    14:  (0x00, 0x04, "小车前进", "主"),
    84:  (0xFF, 0x5F, "这是红色", "被"),
    ...
}

# 自动检测函数
def detect_connection():
    # 1. 尝试串口 /dev/ttyUSB0, /dev/ttyACM0, /dev/ttyAMA0, /dev/ttyS0
    # 2. 尝试 I2C /dev/i2c-1 (从机地址 0x2A)
    ...
```

（完整代码请查看项目提供的 `voice_node.py` 文件）

#### 文件 2：`rviz_control.py` (RViz 控制节点)

**位置**：`~/juxi_speech_ws/src/juxi_voice/scripts/rviz_control.py`

订阅 `/juxi_voice_cmd` 话题接收命令文本，根据命令更新立方体可视化。

（完整代码请查看项目提供的 `rviz_control.py` 文件）

#### 文件 3：`CMakeLists.txt` 和 `package.xml`

已在本项目中提供，直接替换 `catkin_create_pkg` 自动生成的默认文件即可。

---

## 7、编译与运行

#### 编译

```bash
cd ~/juxi_speech_ws
catkin_make
```

#### 环境变量

```bash
source ~/juxi_speech_ws/devel/setup.bash
# 或写入 ~/.bashrc
echo "source ~/juxi_speech_ws/devel/setup.bash" >> ~/.bashrc
```

#### 权限设置

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
# 设置后需要重新登录生效
```

#### 运行节点

**方式一：一键启动（推荐）**

```bash
cd ~/juxi_speech_ws
source devel/setup.bash
roslaunch juxi_voice juxi_voice.launch
```

启动时会自动打开语音节点、RViz控制节点和RViz可视化界面。

**方式二：分步启动（3 个终端）**

**终端 1**：启动 roscore

```bash
roscore
```

**终端 2**：语音节点

```bash
cd ~/juxi_speech_ws
source devel/setup.bash
rosrun juxi_voice voice_node.py
```

启动时会显示检测到的接线方式：
```
[INFO] 自动检测: IIC /dev/i2c-1 (从机地址 0x2A)
[INFO] 语音节点启动完成 - IIC /dev/i2c-1 (从机地址 0x2A)
```
或
```
[INFO] 自动检测: UART /dev/ttyUSB0
[INFO] 语音节点启动完成 - UART /dev/ttyUSB0
```

如果未检测到任何设备：
```
[FATAL] 未检测到AI语音交互模块！请检查接线 (Type-C / UART / IIC)
[FATAL] 支持的端口: I2C(/dev/i2c-1) | 串口(/dev/ttyUSB0 /dev/ttyACM0 /dev/ttyAMA0 /dev/ttyS0)
```

**终端 3**：RViz 控制节点

```bash
cd ~/juxi_speech_ws
source devel/setup.bash
rosrun juxi_voice rviz_control.py
```

**终端 4**：RViz 可视化（直接加载预配文件，无需手动设置）

```bash
rviz -d ~/juxi_speech_ws/src/juxi_voice/juxi_voice.rviz
```

或者先打开 RViz 再加载：

```bash
rviz
# 菜单栏: File → Open Config → 选择 juxi_voice.rviz
```

---

## 8、RViz 预配说明

`juxi_voice.rviz` 已预配好以下内容，启动即可使用，无需任何手动操作：

- **Fixed Frame**：`map`
- **Marker 显示**：已订阅 `/juxi_visual_marker`（单标记）
- **MarkerArray 显示**：已订阅 `/juxi_visual_markers`（多标记：机械臂、电量、报警等）
- **视角**：从斜上方观察，中心点在原点

---

## 9、使用方法

#### 唤醒
对着模块说 **"你好小犀"** → 模块回复 "我在"

#### 发指令
- "小车前进" → 方块前进
- "亮红灯" → 方块变红色
- "打开流水灯" → 颜色循环变化
- "报警" → 红色脉冲球体
- "显示电量" → 电量文字

#### 主机触发播报

```bash
# 被动播报 (I2C → 写 0xD1, 串口 → 发 FE EF FF XX EE)
rostopic pub /juxi_passive_play std_msgs/String "data: '这是红色'"
# 功能词播报 (I2C → 写 0xD2, 串口 → 发 FE EF 01 00 EE)
rostopic pub /juxi_func_play std_msgs/String "data: '欢迎语'"
# 命令词播报 (I2C → 写 0xD3, 串口 → 发 FE EF 00 04 EE)
rostopic pub /juxi_cmd_play std_msgs/String "data: '小车前进'"
```

---

## 10、命令词ID对照表

> 共114条命令词，与`命令词播报词协议列表V1_中文.xlsx`完全一致。

### 功能词 (ID 1-10)

| ID | 命令词 | 串口帧 | 播报模式 |
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

### 命令词 (ID 11-83, 113)

| ID | 命令词 | 串口帧 | 播报模式 |
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

### 被动播报词 (ID 84-112, 114)

| ID | 命令词 | 串口帧 | 播报模式 |
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

## 11、ROS1 话题说明

| 话题 | 类型 | 方向 | 说明 |
|---|---|---|---|
| `/juxi_voice_cmd` | String | 发布 | 识别到的命令文本 |
| `/juxi_passive_play` | String | 订阅 | 被动播报文本 → 写入 0xD1（I2C）或发送串口帧 |
| `/juxi_func_play` | String | 订阅 | 功能词播报文本 → 写入 0xD2（I2C）或发送串口帧 |
| `/juxi_cmd_play` | String | 订阅 | 命令词播报文本 → 写入 0xD3（I2C）或发送串口帧 |
| `/juxi_visual_marker` | Marker | 发布 | RViz可视化标记 |
| `/juxi_visual_markers` | MarkerArray | 发布 | RViz多标记（机械臂、电量、报警等） |

---

## 12、常见问题排查

**启动时报"未检测到AI语音交互模块"**

检查接线方式对应的设备文件是否存在：
```bash
# I2C 接线
ls /dev/i2c-1
sudo i2cdetect -y 1   # 应看到 0x2A

# Type-C 接线
ls /dev/ttyUSB0 /dev/ttyACM0

# UART 接线
ls /dev/ttyAMA0 /dev/ttyS0
```

**串口权限报错**

```bash
sudo chmod 666 /dev/ttyUSB0   # 或 /dev/ttyACM0 等
# 或加入 dialout 用户组（需要重新登录）
sudo usermod -aG dialout $USER
```

**I2C 权限报错**

```bash
sudo chmod 666 /dev/i2c-1
# 或加入 i2c 用户组（需要重新登录）
sudo usermod -aG i2c $USER
```

**RViz 里没有方块**

- 检查 Fixed Frame 是否为 `map`
- 检查 Topic 是否为 `/juxi_visual_marker`
- 确认 rviz_control.py 节点已启动

**唤醒后说指令没反应**

```bash
rostopic echo /juxi_voice_cmd
```
有数据 → RViz 配置问题；无数据 → 接线/通信异常。

**rosrun 找不到节点**

确认已执行过编译和 source：
```bash
cd ~/juxi_speech_ws
catkin_make
source devel/setup.bash
```

**提示语法错误**

```bash
# 确认 Python 脚本有执行权限
chmod +x ~/juxi_speech_ws/src/juxi_voice/scripts/voice_node.py
chmod +x ~/juxi_speech_ws/src/juxi_voice/scripts/rviz_control.py
```
