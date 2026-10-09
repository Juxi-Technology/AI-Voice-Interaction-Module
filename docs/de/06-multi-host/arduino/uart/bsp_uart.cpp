#include "bsp_uart.hpp"

SoftwareSerial voiceSerial(10, 11);

void UART_Init(void)
{
  voiceSerial.begin(115200);
}

int UART_ReadCommand(void)
{
  static uint8_t buffer[5];
  static uint8_t index = 0;
  
  while (voiceSerial.available()) {
    uint8_t data = voiceSerial.read();
    
    if (index == 0 && data == FRAME_HEADER1) {
      buffer[index++] = data;
    } else if (index == 1 && data == FRAME_HEADER2) {
      buffer[index++] = data;
    } else if (index >= 2 && index < 4) {
      buffer[index++] = data;
    } else if (index == 4 && data == FRAME_TAIL) {
      buffer[index] = data;
      index = 0;
      return buffer[3];
    } else {
      index = 0;
    }
  }
  
  return -1;
}

void UART_SetPassiveVoice(uint8_t voiceID)
{
  uint8_t frame[5] = {FRAME_HEADER1, FRAME_HEADER2, 0xD1, voiceID, FRAME_TAIL};
  voiceSerial.write(frame, 5);
}

void UART_SetFunctionVoice(uint8_t voiceID)
{
  uint8_t frame[5] = {FRAME_HEADER1, FRAME_HEADER2, 0xD2, voiceID, FRAME_TAIL};
  voiceSerial.write(frame, 5);
}

void UART_SetCommandVoice(uint8_t voiceID)
{
  uint8_t frame[5] = {FRAME_HEADER1, FRAME_HEADER2, 0xD3, voiceID, FRAME_TAIL};
  voiceSerial.write(frame, 5);
}
