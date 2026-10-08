cmake_minimum_required(VERSION 3.0.2)
project(juxi_voice)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  visualization_msgs
)

catkin_package(
  CATKIN_DEPENDS rospy std_msgs visualization_msgs
)

catkin_install_python(PROGRAMS
  scripts/voice_node.py
  scripts/rviz_control.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(FILES
  juxi_voice.rviz
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
  FILES_MATCHING PATTERN "*.launch"
)
