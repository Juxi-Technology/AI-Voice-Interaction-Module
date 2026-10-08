#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import time
import math
from std_msgs.msg import String
from visualization_msgs.msg import Marker, MarkerArray


class RvizCubeControl:
    def __init__(self):
        self.cube_x, self.cube_y, self.cube_z = 0.0, 0.0, 0.0
        self.cube_color = (1.0, 1.0, 1.0)
        self.cube_alpha = 1.0
        self.cube_scale = 0.5
        self.move_step = 0.5

        self.arm_position = 0.0
        self.rotation_yaw = 0.0
        self.line_follow_color = None
        self.follow_enabled = False
        self.alarm_active = False
        self.current_action = "初始位置"
        self.battery_visible = False
        self.light_mode = "normal"

        self.nav_positions = {
            29: (2.0, 0.0),
            30: (2.0, 2.0),
            31: (0.0, 2.0),
            32: (-2.0, 2.0),
        }

        self.marker_pub = rospy.Publisher('/juxi_visual_marker', Marker, queue_size=10)
        self.marker_array_pub = rospy.Publisher('/juxi_visual_markers', MarkerArray, queue_size=10)
        self.cmd_sub = rospy.Subscriber('/juxi_voice_cmd', String, self._cmd_callback)
        rospy.Timer(rospy.Duration(0.1), self._publish_marker)
        rospy.loginfo("RViz节点启动完成")

    def _cmd_callback(self, msg):
        cmd = msg.data
        rospy.loginfo("收到: %s", cmd)

        if cmd == "小车前进":
            self.cube_x += self.move_step
        elif cmd == "小车后退":
            self.cube_x -= self.move_step
        elif cmd == "小车左转":
            self.cube_y += self.move_step
        elif cmd == "小车右转":
            self.cube_y -= self.move_step
        elif cmd in ["小车左旋", "向左"]:
            self.rotation_yaw += 45.0
        elif cmd in ["小车右旋", "向右"]:
            self.rotation_yaw -= 45.0
        elif cmd == "小车停止":
            self.cube_color = (0.5, 0.5, 0.5)
        elif cmd == "停车":
            self.cube_color = (0.5, 0.5, 0.5)
        elif cmd == "小车休眠":
            self.cube_color = (0.3, 0.3, 0.3)
        elif cmd == "向上":
            self.cube_z += self.move_step
        elif cmd == "向下":
            self.cube_z -= self.move_step
            self.cube_z = max(0.0, self.cube_z)
        elif cmd == "关灯":
            self.cube_color = (0.0, 0.0, 0.0)
            self.cube_alpha = 0.3
            self.light_mode = "normal"
        elif cmd == "亮红灯":
            self.cube_color = (1.0, 0.0, 0.0)
            self.cube_alpha = 1.0
            self.light_mode = "normal"
        elif cmd == "亮绿灯":
            self.cube_color = (0.0, 1.0, 0.0)
            self.cube_alpha = 1.0
            self.light_mode = "normal"
        elif cmd == "亮蓝灯":
            self.cube_color = (0.0, 0.0, 1.0)
            self.cube_alpha = 1.0
            self.light_mode = "normal"
        elif cmd == "亮黄灯":
            self.cube_color = (1.0, 1.0, 0.0)
            self.cube_alpha = 1.0
            self.light_mode = "normal"
        elif cmd == "打开流水灯":
            self.light_mode = "flow"
        elif cmd == "打开渐变灯":
            self.light_mode = "gradient"
        elif cmd == "打开呼吸灯":
            self.light_mode = "breath"
        elif cmd == "回到原点":
            self.cube_x = self.cube_y = self.cube_z = 0.0
            self.cube_color = (1.0, 1.0, 1.0)
            self.cube_alpha = 1.0
            self.cube_scale = 0.5
            self.arm_position = 0.0
            self.rotation_yaw = 0.0
            self.line_follow_color = None
            self.follow_enabled = False
            self.alarm_active = False
            self.current_action = "初始位置"
            self.battery_visible = False
            self.light_mode = "normal"
        elif cmd == "夹紧":
            self.cube_scale = 0.25
        elif cmd == "松开":
            self.cube_scale = 0.5
        elif cmd == "显示电量":
            self.battery_visible = True
            self.cube_color = (0.0, 0.8, 0.8)
        elif cmd == "导航去一号位":
            self.cube_x, self.cube_y = self.nav_positions[29]
            self.cube_color = (0.2, 0.8, 0.4)
        elif cmd == "导航去二号位":
            self.cube_x, self.cube_y = self.nav_positions[30]
            self.cube_color = (0.2, 0.8, 0.4)
        elif cmd == "导航去三号位":
            self.cube_x, self.cube_y = self.nav_positions[31]
            self.cube_color = (0.2, 0.8, 0.4)
        elif cmd == "导航去四号位":
            self.cube_x, self.cube_y = self.nav_positions[32]
            self.cube_color = (0.2, 0.8, 0.4)
        elif cmd == "关闭巡线":
            self.line_follow_color = None
            self.cube_color = (1.0, 1.0, 1.0)
        elif cmd == "巡红线":
            self.line_follow_color = "red"
            self.cube_color = (1.0, 0.2, 0.2)
        elif cmd == "巡绿线":
            self.line_follow_color = "green"
            self.cube_color = (0.2, 1.0, 0.2)
        elif cmd == "巡蓝线":
            self.line_follow_color = "blue"
            self.cube_color = (0.2, 0.2, 1.0)
        elif cmd == "巡黄线":
            self.line_follow_color = "yellow"
            self.cube_color = (1.0, 1.0, 0.2)
        elif cmd == "开启跟随":
            self.follow_enabled = True
            self.cube_color = (0.8, 0.2, 0.8)
        elif cmd == "关闭跟随":
            self.follow_enabled = False
            self.cube_color = (1.0, 1.0, 1.0)
        elif cmd == "报警":
            self.alarm_active = True
            self.cube_color = (1.0, 0.0, 0.0)
        elif cmd == "鼓掌":
            self.current_action = "鼓掌"
            self.cube_color = (1.0, 0.6, 0.2)
        elif cmd == "点头":
            self.current_action = "点头"
            self.cube_color = (0.2, 1.0, 0.6)
        elif cmd == "祈祷":
            self.current_action = "祈祷"
            self.cube_color = (0.6, 0.2, 1.0)
        elif cmd == "跪下":
            self.current_action = "跪下"
            self.cube_scale = 0.3
            self.cube_z = 0.2
        elif cmd == "初始位置":
            self.current_action = "初始位置"
            self.cube_scale = 0.5
            self.cube_z = 0.0
            self.cube_color = (1.0, 1.0, 1.0)
        elif cmd == "惊吓":
            self.current_action = "惊吓"
            self.cube_color = (0.5, 0.5, 1.0)
            self.cube_z += 0.2
        elif cmd == "叠罗汉":
            self.current_action = "叠罗汉"
            self.cube_color = (0.8, 0.8, 0.2)
            self.cube_scale = 0.4
        elif cmd == "跳舞":
            self.current_action = "跳舞"
            self.cube_color = (0.2, 0.8, 1.0)
        elif cmd == "夹方块":
            self.current_action = "夹方块"
            self.cube_scale = 0.3
        elif cmd == "搬运":
            self.current_action = "搬运"
            self.cube_color = (0.6, 0.4, 0.2)
        elif cmd == "推倒":
            self.current_action = "推倒"
            self.cube_scale = 0.3
            self.cube_z = 0.05
            self.cube_color = (0.9, 0.2, 0.1)
        elif cmd == "输入完成":
            self.cube_color = (0.4, 0.9, 0.4)
        elif cmd == "输入结束":
            self.cube_color = (0.5, 0.5, 0.5)
        elif cmd == "运动动作":
            self.current_action = "运动动作"
            self.cube_color = (0.2, 0.7, 0.8)
        elif cmd == "清除动作":
            self.current_action = "初始位置"
            self.cube_color = (1.0, 1.0, 1.0)
            self.cube_scale = 0.5
            self.cube_z = 0.0
        elif cmd == "这是什么颜色":
            self.current_action = "这是什么颜色"
            self.cube_color = (0.9, 0.9, 0.3)
        elif cmd == "开始颜色分拣":
            self.current_action = "颜色分拣"
            self.cube_color = (0.3, 0.9, 0.5)
        elif cmd == "开始颜色抓取":
            self.current_action = "颜色抓取"
            self.cube_color = (0.3, 0.6, 0.9)
        elif cmd == "开始追踪人脸":
            self.current_action = "追踪人脸"
            self.cube_color = (1.0, 0.7, 0.4)
        elif cmd == "开始追踪黄色":
            self.current_action = "追踪黄色"
            self.cube_color = (1.0, 1.0, 0.2)
        elif cmd == "开始追踪红色":
            self.current_action = "追踪红色"
            self.cube_color = (1.0, 0.2, 0.2)
        elif cmd == "开始追踪绿色":
            self.current_action = "追踪绿色"
            self.cube_color = (0.2, 1.0, 0.2)
        elif cmd == "开始追踪蓝色":
            self.current_action = "追踪蓝色"
            self.cube_color = (0.2, 0.2, 1.0)
        elif cmd == "取消追踪":
            self.current_action = "初始位置"
            self.cube_color = (1.0, 1.0, 1.0)
        elif cmd == "夹取黄色":
            self.current_action = "夹取黄色"
            self.cube_scale = 0.25
            self.cube_color = (1.0, 1.0, 0.2)
        elif cmd == "夹取红色":
            self.current_action = "夹取红色"
            self.cube_scale = 0.25
            self.cube_color = (1.0, 0.2, 0.2)
        elif cmd == "夹取绿色":
            self.current_action = "夹取绿色"
            self.cube_scale = 0.25
            self.cube_color = (0.2, 1.0, 0.2)
        elif cmd == "夹取蓝色":
            self.current_action = "夹取蓝色"
            self.cube_scale = 0.25
            self.cube_color = (0.2, 0.2, 1.0)
        elif cmd == "放置完成":
            self.cube_scale = 0.5
            self.cube_color = (0.4, 0.9, 0.4)
        elif cmd == "开始分拣":
            self.current_action = "开始分拣"
            self.cube_color = (0.5, 0.8, 0.3)
        elif cmd == "打扫房间":
            self.current_action = "打扫房间"
            self.cube_color = (0.6, 0.9, 0.6)
        elif cmd == "这是什么垃圾":
            self.current_action = "垃圾分类"
            self.cube_color = (0.7, 0.8, 0.3)
        elif cmd == "红色":
            self.cube_color = (1.0, 0.0, 0.0)
        elif cmd == "绿色":
            self.cube_color = (0.0, 1.0, 0.0)
        elif cmd == "蓝色":
            self.cube_color = (0.0, 0.0, 1.0)
        elif cmd == "黄色":
            self.cube_color = (1.0, 1.0, 0.0)
        elif cmd == "不要":
            self.cube_color = (0.5, 0.5, 0.5)

    def _update_light_effects(self):
        t = time.time()
        if self.light_mode == "flow":
            colors = [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0), (1.0, 1.0, 0.0)]
            idx = int(t * 2) % 4
            self.cube_color = colors[idx]
        elif self.light_mode == "gradient":
            r = 0.5 + 0.5 * (t * 0.5)
            g = 0.5 + 0.5 * (t * 0.7 + 2)
            b = 0.5 + 0.5 * (t * 0.9 + 4)
            self.cube_color = (r % 1.0, g % 1.0, b % 1.0)
        elif self.light_mode == "breath":
            alpha = 0.3 + 0.7 * abs((t * 2) % 2 - 1)
            self.cube_alpha = alpha

    def _publish_marker(self, event):
        self._update_light_effects()

        marker_array = MarkerArray()

        main_marker = Marker()
        main_marker.header.frame_id = "map"
        main_marker.header.stamp = rospy.Time.now()
        main_marker.ns = "juxi_cube"
        main_marker.id = 0
        main_marker.type = Marker.CUBE
        main_marker.action = Marker.ADD

        main_marker.pose.position.x = self.cube_x
        main_marker.pose.position.y = self.cube_y
        main_marker.pose.position.z = self.cube_z

        half_yaw = math.radians(self.rotation_yaw) / 2.0
        main_marker.pose.orientation.z = math.sin(half_yaw)
        main_marker.pose.orientation.w = math.cos(half_yaw)

        main_marker.scale.x = main_marker.scale.y = main_marker.scale.z = self.cube_scale

        main_marker.color.r = float(self.cube_color[0])
        main_marker.color.g = float(self.cube_color[1])
        main_marker.color.b = float(self.cube_color[2])
        main_marker.color.a = float(self.cube_alpha)

        marker_array.markers.append(main_marker)

        if self.arm_position != 0:
            arm_marker = Marker()
            arm_marker.header.frame_id = "map"
            arm_marker.header.stamp = rospy.Time.now()
            arm_marker.ns = "juxi_arm"
            arm_marker.id = 1
            arm_marker.type = Marker.CUBE
            arm_marker.action = Marker.ADD
            arm_marker.pose.position.x = self.cube_x + self.arm_position
            arm_marker.pose.position.y = self.cube_y
            arm_marker.pose.position.z = self.cube_z + 0.5
            arm_marker.pose.orientation.w = 1.0
            arm_marker.scale.x = 0.1
            arm_marker.scale.y = 0.1
            arm_marker.scale.z = 0.4
            arm_marker.color.r = 0.5
            arm_marker.color.g = 0.5
            arm_marker.color.b = 0.5
            arm_marker.color.a = 1.0
            marker_array.markers.append(arm_marker)

        if self.battery_visible:
            battery_marker = Marker()
            battery_marker.header.frame_id = "map"
            battery_marker.header.stamp = rospy.Time.now()
            battery_marker.ns = "juxi_battery"
            battery_marker.id = 2
            battery_marker.type = Marker.TEXT_VIEW_FACING
            battery_marker.action = Marker.ADD
            battery_marker.pose.position.x = self.cube_x
            battery_marker.pose.position.y = self.cube_y
            battery_marker.pose.position.z = self.cube_z + 1.0
            battery_marker.pose.orientation.w = 1.0
            battery_marker.scale.z = 0.3
            battery_marker.color.r = 0.0
            battery_marker.color.g = 1.0
            battery_marker.color.b = 0.0
            battery_marker.color.a = 1.0
            battery_marker.text = "电量: 85%"
            marker_array.markers.append(battery_marker)

        if self.alarm_active:
            alarm_marker = Marker()
            alarm_marker.header.frame_id = "map"
            alarm_marker.header.stamp = rospy.Time.now()
            alarm_marker.ns = "juxi_alarm"
            alarm_marker.id = 3
            alarm_marker.type = Marker.SPHERE
            alarm_marker.action = Marker.ADD
            alarm_marker.pose.position.x = self.cube_x
            alarm_marker.pose.position.y = self.cube_y
            alarm_marker.pose.position.z = self.cube_z + 0.8
            alarm_marker.pose.orientation.w = 1.0
            pulse = 0.2 + 0.3 * abs((time.time() * 4) % 2 - 1)
            alarm_marker.scale.x = alarm_marker.scale.y = alarm_marker.scale.z = pulse
            alarm_marker.color.r = 1.0
            alarm_marker.color.g = 0.0
            alarm_marker.color.b = 0.0
            alarm_marker.color.a = 0.8
            marker_array.markers.append(alarm_marker)

        self.marker_pub.publish(main_marker)
        self.marker_array_pub.publish(marker_array)


def main():
    rospy.init_node('juxi_rviz_node')
    node = RvizCubeControl()
    rospy.spin()

if __name__ == '__main__':
    main()
