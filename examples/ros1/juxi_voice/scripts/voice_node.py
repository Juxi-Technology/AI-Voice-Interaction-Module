#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import time
import os
from std_msgs.msg import String

HEADER_1 = 0xFE
HEADER_2 = 0xEF
TAIL = 0xEE
FRAME_LEN = 5
I2C_SLAVE_ADDR = 0x2A
I2C_BUS_NUM = 1
REG_RESULT = 0xDA
REG_PASSIVE = 0xD1
REG_FUNC = 0xD2
REG_CMD = 0xD3

CMD_DATA = {
    1:   (0x01, 0x00, "欢迎语", "被"),
    2:   (0x02, 0x00, "休息语", "主"),
    3:   (0x03, 0x00, "你好小犀", "主"),
    4:   (0x04, 0x00, "增大音量", "主"),
    5:   (0x05, 0x00, "减小音量", "主"),
    6:   (0x06, 0x00, "最大音量", "主"),
    7:   (0x07, 0x00, "中等音量", "主"),
    8:   (0x08, 0x00, "最小音量", "主"),
    9:   (0x09, 0x00, "开启播报", "主"),
    10:  (0x0A, 0x00, "关闭播报", "主"),
    11:  (0x00, 0x01, "小车停止", "主"),
    12:  (0x00, 0x02, "停车", "主"),
    13:  (0x00, 0x03, "小车休眠", "主"),
    14:  (0x00, 0x04, "小车前进", "主"),
    15:  (0x00, 0x05, "小车后退", "主"),
    16:  (0x00, 0x06, "小车左转", "主"),
    17:  (0x00, 0x07, "小车右转", "主"),
    18:  (0x00, 0x08, "小车左旋", "主"),
    19:  (0x00, 0x09, "小车右旋", "主"),
    20:  (0x00, 0x0A, "关灯", "主"),
    21:  (0x00, 0x0B, "亮红灯", "主"),
    22:  (0x00, 0x0C, "亮绿灯", "主"),
    23:  (0x00, 0x0D, "亮蓝灯", "主"),
    24:  (0x00, 0x0E, "亮黄灯", "主"),
    25:  (0x00, 0x0F, "打开流水灯", "主"),
    26:  (0x00, 0x10, "打开渐变灯", "主"),
    27:  (0x00, 0x11, "打开呼吸灯", "主"),
    28:  (0x00, 0x12, "显示电量", "主"),
    29:  (0x00, 0x13, "导航去一号位", "主"),
    30:  (0x00, 0x14, "导航去二号位", "主"),
    31:  (0x00, 0x15, "导航去三号位", "主"),
    32:  (0x00, 0x20, "导航去四号位", "主"),
    33:  (0x00, 0x21, "回到原点", "主"),
    34:  (0x00, 0x16, "关闭巡线", "主"),
    35:  (0x00, 0x17, "巡红线", "主"),
    36:  (0x00, 0x18, "巡绿线", "主"),
    37:  (0x00, 0x19, "巡蓝线", "主"),
    38:  (0x00, 0x1A, "巡黄线", "主"),
    39:  (0x00, 0x1B, "开启跟随", "主"),
    40:  (0x00, 0x1C, "关闭跟随", "主"),
    41:  (0x00, 0x26, "报警", "主"),
    42:  (0x00, 0x27, "向上", "主"),
    43:  (0x00, 0x28, "向下", "主"),
    44:  (0x00, 0x29, "向左", "主"),
    45:  (0x00, 0x2A, "向右", "主"),
    46:  (0x00, 0x2B, "夹紧", "主"),
    47:  (0x00, 0x2C, "松开", "主"),
    48:  (0x00, 0x2D, "鼓掌", "主"),
    49:  (0x00, 0x2E, "点头", "主"),
    50:  (0x00, 0x2F, "祈祷", "主"),
    51:  (0x00, 0x30, "跪下", "主"),
    52:  (0x00, 0x31, "初始位置", "主"),
    53:  (0x00, 0x32, "惊吓", "主"),
    54:  (0x00, 0x33, "叠罗汉", "主"),
    55:  (0x00, 0x34, "跳舞", "主"),
    56:  (0x00, 0x35, "夹方块", "主"),
    57:  (0x00, 0x36, "搬运", "主"),
    58:  (0x00, 0x37, "输入完成", "主"),
    59:  (0x00, 0x38, "输入结束", "主"),
    60:  (0x00, 0x39, "运动动作", "主"),
    61:  (0x00, 0x3A, "清除动作", "主"),
    62:  (0x00, 0x3C, "这是什么颜色", "主"),
    63:  (0x00, 0x3D, "开始颜色分拣", "主"),
    64:  (0x00, 0x46, "开始颜色抓取", "主"),
    65:  (0x00, 0x47, "开始追踪人脸", "主"),
    66:  (0x00, 0x48, "开始追踪黄色", "主"),
    67:  (0x00, 0x49, "开始追踪红色", "主"),
    68:  (0x00, 0x4A, "开始追踪绿色", "主"),
    69:  (0x00, 0x4B, "开始追踪蓝色", "主"),
    70:  (0x00, 0x4C, "取消追踪", "主"),
    71:  (0x00, 0x4D, "夹取黄色", "主"),
    72:  (0x00, 0x4E, "夹取红色", "主"),
    73:  (0x00, 0x4F, "夹取绿色", "主"),
    74:  (0x00, 0x50, "夹取蓝色", "主"),
    75:  (0x00, 0x51, "放置完成", "主"),
    76:  (0x00, 0x52, "推倒", "主"),
    77:  (0x00, 0x5C, "开始分拣", "主"),
    78:  (0x00, 0x57, "红色", "主"),
    79:  (0x00, 0x58, "绿色", "主"),
    80:  (0x00, 0x59, "蓝色", "主"),
    81:  (0x00, 0x5A, "黄色", "主"),
    82:  (0x00, 0x5B, "不要", "主"),
    83:  (0x00, 0x5E, "这是什么垃圾", "主"),
    84:  (0xFF, 0x5F, "这是红色", "被"),
    85:  (0xFF, 0x60, "这是蓝色", "被"),
    86:  (0xFF, 0x61, "这是绿色", "被"),
    87:  (0xFF, 0x62, "这是黄色", "被"),
    88:  (0xFF, 0x63, "识别到黄色", "被"),
    89:  (0xFF, 0x64, "识别到绿色", "被"),
    90:  (0xFF, 0x65, "识别到蓝色", "被"),
    91:  (0xFF, 0x66, "识别到红色", "被"),
    92:  (0xFF, 0x67, "初始化完成", "被"),
    93:  (0xFF, 0x68, "第一个要排序的颜色是", "被"),
    94:  (0xFF, 0x69, "第二个要排序的颜色是", "被"),
    95:  (0xFF, 0x6A, "第三个要排序的颜色是", "被"),
    96:  (0xFF, 0x6B, "第四个要排序的颜色是", "被"),
    97:  (0xFF, 0x6C, "这是易拉罐,属于可回收垃圾", "被"),
    98:  (0xFF, 0x6D, "这是旧书包,属于可回收垃圾", "被"),
    99:  (0xFF, 0x6E, "这是报纸,属于可回收垃圾", "被"),
    100: (0xFF, 0x6F, "这是书本,属于可回收垃圾", "被"),
    101: (0xFF, 0x70, "这是注射器,属于有毒垃圾", "被"),
    102: (0xFF, 0x71, "这是废旧电池,属于有毒垃圾", "被"),
    103: (0xFF, 0x72, "这是过期化妆品,属于有毒垃圾", "被"),
    104: (0xFF, 0x73, "这是过期药品,属于有毒垃圾", "被"),
    105: (0xFF, 0x74, "这是鱼骨,属于湿垃圾", "被"),
    106: (0xFF, 0x75, "这是西瓜皮,属于湿垃圾", "被"),
    107: (0xFF, 0x76, "这是苹果核,属于湿垃圾", "被"),
    108: (0xFF, 0x77, "这是鸡蛋壳,属于湿垃圾", "被"),
    109: (0xFF, 0x78, "这是一次性筷子,属于干垃圾", "被"),
    110: (0xFF, 0x79, "这是烟蒂,属于干垃圾", "被"),
    111: (0xFF, 0x80, "这是桃核,属于干垃圾", "被"),
    112: (0xFF, 0x8A, "这是卫生纸,属于干垃圾", "被"),
    113: (0x00, 0x8B, "打扫房间", "主"),
    114: (0xFF, 0x8C, "现在是晴天", "被"),
}

