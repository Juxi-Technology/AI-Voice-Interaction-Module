#ifndef __BSP_IIC_HPP_
#define __BSP_IIC_HPP_

#include <Arduino.h>
#include <Wire.h>

#ifdef __cplusplus
extern "C" {
#endif

#define VoiceADDR    0x2A
#define REG_RESULT   0xDA
#define REG_PASSIVE  0xD1
#define REG_FUNCTION 0xD2
#define REG_COMMAND  0xD3

void IIC_Init(void);
int IIC_ReadCommand(void);
void IIC_SetPassiveVoice(uint8_t voiceID);
void IIC_SetFunctionVoice(uint8_t voiceID);
void IIC_SetCommandVoice(uint8_t voiceID);

#ifdef __cplusplus
}
#endif

#endif
