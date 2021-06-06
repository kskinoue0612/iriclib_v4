#ifndef IRICLIB_GUI_COORP_H
#define IRICLIB_GUI_COORP_H

#include "iriclib_global.h"

#ifdef __cplusplus
extern "C" {
#endif

int IRICLIBDLL iRIC_Write_Sol_End(const char* fname);
int IRICLIBDLL iRIC_Check_Lock(const char* fname);
int IRICLIBDLL iRIC_Check_Cancel();

#ifdef __cplusplus
}
#endif

#endif // IRICLIB_GUI_COORP_H
