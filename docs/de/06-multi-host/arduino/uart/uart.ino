#include <Arduino.h>
#include "bsp_uart.hpp"

int lastCommandId = 0;

void setup() {
  Serial.begin(115200);
  UART_Init();
  
  Serial.println("UART Voice Module Initialized");
  
  UART_SetCommandVoice(0x00);
  delay(200);
}

void loop() {
  int commandId = UART_ReadCommand();
  
  if (commandId >= 0) {
    if (commandId != 0 && commandId != 255 && commandId != lastCommandId) {
      Serial.print("ID: ");
      Serial.println(commandId);
      lastCommandId = commandId;
      
      if (commandId == 1) {
        UART_SetCommandVoice(0x00);
      } else if (commandId == 2) {
        UART_SetCommandVoice(0x00);
      }
    } else if (commandId == 0 || commandId == 255) {
      if (lastCommandId != 0) {
        lastCommandId = 0;
      }
    }
  }
  
  delay(50);
}