FUNC_IDS    = set(range(1, 11))
CMD_IDS     = set(range(11, 83)) | {83, 113}
PASSIVE_IDS = set(range(84, 113)) | {114}

SERIAL_TO_ID = {(b2, b3): cid for cid, (b2, b3, _, _) in CMD_DATA.items()}

SERIAL_PORTS = [
    "/dev/ttyUSB0",
    "/dev/ttyACM0",
    "/dev/ttyAMA0",
    "/dev/ttyS0",
]


class I2CBackend:
    def __init__(self):
        from smbus2 import SMBus
        self._bus = SMBus(I2C_BUS_NUM)

    def close(self):
        if self._bus:
            try:
                self._bus.close()
            except Exception:
                pass

    def read_cmd_id(self):
        try:
            cmd_id = self._bus.read_byte_data(I2C_SLAVE_ADDR, REG_RESULT)
        except Exception:
            return None
        return cmd_id if cmd_id != 0x00 else None

    def send_playback(self, cmd_id):
        if cmd_id in FUNC_IDS:
            reg = REG_FUNC
        elif cmd_id in PASSIVE_IDS:
            reg = REG_PASSIVE
        else:
            reg = REG_CMD
        try:
            self._bus.write_byte_data(I2C_SLAVE_ADDR, reg, cmd_id)
            time.sleep(0.005)
        except Exception as e:
            rospy.logwarn("I2C写入失败 (reg=0x%02X id=%d): %s", reg, cmd_id, e)

    def description(self):
        return "IIC /dev/i2c-%d (从机地址 0x%02X)" % (I2C_BUS_NUM, I2C_SLAVE_ADDR)


