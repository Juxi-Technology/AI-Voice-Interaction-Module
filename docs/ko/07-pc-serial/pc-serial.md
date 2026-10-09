[English](../../en/07-pc-serial/pc-serial.md) | [Deutsch](../../de/07-pc-serial/pc-serial.md) | [Español](../../es/07-pc-serial/pc-serial.md) | [Français](../../fr/07-pc-serial/pc-serial.md) | [Italiano](../../it/07-pc-serial/pc-serial.md) | [日本語](../../ja/07-pc-serial/pc-serial.md) | 한국어 | [Português (BR)](../../pt-br/07-pc-serial/pc-serial.md) | [Português (PT)](../../pt-pt/07-pc-serial/pc-serial.md) | [简体中文](../../zh-hans/07-pc-serial/pc-serial.md) | [繁體中文](../../zh-hant/07-pc-serial/pc-serial.md)

# 1. 장치 연결

슬라이드 스위치를 STC8 시리얼 포트 모드로 옮깁니다.

![1](../../en/07-pc-serial/images/1.png)

# 2. 시리얼 디버그 어시스턴트 열기

- Uart Assistant를 열고 해당 시리얼 포트 번호를 선택한 뒤 보드 레이트를 115200으로 설정합니다.

![2](../../en/07-pc-serial/images/2.png)

- 압축 파일의 "命令词播报词协议列表V1\_中文"(명령어/방송어 프로토콜 목록 V1\_중국어) 파일을 참조합니다.

![3](../../en/07-pc-serial/images/3.png)

- "小车前进"(차량 전진)이라고 말하면 시리얼 디버그 어시스턴트가 해당 프로토콜을 출력합니다.

![4](../../en/07-pc-serial/images/4.png)

| 11   | 小车停止 | 명령 | 好的,已停止       | 능동 | FE EF 00 01 EE | FE EF 00 01 EE |
| ---- | -------- | ------- | ----------------- | ------ | -------------- | -------------- |
| 12   | 停车     | 명령 | 好的,已停止       | 능동 | FE EF 00 02 EE | FE EF 00 02 EE |
| 13   | 小车休眠 | 명령 | 好的,已休眠       | 능동 | FE EF 00 03 EE | FE EF 00 03 EE |
| 14   | 小车前进 | 명령 | 好的,正在前进     | 능동 | FE EF 00 04 EE | FE EF 00 04 EE |
| 15   | 小车后退 | 명령 | 好的,正在后退     | 능동 | FE EF 00 05 EE | FE EF 00 05 EE |
| 16   | 小车左转 | 명령 | 好的,正在向左转   | 능동 | FE EF 00 06 EE | FE EF 00 06 EE |
| 17   | 小车右转 | 명령 | 好的,正在向右转   | 능동 | FE EF 00 07 EE | FE EF 00 07 EE |
| 18   | 小车左旋 | 명령 | 好的,正在向左旋转 | 능동 | FE EF 00 08 EE | FE EF 00 08 EE |
| 19   | 小车右旋 | 명령 | 好的,正在向右旋转 | 능동 | FE EF 00 09 EE | FE EF 00 09 EE |

- "命令词播报词协议列表V1\_中文" 파일에 따라 해당 명령을 입력하면, 음성 모듈이 해당 프로토콜의 텍스트를 재생합니다.

| 84   | 这是红色                  | 명령 | 这是红色                  | 수동 | FE EF FF 5F EE | FE EF FF 5F EE |
| ---- | ------------------------- | ------- | ------------------------- | ------- | -------------- | -------------- |
| 85   | 这是蓝色                  | 명령 | 这是蓝色                  | 수동 | FE EF FF 60 EE | FE EF FF 60 EE |
| 86   | 这是绿色                  | 명령 | 这是绿色                  | 수동 | FE EF FF 61 EE | FE EF FF 61 EE |
| 87   | 这是黄色                  | 명령 | 这是黄色                  | 수동 | FE EF FF 62 EE | FE EF FF 62 EE |
| 88   | 识别到黄色                | 명령 | 识别到黄色                | 수동 | FE EF FF 63 EE | FE EF FF 63 EE |
| 89   | 识别到绿色                | 명령 | 识别到绿色                | 수동 | FE EF FF 64 EE | FE EF FF 64 EE |
| 90   | 识别到蓝色                | 명령 | 识别到蓝色                | 수동 | FE EF FF 65 EE | FE EF FF 65 EE |
| 91   | 识别到红色                | 명령 | 识别到红色                | 수동 | FE EF FF 66 EE | FE EF FF 66 EE |
| 92   | 初始化完成                | 명령 | 初始化完成                | 수동 | FE EF FF 67 EE | FE EF FF 67 EE |
| 93   | 第一个要排序的颜色是      | 명령 | 第一个要排序的颜色是      | 수동 | FE EF FF 68 EE | FE EF FF 68 EE |
| 94   | 第二个要排序的颜色是      | 명령 | 第二个要排序的颜色是      | 수동 | FE EF FF 69 EE | FE EF FF 69 EE |
| 95   | 第三个要排序的颜色是      | 명령 | 第三个要排序的颜色是      | 수동 | FE EF FF 6A EE | FE EF FF 6A EE |
| 96   | 第四个要排序的颜色是      | 명령 | 第四个要排序的颜色是      | 수동 | FE EF FF 6B EE | FE EF FF 6B EE |
| 97   | 这是易拉罐,属于可回收垃圾 | 명령 | 这是易拉罐,属于可回收垃圾 | 수동 | FE EF FF 6C EE | FE EF FF 6C EE |

![5](../../en/07-pc-serial/images/5.png)

음성 모듈이 정상적으로 재생되는 것을 들을 수 있습니다.
