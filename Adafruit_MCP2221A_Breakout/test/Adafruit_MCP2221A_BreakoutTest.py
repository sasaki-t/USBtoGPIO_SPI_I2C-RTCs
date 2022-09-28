#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file Adafruit_MCP2221A_BreakoutTest.py
 @brief USB to Digital/Analog IO and I2C, UART components using Adafruit MCP2221A Breakout
 @date $Date$

 @author 佐々木毅 (Takeshi SASAKI) <sasaki-t(_at_)ieee.org>

"""
# </rtc-template>

from __future__ import print_function
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

import Adafruit_MCP2221A_Breakout

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
adafruit_mcp2221a_breakouttest_spec = ["implementation_id", "Adafruit_MCP2221A_BreakoutTest", 
         "type_name",         "Adafruit_MCP2221A_BreakoutTest", 
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
# @class Adafruit_MCP2221A_BreakoutTest
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
class Adafruit_MCP2221A_BreakoutTest(OpenRTM_aist.DataFlowComponentBase):
    
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_G0in = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        G0をディジタル入力ピンとしている場合のピンへの入力に対応する値。
		Highの場合は1が、Lowの場合は0が出力される。
		出力ピンに指定されている場合は出力を行わない。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._G0inIn = OpenRTM_aist.InPort("G0in", self._d_G0in)
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
        self._G1inIn = OpenRTM_aist.InPort("G1in", self._d_G1in)
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
        self._G2inIn = OpenRTM_aist.InPort("G2in", self._d_G2in)
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
        self._G3inIn = OpenRTM_aist.InPort("G3in", self._d_G3in)
        self._d_I2Cread = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        I2C通信で受信したデータ。
         - Type: RTC::TimedOctetSeq
         - Number: データに依存。
        """
        self._I2CreadIn = OpenRTM_aist.InPort("I2Cread", self._d_I2Cread)
        self._d_UARTread = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        UART通信で受信したデータ。
         - Type: RTC::TimedOctetSeq
         - Number: データに依存。
        """
        self._UARTreadIn = OpenRTM_aist.InPort("UARTread", self._d_UARTread)
        self._d_G0out = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        G0をディジタル出力ピンとしている場合のピンからの出力に対応した値。
		Highとする場合は1を、Lowとする場合は0を入力する。
		入力ピンとして指定されている場合はどちらを入力しても影響はない。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._G0outOut = OpenRTM_aist.OutPort("G0out", self._d_G0out)
        self._d_G1out = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        G1をディジタル出力ピンとしている場合のピンからの出力に対応した値。
		Highとする場合は1を、Lowとする場合は0を入力する。
		入力ピンとして指定されている場合はどちらを入力しても影響はない。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._G1outOut = OpenRTM_aist.OutPort("G1out", self._d_G1out)
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
        self._G2outOut = OpenRTM_aist.OutPort("G2out", self._d_G2out)
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
        self._G3outOut = OpenRTM_aist.OutPort("G3out", self._d_G3out)
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
        self._I2Cwcommand_rbytesOut = OpenRTM_aist.OutPort("I2Cwcommand_rbytes", self._d_I2Cwcommand_rbytes)
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
        self._UARTwcommand_rbytesOut = OpenRTM_aist.OutPort("UARTwcommand_rbytes", self._d_UARTwcommand_rbytes)


        


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
        self.addInPort("G0in",self._G0inIn)
        self.addInPort("G1in",self._G1inIn)
        self.addInPort("G2in",self._G2inIn)
        self.addInPort("G3in",self._G3inIn)
        self.addInPort("I2Cread",self._I2CreadIn)
        self.addInPort("UARTread",self._UARTreadIn)
        
        # Set OutPort buffers
        self.addOutPort("G0out",self._G0outOut)
        self.addOutPort("G1out",self._G1outOut)
        self.addOutPort("G2out",self._G2outOut)
        self.addOutPort("G3out",self._G3outOut)
        self.addOutPort("I2Cwcommand_rbytes",self._I2Cwcommand_rbytesOut)
        self.addOutPort("UARTwcommand_rbytes",self._UARTwcommand_rbytesOut)
        
        # Set service provider to Ports
        
        # Set service consumers to Ports
        
        # Set CORBA Service Ports
        
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
    
    #    ##
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
    
        return RTC.RTC_OK
    
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
    
        return RTC.RTC_OK
    
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
    
        return RTC.RTC_OK
    
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
    
    def runTest(self):
        return True

def RunTest():
    manager = OpenRTM_aist.Manager.instance()
    comp = manager.getComponent("Adafruit_MCP2221A_BreakoutTest0")
    if comp is None:
        print('Component get failed.', file=sys.stderr)
        return False
    return comp.runTest()

def Adafruit_MCP2221A_BreakoutTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=adafruit_mcp2221a_breakouttest_spec)
    manager.registerFactory(profile,
                            Adafruit_MCP2221A_BreakoutTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    Adafruit_MCP2221A_BreakoutTestInit(manager)
    Adafruit_MCP2221A_Breakout.Adafruit_MCP2221A_BreakoutInit(manager)

    # Create a component
    comp = manager.createComponent("Adafruit_MCP2221A_BreakoutTest")

def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager(True)

    ret = RunTest()
    mgr.shutdown()

    if ret:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()

