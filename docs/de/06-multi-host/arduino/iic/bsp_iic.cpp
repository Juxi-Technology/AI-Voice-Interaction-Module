#include "bsp_iic.hpp"

void IIC_Init(void)
{
  Wire.begin();
}

int IIC_ReadCommand(void)
{
  Wire.beginTransmission(VoiceADDR);
  Wire.write(REG_RESULT);
  uint8_t error = Wire.endTransmission();
  
  if (error != 0) {
    return -1;
  }
  
  Wire.requestFrom((uint8_t)VoiceADDR, (uint8_t)1);
  if (Wire.available()) {
    return Wire.read();
  }
  
  return -1;
}

void IIC_SetPassiveVoice(uint8_t voiceID)
{
  Wire.beginTransmission(VoiceADDR);
  Wire.write(REG_PASSIVE);
  Wire.write(voiceID);
  Wire.endTransmission();
}

void IIC_SetFunctionVoice(uint8_t voiceID)
{
  Wire.beginTransmission(VoiceADDR);
  Wire.write(REG_FUNCTION);
  Wire.write(voiceID);
  Wire.endTransmission();
}

void IIC_SetCommandVoice(uint8_t voiceID)
{
  Wire.beginTransmission(VoiceADDR);
  Wire.write(REG_COMMAND);
  Wire.write(voiceID);
  Wire.endTransmission();
}
