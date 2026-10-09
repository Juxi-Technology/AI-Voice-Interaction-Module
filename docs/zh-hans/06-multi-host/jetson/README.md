[English](../../../en/06-multi-host/jetson/README.md) | [Deutsch](../../../de/06-multi-host/jetson/README.md) | [Español](../../../es/06-multi-host/jetson/README.md) | [Français](../../../fr/06-multi-host/jetson/README.md) | [Italiano](../../../it/06-multi-host/jetson/README.md) | [日本語](../../../ja/06-multi-host/jetson/README.md) | [한국어](../../../ko/06-multi-host/jetson/README.md) | [Português (BR)](../../../pt-br/06-multi-host/jetson/README.md) | [Português (PT)](../../../pt-pt/06-multi-host/jetson/README.md) | 简体中文 | [繁體中文](../../../zh-hant/06-multi-host/jetson/README.md)

# Jetson语音交互模块使用说明

## 安装依赖

```bash
sudo apt-get update
sudo apt-get install -y python3-smbus python3-serial i2c-tools
```

## 检查用户组

```bash
sudo usermod -aG i2c $USER
sudo usermod -aG dialout $USER
```
注销并重新登录生效。

## IIC版本

### 文件位置
`IIC_Voice/iic_voice.py`

### 接线说明
| Jetson | 语音模块 |
|--------|----------|
| Pin 27 (I2C1 SDA) | SDA |
| Pin 28 (I2C1 SCL) | SCL |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### 检查I2C设备
```bash
sudo i2cdetect -y -r 1
```
应能看到地址 0x2A

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
`UART_Voice/uart_voice.py`

模块通过UART针脚连接到Jetson，注释掉SERIAL_PORT = '/dev/ttyUSB0'，取消注释SERIAL_PORT = '/dev/ttyTHS1'

![image-20260701185853347](C:\Users\qq141\AppData\Roaming\Typora\typora-user-images\image-20260701185853347.png)

### 接线说明

| Jetson | 语音模块 |
|--------|----------|
| Pin 8 (UART1 TX) | RX |
| Pin 10 (UART1 RX) | TX |
| Pin 6 (GND) | GND |
| Pin 4 (5V) | 5V |

### 检查串口
```bash
ls /dev/ttyTHS*
```

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

模块通过Type数据线连接到Jetson，取消注释SERIAL_PORT = '/dev/ttyUSB0'，注释掉SERIAL_PORT = '/dev/ttyTHS1'

![image-20260701185812787](C:\Users\qq141\AppData\Roaming\Typora\typora-user-images\image-20260701185812787.png)

### 检查串口

```bash
ls /dev/ttyUSB*
```

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

## 常见问题

### I2C权限问题
```bash
sudo chmod 666 /dev/i2c-1
```

### 串口被占用
如果串口无法打开，请检查是否被其他服务占用：
```bash
sudo systemctl stop nvgetty
sudo systemctl disable nvgetty
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
