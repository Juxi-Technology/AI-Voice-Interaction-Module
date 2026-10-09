#!/usr/bin/env python3
import smbus
import time

DEVICE_ADDRESS = 0x2A
REG_RESULT = 0xDA

bus = smbus.SMBus(1)
last_command_id = 0

print("Speech Serial Opened! Baudrate=115200")

try:
    while True:
        try:
            bus.write_byte(DEVICE_ADDRESS, REG_RESULT)
            time.sleep(0.005)
            command_id = bus.read_byte(DEVICE_ADDRESS)
            
            if command_id != 0 and command_id != 255 and command_id != last_command_id:
                print(f"ID:{command_id}")
                last_command_id = command_id
            elif command_id == 0 or command_id == 255:
                if last_command_id != 0:
                    last_command_id = 0
                    
        except OSError as e:
            print(f"I2C Error: {e}")
            time.sleep(1)
            
        time.sleep(0.05)
        
except KeyboardInterrupt:
    print()