class SerialBackend:
    def __init__(self, port, baudrate):
        import serial
        self._port = port
        self._ser = serial.Serial(port, baudrate, timeout=0.01)
        self._buf = bytearray()

    def close(self):
        if self._ser and self._ser.is_open:
            try:
                self._ser.close()
            except Exception:
                pass

    def read_cmd_id(self):
        if not self._ser or not self._ser.is_open:
            return None
        try:
            avail = self._ser.in_waiting
            if avail < 1:
                return None
            self._buf.extend(self._ser.read(avail))
        except Exception:
            return None

        while len(self._buf) >= FRAME_LEN:
            b0 = self._buf[0]
            b1 = self._buf[1]
            b4 = self._buf[4]
            if b0 == HEADER_1 and b1 == HEADER_2 and b4 == TAIL:
                b2 = self._buf[2]
                b3 = self._buf[3]
                del self._buf[:FRAME_LEN]
                try:
                    return SERIAL_TO_ID[(b2, b3)]
                except KeyError:
                    rospy.logwarn("未知帧: FE EF %02X %02X EE", b2, b3)
                    return None
            else:
                del self._buf[0]

        if len(self._buf) > 256:
            self._buf.clear()
        return None

    def send_playback(self, cmd_id):
        if not self._ser or not self._ser.is_open:
            return
        b2, b3, _, _ = CMD_DATA[cmd_id]
        frame = bytes([HEADER_1, HEADER_2, b2, b3, TAIL])
        try:
            self._ser.write(frame)
            time.sleep(0.005)
        except Exception as e:
            rospy.logwarn("串口写入失败: %s", e)

    def description(self):
        return "UART %s" % self._port


