#include <Arduino.h>
#include "bsp_iic.hpp"

int lastCommandId = 0;

void setup() {
  Serial.begin(115200);
  IIC_Init();
  
  Serial.println("IIC Voice Module Initialized");
  
  IIC_SetCommandVoice(0x00);
  delay(200);
}

void loop() {
  int commandId = IIC_ReadCommand();
  
  if (commandId >= 0) {
    if (commandId != 0 && commandId != 255 && commandId != lastCommandId) {
      Serial.print("ID: ");
      Serial.println(commandId);
      lastCommandId = commandId;
      
      if (commandId == 1) {
        IIC_SetCommandVoice(0x00);
      } else if (commandId == 2) {
        IIC_SetCommandVoice(0x00);
      }
    } else if (commandId == 0 || commandId == 255) {
      if (lastCommandId != 0) {
        lastCommandId = 0;
      }
    }
  } else {
    Serial.println("IIC Read Error");
    delay(1000);
  }
  
  delay(50);
}
