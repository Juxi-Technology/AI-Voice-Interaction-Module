English | [简体中文](README_CN.md)

Open the attached command word / announcement phrase protocol list (`../../docs/command-words-v1-zh.xlsx`) — it contains both the transmit and the receive protocols.

# 1. Function word entries

The file lists the transmit and receive frames for 10 function word entries.

![1](images/1.png)

Function word entries can be told apart by the third byte of the frame.

![2](images/2.png)

The first two bytes (`FE EF`) are the frame header, the third byte is the function word ID, the fourth byte is the command word ID, and the fifth byte (`EE`) is the frame tail.

# 2. Command word entries

A command word entry looks like this — the fourth byte is the ID.

![3](images/3.png)

Example:

if we say "小车停止" (car stop) to the module, it sends `FE EF 00 01 EE` over its serial port. The host receives this in its serial service function, then parses the fourth byte to get ID `0x01` — which tells us the command was "小车停止".

# 3. Announcement phrases

Announcement phrases are never played unprompted — the host must send a serial command to play them. (A command word's announcement phrase can also be played this way.)

![4](images/4.png)

The first two bytes (`FE EF`) are the frame header, the third byte is the announcement function `FF`, the fourth byte is the ID of the phrase to play, and the fifth byte (`EE`) is the frame tail.

Example:

to play "初始化完成", the host sends `FE EF FF 67 EE` to the module, which then plays "初始化完成".

![5](images/5.png)