def detect_connection():
    import serial
    for port in SERIAL_PORTS:
        if not os.path.exists(port):
            rospy.loginfo("检测串口: %s 不存在，跳过", port)
            continue
        try:
            ser = serial.Serial(port, 115200, timeout=0.1)
            ser.close()
            backend = SerialBackend(port, 115200)
            rospy.loginfo("自动检测: %s", backend.description())
            return backend
        except serial.SerialException:
            rospy.loginfo("检测串口: %s 打开失败，跳过", port)
        except Exception as e:
            rospy.loginfo("检测串口: %s 异常: %s，跳过", port, e)

    i2c_path = "/dev/i2c-%d" % I2C_BUS_NUM
    if os.path.exists(i2c_path):
        try:
            from smbus2 import SMBus
            bus = SMBus(I2C_BUS_NUM)
            bus.read_byte_data(I2C_SLAVE_ADDR, REG_RESULT)
            bus.close()
            backend = I2CBackend()
            rospy.loginfo("自动检测: %s", backend.description())
            return backend
        except Exception:
            rospy.loginfo("检测I2C: %s 无设备 0x%02X 响应", i2c_path, I2C_SLAVE_ADDR)

    return None


class VoiceControlNode:
    def __init__(self):
        self.is_awake = False

        self.pub_cmd = rospy.Publisher('/juxi_voice_cmd', String, queue_size=10)
        self.sub_passive = rospy.Subscriber(
            '/juxi_passive_play', String, self._passive_callback)
        self.sub_func = rospy.Subscriber(
            '/juxi_func_play', String, self._func_callback)
        self.sub_cmd_play = rospy.Subscriber(
            '/juxi_cmd_play', String, self._cmd_play_callback)

        self._backend = detect_connection()
        if self._backend is None:
            rospy.logfatal(
                "未检测到AI语音交互模块！请检查接线 (Type-C / UART / IIC)")
            rospy.logfatal(
                "支持的端口: I2C(/dev/i2c-1) | 串口(/dev/ttyUSB0 "
                "/dev/ttyACM0 /dev/ttyAMA0 /dev/ttyS0)")
        else:
            rospy.loginfo("语音节点启动完成 - %s", self._backend.description())

        rospy.Timer(rospy.Duration(0.05), self._read_result)

    def _read_result(self, event):
        if self._backend is None:
            return
        cmd_id = self._backend.read_cmd_id()
        if cmd_id is None:
            return

        _, _, text, mode = CMD_DATA[cmd_id]

        if cmd_id == 3:
            self.is_awake = True
            rospy.loginfo("已唤醒: %s", text)
            self._backend.send_playback(cmd_id)
            return

        if not self.is_awake:
            return

        msg = String()
        msg.data = text
        self.pub_cmd.publish(msg)
        rospy.loginfo("发送指令 (ID=%d): %s [%s]", cmd_id, text, mode)

    def _passive_callback(self, msg):
        if self._backend is None:
            return
        play_text = msg.data
        for cid in PASSIVE_IDS:
            if CMD_DATA[cid][2] == play_text:
                self._backend.send_playback(cid)
                rospy.loginfo("被动播报 (ID=%d): %s", cid, play_text)
                return
        rospy.logwarn("未找到被动播报文本: %s", play_text)

    def _func_callback(self, msg):
        if self._backend is None:
            return
        play_text = msg.data
        for cid in FUNC_IDS:
            if CMD_DATA[cid][2] == play_text:
                self._backend.send_playback(cid)
                rospy.loginfo("功能词播报 (ID=%d): %s", cid, play_text)
                return
        rospy.logwarn("未找到功能词文本: %s", play_text)

    def _cmd_play_callback(self, msg):
        if self._backend is None:
            return
        play_text = msg.data
        for cid in CMD_IDS:
            if CMD_DATA[cid][2] == play_text:
                self._backend.send_playback(cid)
                rospy.loginfo("命令词播报 (ID=%d): %s", cid, play_text)
                return
        rospy.logwarn("未找到命令词文本: %s", play_text)

    def shutdown(self):
        if self._backend:
            self._backend.close()


def main():
    rospy.init_node('juxi_voice_node')
    node = VoiceControlNode()
    rospy.on_shutdown(node.shutdown)
    rospy.spin()

if __name__ == '__main__':
    main()
