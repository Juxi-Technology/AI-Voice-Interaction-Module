[English](README.md) | 简体中文

# 树莓派语音交互模块使用说明

## 安装依赖

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## 启用I2C

```bash
sudo raspi-config
```
选择 `Interface Options` -> `I2C` -> `Yes`

重启树莓派

## IIC版本

### 文件位置
`IIC_Voice/iic_voice.py

### 接线说明
| 树莓派 | 语音模块 |
|-------|----------|
| GPIO2 (SDA) | SDA |
| GPIO3 (SCL) | SCL |
| GND | GND |
| 5V | 5V |

![img](https://juxitech.feishu.cn/space/api/box/stream/download/asynccode/?code=YjI3YTllMmYzM2RkMzYzMmM3MTM2MmFiZTYzYjlhYjdfNnkzcEJnTkVrZ3hIbTY0cVExRDExeU5XRnJwZVRwektfVG9rZW46VFl6TGJ4Vk1EbzVWM1J4RUlobmNHaTRFbkdnXzE3ODQyNzkyOTA6MTc4NDI4Mjg5MF9WNA&add_watermark=true&scene_type=CCM)

### 运行

```bash
cd IIC_Voice
python3 iic_voice.py
```

### 输出格式
```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## UART版本

### 文件位置
`UART_Voice/uart_voice.py

### 启用串口
编辑 `/boot/firmware/config.txt` 或 `/boot/config.txt`，确保以下配置：
```
enable_uart=1
dtoverlay=disable-bt
```

然后重启树莓派。

```
sudo reboot
```

### 接线说明

Type直连树莓派时，取消注释SERIAL_PORT = '/dev/ttyUSB0'，注释掉SERIAL_PORT = '/dev/ttyAMA0'

![](C:\Users\qq141\AppData\Roaming\Typora\typora-user-images\image-20260701162405794.png)

通过UART针脚连接树莓派

| 树莓派 | 语音模块 |
|-------|----------|
| GPIO14 (TXD) | RX |
| GPIO15 (RXD) | TX |
| GND | GND |
| 5V | 5V |

注释掉SERIAL_PORT = '/dev/ttyUSB0'
取消注释SERIAL_PORT = '/dev/ttyAMA0'

![](C:\Users\qq141\AppData\Roaming\Typora\typora-user-images\image-20260701162229241.png)

### 运行

```bash
cd UART_Voice
python3 uart_voice.py
```

### 输出格式
```
Speech Serial Opened! Baudrate=115200
ID:4
ID:1
ID:10
```

## 协议说明

### UART协议
| 字节 | 内容 |
|------|------|
| 1 | 0xFE (帧头) |
| 2 | 0xEF (帧头) |
| 3 | 功能词ID |
| 4 | 命令词ID |
| 5 | 0xEE (结束帧) |

### IIC协议
- 设备地址: 0x2A
- 读取寄存器: 0xDA (读取1字节)
  - 0x00: 未识别
  - 其他: 命令词ID
