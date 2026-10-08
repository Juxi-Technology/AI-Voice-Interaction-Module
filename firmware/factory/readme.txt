1. For detailed information about the SDK's components, features, and development, please refer to the SDK documentation for the corresponding chip series in the Software Development section of the Docume
   Taking CI13060 as an example, the reference link is as follows: https://document.chipintelli.com/%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91/SDK/CI130X%E8%8A%AF%E7%89%87SDK/CI-SDK-Offline/

2. If you need to modify and adjust the relevant algorithm parameters in the SDK, please refer to the SDK documentation for the corresponding chip series in the Software Development section of the Documentation Center.
   Taking AEC as an example, the reference link is as follows:：https://document.chipintelli.com/%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91/SDK/CI130X%E8%8A%AF%E7%89%87SDK/components/%E5%9B%9E%E5%A3%B0%E6%B6%88%E9%99%A4%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E/

3. If the firmware size exceeds the flash capacity of the selected chip, please try again after switching to a smaller acoustic model, reducing the number of command words or voice prompts, or using a chip with larger flash capacity.

4. If algorithms are enabled, the system provides relatively less memory space for language model. To ensure normal recognition operation, please reduce the number of command words.


The firmware communication protocol is as follows:
<welcome>:FE EF 01 00 EE:FE EF 01 00 EE
<inactivate>:FE EF 02 00 EE:FE EF 02 00 EE
你好小犀:FE EF 03 00 EE:FE EF 03 00 EE
增大音量:FE EF 04 00 EE:FE EF 04 00 EE
减小音量:FE EF 05 00 EE:FE EF 05 00 EE
最大音量:FE EF 06 00 EE:FE EF 06 00 EE
中等音量:FE EF 07 00 EE:FE EF 07 00 EE
最小音量:FE EF 08 00 EE:FE EF 08 00 EE
开启播报:FE EF 09 00 EE:FE EF 09 00 EE
关闭播报:FE EF 0A 00 EE:FE EF 0A 00 EE
小车停止:FE EF 00 01 EE:FE EF 00 01 EE
停车:FE EF 00 02 EE:FE EF 00 02 EE
小车休眠:FE EF 00 03 EE:FE EF 00 03 EE
小车前进:FE EF 00 04 EE:FE EF 00 04 EE
小车后退:FE EF 00 05 EE:FE EF 00 05 EE
小车左转:FE EF 00 06 EE:FE EF 00 06 EE
小车右转:FE EF 00 07 EE:FE EF 00 07 EE
小车左旋:FE EF 00 08 EE:FE EF 00 08 EE
小车右旋:FE EF 00 09 EE:FE EF 00 09 EE
关灯:FE EF 00 0A EE:FE EF 00 0A EE
亮红灯:FE EF 00 0B EE:FE EF 00 0B EE
亮绿灯:FE EF 00 0C EE:FE EF 00 0C EE
亮蓝灯:FE EF 00 0D EE:FE EF 00 0D EE
亮黄灯:FE EF 00 0E EE:FE EF 00 0E EE
打开流水灯:FE EF 00 0F EE:FE EF 00 0F EE
打开渐变灯:FE EF 00 10 EE:FE EF 00 10 EE
打开呼吸灯:FE EF 00 11 EE:FE EF 00 11 EE
显示电量:FE EF 00 12 EE:FE EF 00 12 EE
导航去一号位:FE EF 00 13 EE:FE EF 00 13 EE
导航去二号位:FE EF 00 14 EE:FE EF 00 14 EE
导航去三号位:FE EF 00 15 EE:FE EF 00 15 EE
导航去四号位:FE EF 00 20 EE:FE EF 00 20 EE
回到原点:FE EF 00 21 EE:FE EF 00 21 EE
关闭巡线:FE EF 00 16 EE:FE EF 00 16 EE
巡红线:FE EF 00 17 EE:FE EF 00 17 EE
巡绿线:FE EF 00 18 EE:FE EF 00 18 EE
巡蓝线:FE EF 00 19 EE:FE EF 00 19 EE
巡黄线:FE EF 00 1A EE:FE EF 00 1A EE
开启跟随:FE EF 00 1B EE:FE EF 00 1B EE
关闭跟随:FE EF 00 1C EE:FE EF 00 1C EE
报警:FE EF 00 26 EE:FE EF 00 26 EE
向上:FE EF 00 27 EE:FE EF 00 27 EE
向下:FE EF 00 28 EE:FE EF 00 28 EE
向左:FE EF 00 29 EE:FE EF 00 29 EE
向右:FE EF 00 2A EE:FE EF 00 2A EE
夹紧:FE EF 00 2B EE:FE EF 00 2B EE
松开:FE EF 00 2C EE:FE EF 00 2C EE
鼓掌:FE EF 00 2D EE:FE EF 00 2D EE
点头:FE EF 00 2E EE:FE EF 00 2E EE
祈祷:FE EF 00 2F EE:FE EF 00 2F EE
跪下:FE EF 00 30 EE:FE EF 00 30 EE
初始位置:FE EF 00 31 EE:FE EF 00 31 EE
惊吓:FE EF 00 32 EE:FE EF 00 32 EE
叠罗汉:FE EF 00 33 EE:FE EF 00 33 EE
跳舞:FE EF 00 34 EE:FE EF 00 34 EE
夹方块:FE EF 00 35 EE:FE EF 00 35 EE
搬运:FE EF 00 36 EE:FE EF 00 36 EE
输入完成:FE EF 00 37 EE:FE EF 00 37 EE
输入结束:FE EF 00 38 EE:FE EF 00 38 EE
运动动作:FE EF 00 39 EE:FE EF 00 39 EE
清除动作:FE EF 00 3A EE:FE EF 00 3A EE
这是什么颜色:FE EF 00 3C EE:FE EF 00 3C EE
开始颜色分拣:FE EF 00 3D EE:FE EF 00 3D EE
开始颜色抓取:FE EF 00 46 EE:FE EF 00 46 EE
开始追踪人脸:FE EF 00 47 EE:FE EF 00 47 EE
开始追踪黄色:FE EF 00 48 EE:FE EF 00 48 EE
开始追踪红色:FE EF 00 49 EE:FE EF 00 49 EE
开始追踪绿色:FE EF 00 4A EE:FE EF 00 4A EE
开始追踪蓝色:FE EF 00 4B EE:FE EF 00 4B EE
取消追踪:FE EF 00 4C EE:FE EF 00 4C EE
夹取黄色:FE EF 00 4D EE:FE EF 00 4D EE
夹取红色:FE EF 00 4E EE:FE EF 00 4E EE
夹取绿色:FE EF 00 4F EE:FE EF 00 4F EE
夹取蓝色:FE EF 00 50 EE:FE EF 00 50 EE
放置完成:FE EF 00 51 EE:FE EF 00 51 EE
推倒:FE EF 00 52 EE:FE EF 00 52 EE
开始分拣:FE EF 00 5C EE:FE EF 00 5C EE
红色:FE EF 00 57 EE:FE EF 00 57 EE
绿色:FE EF 00 58 EE:FE EF 00 58 EE
蓝色:FE EF 00 59 EE:FE EF 00 59 EE
黄色:FE EF 00 5A EE:FE EF 00 5A EE
不要:FE EF 00 5B EE:FE EF 00 5B EE
这是什么垃圾:FE EF 00 5E EE:FE EF 00 5E EE
这是红色:FE EF FF 5F EE:FE EF FF 5F EE
这是蓝色:FE EF FF 60 EE:FE EF FF 60 EE
这是绿色:FE EF FF 61 EE:FE EF FF 61 EE
这是黄色:FE EF FF 62 EE:FE EF FF 62 EE
识别到黄色:FE EF FF 63 EE:FE EF FF 63 EE
识别到绿色:FE EF FF 64 EE:FE EF FF 64 EE
识别到蓝色:FE EF FF 65 EE:FE EF FF 65 EE
识别到红色:FE EF FF 66 EE:FE EF FF 66 EE
初始化完成:FE EF FF 67 EE:FE EF FF 67 EE
第一个要排序的颜色是:FE EF FF 68 EE:FE EF FF 68 EE
第二个要排序的颜色是:FE EF FF 69 EE:FE EF FF 69 EE
第三个要排序的颜色是:FE EF FF 6A EE:FE EF FF 6A EE
第四个要排序的颜色是:FE EF FF 6B EE:FE EF FF 6B EE
这是易拉罐属于可回收垃圾:FE EF FF 6C EE:FE EF FF 6C EE
这是旧书包属于可回收垃圾:FE EF FF 6D EE:FE EF FF 6D EE
这是报纸属于可回收垃圾:FE EF FF 6E EE:FE EF FF 6E EE
这是书本属于可回收垃圾:FE EF FF 6F EE:FE EF FF 6F EE
这是注射器属于有毒垃圾:FE EF FF 70 EE:FE EF FF 70 EE
这是废旧电池属于有毒垃圾:FE EF FF 71 EE:FE EF FF 71 EE
这是过期化妆品属于有毒垃圾:FE EF FF 72 EE:FE EF FF 72 EE
这是过期药品属于有毒垃圾:FE EF FF 73 EE:FE EF FF 73 EE
这是鱼骨属于湿垃圾:FE EF FF 74 EE:FE EF FF 74 EE
这是西瓜皮属于湿垃圾:FE EF FF 75 EE:FE EF FF 75 EE
这是苹果核属于湿垃圾:FE EF FF 76 EE:FE EF FF 76 EE
这是鸡蛋壳属于湿垃圾:FE EF FF 77 EE:FE EF FF 77 EE
这是一次性筷子属于干垃圾:FE EF FF 78 EE:FE EF FF 78 EE
这是烟蒂属于干垃圾:FE EF FF 79 EE:FE EF FF 79 EE
这是桃核属于干垃圾:FE EF FF 80 EE:FE EF FF 80 EE
这是卫生纸属于干垃圾:FE EF FF 8A EE:FE EF FF 8A EE
不要过来:FE EF 00 8B EE:FE EF 00 8B EE
现在是晚上:FE EF FF 8C EE:FE EF FF 8C EE
