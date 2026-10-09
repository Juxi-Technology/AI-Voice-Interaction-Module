#!/usr/bin/env python3
import serial

# Type-C 数据线连接
SERIAL_PORT = '/dev/ttyUSB0'  # 需手动编译ch341驱动时，改为ttyCH341USB0

# UART 连接
#SERIAL_PORT = '/dev/ttyTHS1'

BAUD_RATE = 115200

buffer = []

print("Speech Serial Opened! Baudrate=115200")

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=0.1)

    while True:
        data = ser.read(1)
        if data:
            byte = ord(data)
            buffer.append(byte)

            if len(buffer) >= 5:
                if buffer[0] == 0xFE and buffer[1] == 0xEF and buffer[4] == 0xEE:
                    command_id = buffer[3]
                    print(f"ID:{command_id}")
                buffer = []

except serial.SerialException as e:
    print(f"Serial Error: {e}")
except KeyboardInterrupt:
    print()
