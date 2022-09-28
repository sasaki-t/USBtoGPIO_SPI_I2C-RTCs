#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file Adafruit_MCP2221A_Breakout.py
 @brief USB to Digital/Analog IO and I2C, UART components using Adafruit MCP2221A Breakout
 @date $Date$

 @author 佐々木毅 (Takeshi SASAKI) <sasaki-t(_at_)ieee.org>

"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

# Import CircuitPython modules
import os
os.environ['BLINKA_MCP2221'] = '1' #Setting Environmental Variable

import board
import digitalio
import busio
import analogio
import serial
from serial.tools import list_ports
from serial import SerialException
from enum import Enum

class GPIOtype(Enum):
    DI = 0
    DO = 1
    AI = 2
    AO = 3

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
adafruit_mcp2221a_breakout_spec = ["implementation_id", "Adafruit_MCP2221A_Breakout", 
         "type_name",         "Adafruit_MCP2221A_Breakout", 
         "description",       "USB to Digital/Analog IO and I2C, UART components using Adafruit MCP2221A Breakout", 
         "version",           "1.0.0", 
         "vendor",            "TakeshiSasaki", 
         "category",          "GPIO", 
         "activity_type",     "COMMUTATIVE", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.GPIO_G0_select", "DI",
         "conf.default.GPIO_G1_select", "DI",
         "conf.default.GPIO_G2_select", "DI",
         "conf.default.GPIO_G3_select", "DI",
         "conf.default.I2C_use", "0",
         "conf.default.I2C_device_address", "0x08",
         "conf.default.I2C_timeout", "1000",
         "conf.default.UART_use", "0",
         "conf.default.UART_port", "COM3",
         "conf.default.UART_baudrate", "115200",
         "conf.default.UART_read_timeout", "10.0",

         "conf.__widget__.GPIO_G0_select", "radio",
         "conf.__widget__.GPIO_G1_select", "radio",
         "conf.__widget__.GPIO_G2_select", "radio",
         "conf.__widget__.GPIO_G3_select", "radio",
         "conf.__widget__.I2C_use", "radio",
         "conf.__widget__.I2C_device_address", "text",
         "conf.__widget__.I2C_timeout", "text",
         "conf.__widget__.UART_use", "radio",
         "conf.__widget__.UART_port", "text",
         "conf.__widget__.UART_baudrate", "text",
         "conf.__widget__.UART_read_timeout", "text",
         "conf.__constraints__.GPIO_G0_select", "(DI,DO)",
         "conf.__constraints__.GPIO_G1_select", "(DI,DO,AI)",
         "conf.__constraints__.GPIO_G2_select", "(DI,DO,AI,AO)",
         "conf.__constraints__.GPIO_G3_select", "(DI,DO,AI,AO)",
         "conf.__constraints__.I2C_use", "(0,1)",
         "conf.__constraints__.I2C_timeout", "x>=0",
         "conf.__constraints__.UART_use", "(0,1)",
         "conf.__constraints__.UART_baudrate", "x>0",

         "conf.__type__.GPIO_G0_select", "string",
         "conf.__type__.GPIO_G1_select", "string",
         "conf.__type__.GPIO_G2_select", "string",
         "conf.__type__.GPIO_G3_select", "string",
         "conf.__type__.I2C_use", "int",
         "conf.__type__.I2C_device_address", "string",
         "conf.__type__.I2C_timeout", "int",
         "conf.__type__.UART_use", "int",
         "conf.__type__.UART_port", "string",
         "conf.__type__.UART_baudrate", "int",
         "conf.__type__.UART_read_timeout", "float",

         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class Adafruit_MCP2221A_Breakout
# @brief USB to Digital/Analog IO and I2C, UART components using Adafruit MCP2221A Breakout
# 
# Adafruit MCP2221A Breakoutを使用したUSB-GPIO, I2C,
# UART変換コンポーネント。GPIOに関しては、まずコンフィギュレーションから各ピンの利
# 用方法（アナログ/ディジタル、入力/出力）を選択する。出力として設定したピンに対し
# ては、対応するInPortに値が入力されると、その値に応じてディジタル出力であればHig
# h/Low、アナログ出力であれば0-最大電圧（ハードウェアのジャンパで3.3Vか5.0Vを設定
# ）を出力する。入力として設定したピンに対しては、ディジタル入力であればHigh/Low、
# アナログ入力であれば電圧値を読み込み、それに応じた値を対応するOutPortから出力す
# る。I2CやUARTについても、まずコンフィギュレーションからそれぞれを利用するか、利
# 用するならばそのパラメータを設定する。送信するデータや受信バイト数はInPortから入
# 力し、受信したデータはOutPortから出力される。
# Windows, Macの場合はhidapi, pyserialおよびAdafruit
# Blinkaのインストールが必要。Linuxの場合はこれらに加えlibusb、libudevのインストー
# ルが必要。
# 
# InPort
# ポート名/型/説明
# G*out/TimedLong/G*を出力ピンとしている場合のピンからの出力に対応した値。
# ディジタル出力の場合、Highとする場合は1を、Lowとする場合は0を入力する。
# アナログ出力の場合、0（0V）から65535（最大電圧、ハードウェアのジャンパで3.3Vか5
# .0Vを設定）の値で出力電圧を指定する。
# DAコンバータは1つのみのため、G2とG3をどちらもアナログ出力とした場合にはG2,
# G3からは同じ電圧が出力される。
# 入力ピンとして指定されている場合は何を入力しても影響はない。
# I2Cwcommand_rbytes/TimedOctetSeq/I2C通信で送信するデータ・受信するデータのバイト
# 数。
# 最終要素の前までが送信データ、最終要素が受信バイト数となる。例えば、1,2,3という
# データの場合は1,2という2バイトの値をデバイスに送信し、その後3バイトの情報をデバ
# イスから受信する。
# 受信バイト数が0の場合は送信だけを行い、受信を行わない（例: 1,2,0）。
# 受信バイト数のみが指定されている場合（要素が1つの場合）は送信を行わず受信だけを
# 行う（例: 3）。
# UARTwcommand_rbytes/TimedOctetSeq/UART通信で送信するデータ・受信するデータのバイ
# ト数。
# 最終要素の前までが送信データ、最終要素が受信バイト数となる。例えば、1,2,3という
# データの場合は1,2という2バイトの値をデバイスに送信し、その後3バイトの情報をデバ
# イスから受信する。
# 受信バイト数が0の場合は送信だけを行い、受信を行わない（例: 1,2,0）。
# 受信バイト数のみが指定されている場合（要素が1つの場合）は送信を行わず受信だけを
# 行う（例: 3）。
# 例外として、受信バイト数が255の場合には1行受信を行う。
# OutPort
# ポート名/型/説明
# G*in/TimedLong/G*を入力ピンとしている場合のピンへの入力に対応する値。
# ディジタル入力の場合、Highの場合は1が、Lowの場合は0が出力される。
# アナログ入力の場合、入力電圧に応じて0（0V）から65535（最大電圧、ハードウェアのジ
# ャンパで3.3Vか5.0Vを設定）の値が出力される。
# 出力ピンに指定されている場合は出力を行わない。
# I2Cread/TimedOctetSeq/I2C通信で受信したデータ。
# UARTread/TimedOctetSeq/UART通信で受信したデータ。
# 
# ライブラリのセットアップについて
# https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-mcp2221
# 
# 
# </rtc-template>
class Adafruit_MCP2221A_Breakout(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_G0out = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        G0をディジタル出力ピンとしている場合のピンからの出力に対応した値。
		Highとする場合は1を、Lowとする場合は0を入力する。
		入力ピンとして指定されている場合はどちらを入力しても影響はない。
	        - Type: RTC::TimedLong
         - Number: 1
        """
        self._G0outIn = OpenRTM_aist.InPort("G0out", self._d_G0out)
        self._d_G1out = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        G1をディジタル出力ピンとしている場合のピンからの出力に対応した値。
		Highとする場合は1を、Lowとする場合は0を入力する。
		入力ピンとして指定されている場合はどちらを入力しても影響はない。
	        - Type: RTC::TimedLong
         - Number: 1
        """
        self._G1outIn = OpenRTM_aist.InPort("G1out", self._d_G1out)
        self._d_G2out = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        G2を出力ピンとしている場合のピンからの出力に対応した値。
		ディジタル出力の場合、Highとする場合は1を、Lowとする場合は0を入力する。
		アナログ出力の場合、0（0V）から65535（最大電圧、ハードウェアのジャンパで3.3V
		か5.0Vを設定）の値で出力電圧を指定する。
		DAコンバータは1つのみのため、G2とG3をどちらもアナログ出力とした場合にはG3から
		も同じ電圧が出力される。
		入力ピンとして指定されている場合は何を入力しても影響はない。
	        - Type: RTC::TimedLong
         - Number: 1
        """
        self._G2outIn = OpenRTM_aist.InPort("G2out", self._d_G2out)
        self._d_G3out = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        G3を出力ピンとしている場合のピンからの出力に対応した値。
		ディジタル出力の場合、Highとする場合は1を、Lowとする場合は0を入力する。
		アナログ出力の場合、0（0V）から65535（最大電圧、ハードウェアのジャンパで3.3V
		か5.0Vを設定）の値で出力電圧を指定する。
		DAコンバータは1つのみのため、G2とG3をどちらもアナログ出力とした場合にはG3から
		も同じ電圧が出力される。
		入力ピンとして指定されている場合は何を入力しても影響はない。
	        - Type: RTC::TimedLong
         - Number: 1
        """
        self._G3outIn = OpenRTM_aist.InPort("G3out", self._d_G3out)
        self._d_I2Cwcommand_rbytes = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        I2C通信で送信するデータ・受信するデータのバイト数。
		最終要素の前までが送信データ、最終要素が受信バイト数となる。例えば、1,2,3とい
		うデータの場合は1,2という2バイトの値をデバイスに送信し、その後3バイトの情報を
		デバイスから受信する。
		受信バイト数が0の場合は送信だけを行い、受信を行わない（例: 1,2,0）。
		受信バイト数のみが指定されている場合（要素が1つの場合）は送信を行わず受信だけ
		を行う（例: 3）。
	        - Type: RTC::TimedOctetSeq
         - Number: データに依存。
        """
        self._I2Cwcommand_rbytesIn = OpenRTM_aist.InPort("I2Cwcommand_rbytes", self._d_I2Cwcommand_rbytes)
        self._d_UARTwcommand_rbytes = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        UART通信で送信するデータ・受信するデータのバイト数。
		最終要素の前までが送信データ、最終要素が受信バイト数となる。例えば、1,2,3とい
		うデータの場合は1,2という2バイトの値をデバイスに送信し、その後3バイトの情報を
		デバイスから受信する。
		受信バイト数が0の場合は送信だけを行い、受信を行わない（例: 1,2,0）。
		受信バイト数のみが指定されている場合（要素が1つの場合）は送信を行わず受信だけ
		を行う（例: 3）。
		例外として、受信バイト数が255の場合には1行受信を行う。
	        - Type: RTC::TimedOctetSeq
         - Number: データに依存。
        """
        self._UARTwcommand_rbytesIn = OpenRTM_aist.InPort("UARTwcommand_rbytes", self._d_UARTwcommand_rbytes)
        self._d_G0in = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        G0をディジタル入力ピンとしている場合のピンへの入力に対応する値。
		Highの場合は1が、Lowの場合は0が出力される。
		出力ピンに指定されている場合は出力を行わない。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._G0inOut = OpenRTM_aist.OutPort("G0in", self._d_G0in)
        self._d_G1in = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        G1を入力ピンとしている場合のピンへの入力に対応する値。
		ディジタル入力の場合、Highの場合は1が、Lowの場合は0が出力される。
		アナログ入力の場合、入力電圧に応じて0（0V）から65535（最大電圧、ハードウェア
		のジャンパで3.3Vか5.0Vを設定）の値が出力される。
		出力ピンに指定されている場合は出力を行わない。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._G1inOut = OpenRTM_aist.OutPort("G1in", self._d_G1in)
        self._d_G2in = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        G2を入力ピンとしている場合のピンへの入力に対応する値。
		ディジタル入力の場合、Highの場合は1が、Lowの場合は0が出力される。
		アナログ入力の場合、入力電圧に応じて0（0V）から65535（最大電圧、ハードウェア
		のジャンパで3.3Vか5.0Vを設定）の値が出力される。
		出力ピンに指定されている場合は出力を行わない。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._G2inOut = OpenRTM_aist.OutPort("G2in", self._d_G2in)
        self._d_G3in = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        G3を入力ピンとしている場合のピンへの入力に対応する値。
		ディジタル入力の場合、Highの場合は1が、Lowの場合は0が出力される。
		アナログ入力の場合、入力電圧に応じて0（0V）から65535（最大電圧、ハードウェア
		のジャンパで3.3Vか5.0Vを設定）の値が出力される。
		出力ピンに指定されている場合は出力を行わない。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._G3inOut = OpenRTM_aist.OutPort("G3in", self._d_G3in)
        self._d_I2Cread = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        I2C通信で受信したデータ。
         - Type: RTC::TimedOctetSeq
         - Number: データに依存。
        """
        self._I2CreadOut = OpenRTM_aist.OutPort("I2Cread", self._d_I2Cread)
        self._d_UARTread = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        UART通信で受信したデータ。
         - Type: RTC::TimedOctetSeq
         - Number: データに依存。
        """
        self._UARTreadOut = OpenRTM_aist.OutPort("UARTread", self._d_UARTread)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
        G0ピンの利用方法（ディジタル入力/ディジタル出力）を指定する。
		DIであればディジタル入力、DOであればディジタル出力になる。
		アクティブ状態での変更は無効（反映されない）。
         - Name: GPIO_G0_select GPIO_G0_select
         - DefaultValue: DI
         - Constraint: (DI,DO)
        """
        self._GPIO_G0_select = ['DI']
        """
        G1ピンの利用方法（ディジタル入力/ディジタル出力/アナログ入力）を指定する。
		DIであればディジタル入力、DOであればディジタル出力、AIであればアナログ入力に
		なる。
		アクティブ状態での変更は無効（反映されない）。
         - Name: GPIO_G1_select GPIO_G1_select
         - DefaultValue: DI
         - Constraint: (DI,DO,AI)
        """
        self._GPIO_G1_select = ['DI']
        """
        G2ピンの利用方法（ディジタル入力/ディジタル出力/アナログ入力/アナログ出力）を
		指定する。
		DIであればディジタル入力、DOであればディジタル出力、AIであればアナログ入力、
		AOであればアナログ出力になる。DAコンバータは1つのみのため、G2とG3をどちらもア
		ナログ出力とした場合にはG3からも同じ電圧が出力される。
		アクティブ状態での変更は無効（反映されない）。
         - Name: GPIO_G2_select GPIO_G2_select
         - DefaultValue: DI
         - Constraint: (DI,DO,AI,AO)
        """
        self._GPIO_G2_select = ['DI']
        """
        G3ピンの利用方法（ディジタル入力/ディジタル出力/アナログ入力/アナログ出力）を
		指定する。
		DIであればディジタル入力、DOであればディジタル出力、AIであればアナログ入力、
		AOであればアナログ出力になる。DAコンバータは1つのみのため、G2とG3をどちらもア
		ナログ出力とした場合にはG2からも同じ電圧が出力される。
		アクティブ状態での変更は無効（反映されない）。
         - Name: GPIO_G3_select GPIO_G3_select
         - DefaultValue: DI
         - Constraint: (DI,DO,AI,AO)
        """
        self._GPIO_G3_select = ['DI']
        """
        I2C通信を使用するか、使用しないかを選択する。1であれば使用し、0であれば使用し
		ない。
		アクティブ状態での変更は無効（反映されない）。
         - Name: I2C_use I2C_use
         - DefaultValue: 0
         - Constraint: (0,1)
        """
        self._I2C_use = [0]
        """
        I2Cデバイスの7ビットアドレス。0bや0xを値の前につけることで2進法や16進法で指定
		することも可能。
		I2Cを使用しない場合はこの設定は無視される。
		アクティブ状態での変更は無効（反映されない）。
         - Name: I2C_device_address I2C_device_address
         - DefaultValue: 0x08
         - Range: [0x08, 0x77]
        """
        self._I2C_device_address = ['0x08']
        """
        I2C通信においてバスをロックするときの最大待ち時間。この時間を超えてもバスがロ
		ックできない場合はエラーとする。
		I2Cを使用しない場合はこの設定は無視される。
         - Name: I2C_timeout I2C_timeout
         - DefaultValue: 1000
         - Unit: ms
         - Constraint: x>=0
        """
        self._I2C_timeout = [1000]
        """
        UART通信を使用するか、使用しないかを選択する。1であれば使用し、0であれば使用
		しない。
		アクティブ状態での変更は無効（反映されない）。
         - Name: UART_use UART_use
         - DefaultValue: 0
         - Constraint: (0,1)
        """
        self._UART_use = [0]
        """
        UART通信を行う際のポート。Windowsの場合はCOMx、Linuxの場合は/dev/ttACMx等。
		UARTを使用しない場合はこの設定は無視される。
		アクティブ状態での変更は無効（反映されない）。
         - Name: UART_port UART_port
         - DefaultValue: COM3
        """
        self._UART_port = ['COM3']
        """
        UART通信の通信速度。
		UARTを使用しない場合はこの設定は無視される。
		アクティブ状態での変更は無効（反映されない）。
         - Name: UART_baudrate UART_baudrate
         - DefaultValue: 115200
         - Unit: bps
         - Constraint: x>0
        """
        self._UART_baudrate = [115200]
        """
        UART通信における読み込みの最大待ち時間。
		この時間を超えても指定のバイト数が読み取れない場合はそれまでに読み込んだデー
		タを出力する。
		負の値を設定した場合は指定されたバイト数が読み込まれるまで待つ。
		UARTを使用しない場合はこの設定は無視される。
		アクティブ状態での変更は無効（反映されない）。
         - Name: UART_timeout UART_read_timeout
         - DefaultValue: 10.0
         - Unit: sec
        """
        self._UART_read_timeout = [10.0]
		
        # </rtc-template>


		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
        self.bindParameter("GPIO_G0_select", self._GPIO_G0_select, "DI")
        self.bindParameter("GPIO_G1_select", self._GPIO_G1_select, "DI")
        self.bindParameter("GPIO_G2_select", self._GPIO_G2_select, "DI")
        self.bindParameter("GPIO_G3_select", self._GPIO_G3_select, "DI")
        self.bindParameter("I2C_use", self._I2C_use, "0")
        self.bindParameter("I2C_device_address", self._I2C_device_address, "0x08")
        self.bindParameter("I2C_timeout", self._I2C_timeout, "1000")
        self.bindParameter("UART_use", self._UART_use, "0")
        self.bindParameter("UART_port", self._UART_port, "COM3")
        self.bindParameter("UART_baudrate", self._UART_baudrate, "115200")
        self.bindParameter("UART_read_timeout", self._UART_read_timeout, "10.0")
		
        # Set InPort buffers
        self.addInPort("G0out",self._G0outIn)
        self.addInPort("G1out",self._G1outIn)
        self.addInPort("G2out",self._G2outIn)
        self.addInPort("G3out",self._G3outIn)
        self.addInPort("I2Cwcommand_rbytes",self._I2Cwcommand_rbytesIn)
        self.addInPort("UARTwcommand_rbytes",self._UARTwcommand_rbytesIn)
		
        # Set OutPort buffers
        self.addOutPort("G0in",self._G0inOut)
        self.addOutPort("G1in",self._G1inOut)
        self.addOutPort("G2in",self._G2inOut)
        self.addOutPort("G3in",self._G3inOut)
        self.addOutPort("I2Cread",self._I2CreadOut)
        self.addOutPort("UARTread",self._UARTreadOut)
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports

        #GPIO port settings
        self.GPIOSelect = [GPIOtype.DI] * 4

        #Serial port setting flags
        #for I2C communication
        self.i2c_set = False
        self.i2c_locked = False

        #for UART communication
        self.uart = serial.Serial()
		
        return RTC.RTC_OK
	
    ###
    ## 
    ## The finalize action (on ALIVE->END transition)
    ## 
    ## @return RTC::ReturnCode_t
    #
    ## 
    #def onFinalize(self):
    #

    #    return RTC.RTC_OK
	
    ###
    ##
    ## The startup action when ExecutionContext startup
    ## 
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ##
    # コンフィギュレーション変数を読み込み、GPIOの各ピンのアナログ/ディジタル、入力
	# /は出力を設定する。また、I2CおよびUART通信の設定を行う。
    #
    # The activated action (Active state entry action)
    #
    # @param ec_id target ExecutionContext Id
    # 
    # @return RTC::ReturnCode_t
    #
    #
    def onActivated(self, ec_id):
        #Set the I2C device
        # *** must be done before calling setGPIOPorts() since this resets the GPIO port direction settings ***
        if self._I2C_use[0] == 1:
            res = self.connectI2CDevice()
            if res < 0:
                return RTC.RTC_ERROR

        #Set the UART device
        if self._UART_use[0] == 1:
            res = self.openUARTPort()
            if res < 0:
                return RTC.RTC_ERROR

        #GPIO port settings
        res = self.setGPIOPorts()
        if res < 0:
            return RTC.RTC_ERROR

        return RTC.RTC_OK
	
    ###
    ##
    ## Set GPIO port (Analog or Digital, Input or Output) depending on the configuration values.
    ##  G0: digital IO
    ##  G1: digital IO, analog In
    ##  G2: digital IO, analog IO
    ##  G3: digital IO, analog IO
    ##
    ## @return 0 if no error, <0 if error
    ##
    ##
    def setGPIOPorts(self):
        #G0
        self.g0 = digitalio.DigitalInOut(board.G0)
        if self._GPIO_G0_select[0] == 'DO': #DigitalOut
            self.g0.direction = digitalio.Direction.OUTPUT
            self.GPIOSelect[0] = GPIOtype.DO
        else: #DigitalIn (as default)
            self.g0.direction = digitalio.Direction.INPUT
            self.GPIOSelect[0] = GPIOtype.DI

        #G1
        if self._GPIO_G1_select[0] == 'AI': #AnalogIn
            self.g1 = analogio.AnalogIn(board.G1)
            self.GPIOSelect[1] = GPIOtype.AI
        else:
            self.g1 = digitalio.DigitalInOut(board.G1)
            if self._GPIO_G1_select[0] == 'DO': #DigitalOut
                self.g1.direction = digitalio.Direction.OUTPUT
                self.GPIOSelect[1] = GPIOtype.DO
            else: #DigitalIn (as default)
                self.g1.direction = digitalio.Direction.INPUT
                self.GPIOSelect[1] = GPIOtype.DI

        #G2
        if self._GPIO_G2_select[0] == 'AO': #AnalogOut
            self.g2 = analogio.AnalogOut(board.G2)
            self.GPIOSelect[2] = GPIOtype.AO
        elif self._GPIO_G2_select[0] == 'AI': #AnalogIn
            self.g2 = analogio.AnalogIn(board.G2)
            self.GPIOSelect[2] = GPIOtype.AI
        else:
            self.g2 = digitalio.DigitalInOut(board.G2)
            if self._GPIO_G2_select[0] == 'DO': #DigitalOut
                self.g2.direction = digitalio.Direction.OUTPUT
                self.GPIOSelect[2] = GPIOtype.DO
            else: #DigitalIn (as default)
                self.g2.direction = digitalio.Direction.INPUT
                self.GPIOSelect[2] = GPIOtype.DI

        #G3
        if self._GPIO_G3_select[0] == 'AO': #AnalogOut
            self.g3 = analogio.AnalogOut(board.G3)
            self.GPIOSelect[3] = GPIOtype.AO
        elif self._GPIO_G3_select[0] == 'AI': #AnalogIn
            self.g3 = analogio.AnalogIn(board.G3)
            self.GPIOSelect[3] = GPIOtype.AI
        else:
            self.g3 = digitalio.DigitalInOut(board.G3)
            if self._GPIO_G3_select[0] == 'DO': #DigitalOut
                self.g3.direction = digitalio.Direction.OUTPUT
                self.GPIOSelect[3] = GPIOtype.DO
            else: #DigitalIn (as default)
                self.g3.direction = digitalio.Direction.INPUT
                self.GPIOSelect[3] = GPIOtype.DI

        return 0

    ###
    ##
    ## Connect to I2C device depending on the configuration values.
    ##
    ## @return 0 if no error, <0 if error
    ##
    ##
    def connectI2CDevice(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.i2c_set = True

        t1 = time.perf_counter_ns()
        #for I2C communication
        #Lock the bus
        while not self.i2c.try_lock():
            if (time.perf_counter_ns() - t1)/1000 >= self._I2C_timeout[0]:
                printf('Error in I2C connection: cannot lock the bus')
                return -2
        self.i2c_locked = True

        #Check the device address
        try:
            self.I2C_address = int(self._I2C_device_address[0], 0)  #try to convert to integer
        except ValueError:
            print('Invalid configuration value (I2C_device_address): value not integer')
            return -1
        else:
            deviceIDs = self.i2c.scan() #i2c.scan() returns 7-bit I2C device addresses
            print('The detected I2C device IDs are', deviceIDs)
            if self.I2C_address not in deviceIDs: 
                print('Invalid configuration value (I2C_device_address): address not found')
                print('Check the input address, wiring, power, and if pull-up resistors are necessary')
                return -1
            else:
                print(f'I2C device connected: address {self.I2C_address}')
        return 0

    ###
    ##
    ## Open UART port depending on the configuration values.
    ##
    ## @return 0 if no error, <0 if error
    ##
    ##
    def openUARTPort(self):
        #Check the port name
        devices = [info.device for info in list_ports.comports()]
        print('The detected serial ports are', devices)

        try:
            self.uart.port = self._UART_port[0]
            self.uart.baudrate = self._UART_baudrate[0]
            self.uart.timeout = self._UART_read_timeout[0] if self._UART_read_timeout[0]>=0 else None
            self.uart.open()
        except ValueError:
            print('Invalid configuration value (UART_baudrate or UART_timeout): out of range')
            return -1
        except SerialException:
            print(f'Cannot open serial port for UART communication ({self._UART_port[0]})')
            print('Check if the correct port name is specified')
            return -2
        else:
            print(f'UART opened: port name {self._UART_port[0]}')
        return 0

    ##
    # GPIOの全ての出力ピンにLowもしくは0Vを出力する。I2CおよびUART通信を終了する。
    #
    # The deactivated action (Active state exit action)
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onDeactivated(self, ec_id):
        self.finalizeDevice()
    
        return RTC.RTC_OK
	
    ###
    ##
    ## Finalize the device.
    ##  Output low from all GPIO ports, unlock the serial communication bus, and unset the device 
    ##
    ##
    def finalizeDevice(self):
        #Output low or 0 to output pins
        if self.GPIOSelect[0] == GPIOtype.DO:
          self.g0.value = False
          print('G0->0')

        if self.GPIOSelect[1] == GPIOtype.DO:
          self.g1.value = False
          print('G1->0')

        if self.GPIOSelect[2] == GPIOtype.DO:
          self.g2.value = False
          print('G2->0')
        elif self.GPIOSelect[2] == GPIOtype.AO:
          self.g2.value = 0
          print('G2->0')

        if self.GPIOSelect[3] == GPIOtype.DO:
          self.g3.value = False
          print('G3->0')
        elif self.GPIOSelect[3] == GPIOtype.AO:
          self.g3.value = 0
          print('G3->0')

        self.g0.deinit()
        self.g1.deinit()
        self.g2.deinit()
        self.g3.deinit()

        #Unlock the bus
        #for I2C communication
        if self.i2c_locked:
            self.i2c.unlock()
            self.i2c_locked = False

        #Unset the device
        #for I2C communication
        if self.i2c_set:
            self.i2c.deinit()
            self.i2c_set = False
        #for UART communication
        if self.uart.is_open:
            self.uart.close()

        return

    ##
    # InPortから値を読み込み、GPIOの各出力ピンから値に対応してHigh/Lowやアナログ電
	# 圧を出力する。
	# GPIOの各入力ピンからHighまたはLowを読み込みOutPortから対応する値を出力する。
	# I2CもしくはUART通信が設定されている場合は、InPortから読み込んだ値に応じてデバ
	# イスへの書き込みやデバイスからの読み込みを行い、OutPortからの出力を行う。
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onExecute(self, ec_id):
        #--- GPIO ------------------------------------------
        #Output data to PortG
        if self._G0outIn.isNew():
            self._d_G0out = self._G0outIn.read()
            if self.GPIOSelect[0] == GPIOtype.DO: #if digital output
                self.g0.value = True if self._d_G0out.data else False
                print(f'G0->{self._d_G0out.data}')

        if self._G1outIn.isNew():
            self._d_G1out = self._G1outIn.read()
            if self.GPIOSelect[1] == GPIOtype.DO: #if digital output
                self.g1.value = True if self._d_G1out.data else False
                print(f'G1->{self._d_G1out.data}')

        if self._G2outIn.isNew():
            self._d_G2out = self._G2outIn.read()
            if self.GPIOSelect[2] == GPIOtype.DO: #if digital output
                self.g2.value = True if self._d_G2out.data else False
                print(f'G2->{self._d_G2out.data}')
            elif self.GPIOSelect[2] == GPIOtype.AO: #if analog output
                self.g2.value = self._d_G2out.data
                print(f'G2->{self._d_G2out.data}')

        if self._G3outIn.isNew():
            self._d_G3out = self._G3outIn.read()
            if self.GPIOSelect[3] == GPIOtype.DO: #if digital output
                self.g3.value = True if self._d_G3out.data else False
                print(f'G3->{self._d_G3out.data}')
            elif self.GPIOSelect[3] == GPIOtype.AO: #if analog output
                self.g3.value = self._d_G3out.data
                print(f'G3->{self._d_G3out.data}')

        #Input data from PortG
        if self.GPIOSelect[0] == GPIOtype.DI: # if digital input
            self._d_G0in.data = 1 if self.g0.value else 0
            self._G0inOut.write()

        if self.GPIOSelect[1] == GPIOtype.DI: # if digital input
            self._d_G1in.data = 1 if self.g1.value else 0
            self._G1inOut.write()
        elif self.GPIOSelect[1] == GPIOtype.AI: # if analog input
            self._d_G1in.data = self.g1.value
            self._G1inOut.write()

        if self.GPIOSelect[2] == GPIOtype.DI: # if digital input
            self._d_G2in.data = 1 if self.g2.value else 0
            self._G2inOut.write()
        elif self.GPIOSelect[2] == GPIOtype.AI: # if analog input
            self._d_G2in.data = self.g2.value
            self._G2inOut.write()

        if self.GPIOSelect[3] == GPIOtype.DI: # if digital input
            self._d_G3in.data = 1 if self.g3.value else 0
            self._G3inOut.write()
        elif self.GPIOSelect[3] == GPIOtype.AI: # if analog input
            self._d_G3in.data = self.g3.value
            self._G3inOut.write()
        #--- end GPIO --------------------------------------

        #--- Serial ----------------------------------------
        #--- I2C from InPort ----------------------------
        if self._I2Cwcommand_rbytesIn.isNew():
            self._d_I2Cwcommand_rbytes = self._I2Cwcommand_rbytesIn.read()
            if len(self._d_I2Cwcommand_rbytes.data) > 0 : #not empty
                readbytes = self._d_I2Cwcommand_rbytes.data[-1]
                msg = bytes(self._d_I2Cwcommand_rbytes.data[:-1])

                res = self.I2CCommunication(msg, readbytes)
                if len(res) > 0:
                    self._d_I2Cread.data = bytes(res)
                    print(f'I2C data = {self._d_I2Cread.data}')
                    self._I2CreadOut.write()

        #--- UART from InPort ----------------------------
        if self._UARTwcommand_rbytesIn.isNew():
            self._d_UARTwcommand_rbytes = self._UARTwcommand_rbytesIn.read()
            if len(self._d_UARTwcommand_rbytes.data) > 0 : #not empty
                readbytes = self._d_UARTwcommand_rbytes.data[-1]
                msg = bytes(self._d_UARTwcommand_rbytes.data[:-1])

                res = self.UARTCommunication(msg, readbytes)
                if len(res) > 0:
                    self._d_UARTread.data = bytes(res)
                    print(f'UART data = {self._d_UARTread.data}')
                    self._UARTreadOut.write()

        #--- end Serial ------------------------------------
    
        return RTC.RTC_OK
	
    ###
    ##
    ## Communicate with the I2C device depending on the arguments.
    ## Send only if msg is not empty and readbytes = 0
    ## Receive only if msg is empty and readbytes > 0
    ## Send and receive if msg is not empty and readbytes > 0
    ## Neither send nor receive otherwise 
    ##
    ## @param msg message sent to the device
    ## @param readbytes number of bytes of the message recieved from the device
    ##
    ## @return bytearray of the received message. if readbytes<=0 or i2c device not connected then empty bytearray is returned
    ##
    ##
    def I2CCommunication(self, msg, readbytes):
        if (readbytes < 0) or (not self.i2c_locked):
            return bytearray()

        result = bytearray(readbytes)
        if len(msg) > 0:
            if readbytes == 0: #write only
                self.i2c.writeto(self.I2C_address, msg)
            else: #write and read
                self.i2c.writeto_then_readfrom(self.I2C_address, msg, result)
        else: #read only
            if readbytes > 0:
                self.i2c.readfrom_into(self.I2C_address, result) #the read data is stored in result

        return result

    ###
    ##
    ## Communicate with the UART device depending on the arguments.
    ## Send message (if msg is not empty) and then receive message (if readbytes != 0)
    ##
    ## @param msg message sent
    ## @param readbytes number of bytes of the message read if 0 < readbytes < 255, read one line if readbytes = 255 
    ##
    ## @return bytearray of the received message. if readbytes=0 or serial port is not opened then empty bytearray is returned
    ##
    ##
    def UARTCommunication(self, msg, readbytes):
        if not self.uart.is_open:
            return bytearray()

        #write message
        if len(msg) > 0:
            self.uart.write(msg)

        #read message
        if readbytes == 255: #read one line
            result = self.uart.readline()
        elif readbytes > 0: #read specified number of bytes
            result = self.uart.read(readbytes)
        else: #no need to read
            return bytearray()

        return result

    ##
    # GPIOの全ての出力ピンにLowもしくは0Vを出力する。I2CおよびUART通信を終了する。
    #
    # The aborting action when main logic error occurred.
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onAborting(self, ec_id):
        self.finalizeDevice()
    
        return RTC.RTC_OK
	
    ###
    ##
    ## The error action in ERROR state
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onError(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The reset action that is invoked resetting
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The state update action that is invoked after onExecute() action
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##

    ##
    #def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The action that is invoked when execution context's rate is changed
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK
	



def Adafruit_MCP2221A_BreakoutInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=adafruit_mcp2221a_breakout_spec)
    manager.registerFactory(profile,
                            Adafruit_MCP2221A_Breakout,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    Adafruit_MCP2221A_BreakoutInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("Adafruit_MCP2221A_Breakout" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

