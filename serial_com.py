#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#****************************************
#@ 文件        :serial_com.py
#@ 说明        :
#@ 时间        :2021/04/07 17:24:50
#@ 作者        :Dannie
#@ 版本        :1.0
#****************************************

import serial
import serial.tools.list_ports

# 获取可用串口列表
# port_list = list(serial.tools.list_ports.comports())
# if len(port_list) == 0:
#     print('No Port!')
# else:
#     for i in range(0,len(port_list)):
#         print(port_list[i]) 


# 从串口读数据
# try:
#     # 端口：CNU； Linux上的/dev /ttyUSB0等； windows上的COM3等
#     portx = 'COM2'
#     # 波特率，标准值有：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
#     bps = 115200
#     # 超时设置，None：永远等待操作；
#     # 0：立即返回请求结果；
#     # 其他：等待超时时间（单位为秒）
#     timex = None
    
#     # 打开串口，并得到串口对象
#     ser = serial.Serial(portx, bps, timeout=timex)
#     # print('串口详情参数：', ser)

#     # 读一个字节
#     # print(ser.read().hex()) # 十六进制的读取
#     print(ser.read()) # ASIIC码显示
#     ser.close()

# except Exception as e:
#     print('error !', e)


# 从串口写
# try:
#     portx = 'COM2'
#     bps = 115200
#     timex = 5

#     ser = serial.Serial(portx, bps, timeout=timex)
#     result = ser.write('Hello World'.encode('gbk'))
#     print('写总字节数：', result)
#     ser.close()   # 关闭串口

# except Exception as e:
#     print('error !', e)