#ifndef __BSP_UART_HPP_
#define __BSP_UART_HPP_

#include <Arduino.h>
#include <SoftwareSerial.h>

#ifdef __cplusplus
extern "C" {
#endif

#define FRAME_HEADER1 0xFE
#define FRAME_HEADER2 0xEF
#define FRAME_TAIL 0xEE

void UART_Init(void);
int UART_ReadCommand(void);
void UART_SetPassiveVoice(uint8_t voiceID);
void UART_SetFunctionVoice(uint8_t voiceID);
void UART_SetCommandVoice(uint8_t voiceID);

#ifdef __cplusplus
}
#endif

#endif
