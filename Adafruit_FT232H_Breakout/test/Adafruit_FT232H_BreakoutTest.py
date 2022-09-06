#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file Adafruit_FT232H_BreakoutTest.py
 @brief USB to Digital IO and I2C/SPI components using Adafruit FT232H Breakout
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

import Adafruit_FT232H_Breakout

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
adafruit_ft232h_breakouttest_spec = ["implementation_id", "Adafruit_FT232H_BreakoutTest", 
         "type_name",         "Adafruit_FT232H_BreakoutTest", 
         "description",       "USB to Digital IO and I2C/SPI components using Adafruit FT232H Breakout", 
         "version",           "1.0.0", 
         "vendor",            "TakeshiSasaki", 
         "category",          "GPIO", 
         "activity_type",     "COMMUTATIVE", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.GPIO_C7_0_IO_select", "0b11111111",
         "conf.default.GPIO_D7_4_IO_select", "0b1111",
         "conf.default.SPI_baudrate", "100000",
         "conf.default.SPI_mode", "0",
         "conf.default.SPI_cs_pin", "D4",
         "conf.default.SPI_cs_talking", "0",
         "conf.default.I2C_device_address", "0x08",
         "conf.default.SER_select", "None",
         "conf.default.SER_timeout", "1000",

         "conf.__widget__.GPIO_C7_0_IO_select", "text",
         "conf.__widget__.GPIO_D7_4_IO_select", "text",
         "conf.__widget__.SPI_baudrate", "text",
         "conf.__widget__.SPI_mode", "radio",
         "conf.__widget__.SPI_cs_pin", "radio",
         "conf.__widget__.SPI_cs_talking", "radio",
         "conf.__widget__.I2C_device_address", "text",
         "conf.__widget__.SER_select", "radio",
         "conf.__widget__.SER_timeout", "text",
         "conf.__constraints__.SPI_baudrate", "x>0",
         "conf.__constraints__.SPI_mode", "(0,1,2,3)",
         "conf.__constraints__.SPI_cs_pin", "(D4,D5,D6,D7)",
         "conf.__constraints__.SPI_cs_talking", "(0,1)",
         "conf.__constraints__.SER_select", "(None,I2C,SPI)",
         "conf.__constraints__.SER_timeout", "x>=0",

         "conf.__type__.GPIO_C7_0_IO_select", "string",
         "conf.__type__.GPIO_D7_4_IO_select", "string",
         "conf.__type__.SPI_baudrate", "int",
         "conf.__type__.SPI_mode", "int",
         "conf.__type__.SPI_cs_pin", "string",
         "conf.__type__.SPI_cs_talking", "int",
         "conf.__type__.I2C_device_address", "string",
         "conf.__type__.SER_select", "string",
         "conf.__type__.SER_timeout", "int",

         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class Adafruit_FT232H_BreakoutTest
# @brief USB to Digital IO and I2C/SPI components using Adafruit FT232H Breakout
# 
# Adafruit FT232H Breakoutを使用したUSB-GPIO, SPI,
# I2C変換コンポーネント。GPIOに関しては、まずコンフィギュレーションから各ピンをデ
# ィジタル入力として使うか、ディジタル出力として使うかを選択する。出力として設定し
# たピンに対しては、対応するInPortに値が入力されると、その値に応じてHighまたはLow
# を出力する。入力として設定したピンに対しては、HighまたはLowを読み込み、それに応
# じた値を対応するOutPortから出力する。I2C/SPIについても、まずコンフィギュレーショ
# ンからいずれかを利用するか、利用するならばそのパラメータを設定する。送信するデー
# タや受信バイト数はInPortから入力し、受信したデータはOutPortから出力される。
# pyusb（Mac, Linuxの場合はlibusb）, pyftdiおよびAdafruit
# Blinkaのインストールが必要。
# 
# InPort
# ポート名/型/説明
# C7_0out/TimedLong/C7~C0のうち、出力ピンとしているピンからの出力に対応した値。
# C7から順に、Highとする場合は1、Lowとする場合は0とした8ビットの値を入力する。
# 入力ピンとして指定されているピンに対してはどちらを入力しても影響はない。
# 例えば、C7, C5, C4をHigh、他をLowとする場合には10110000、つまり176を入力する。
# D*out/TimedLong/D*を出力ピンとしている場合のピンからの出力に対応した値。
# Highとする場合は1を、Lowとする場合は0を入力する。
# 入力ピンとして指定されている場合はどちらを入力しても影響はない。
# I2C_SPIwcommand_rbytes/TimedOctetSeq/I2CもしくはSPI通信で送信するデータ・受信す
# るデータのバイト数。最終要素の前までが送信データ、最終要素が受信バイト数となる。
# 例えば、1,2,3というデータの場合は1,2という2バイトの値をデバイスに送信し、その後
# 3バイトの情報をデバイスから受信する。受信バイト数が0の場合は送信だけを行い、受信
# を行わない（例:
# 1,2,0）。受信バイト数のみが指定されている場合（要素が1つの場合）は送信を行わず受
# 信だけを行う（例: 3）。
# OutPort
# ポート名/型/説明
# C7_0in/TimedLong/C7~C0のうち、入力ピンとしているピンへの入力に対応する値。
# C7から順に、Highの場合は1、Lowもしくは出力ピンとして指定している場合は0とした8ビ
# ットの値が出力される。
# 例えば、C7, C5,
# C4がHigh、他がLowもしくは出力ピンである場合には10110000、つまり176が出力される。
# 全てのピンが出力ピンに指定されている場合は出力を行わない。
# D*in/TimedLong/D*を入力ピンとしている場合のピンへの入力に対応する値。
# Highの場合は1が、Lowの場合は0が出力される。
# 出力ピンに指定されている場合は出力を行わない。
# I2C_SPIread/TimedOctetSeq/I2CもしくはSPI通信で受信したデータ。
# 
# ライブラリのセットアップについて
# https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h
# 
# 
# </rtc-template>
class Adafruit_FT232H_BreakoutTest(OpenRTM_aist.DataFlowComponentBase):
    
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_C7_0in = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        C7~C0のうち、入力ピンとしているピンへの入力に対応する値。
		C7から順に、Highの場合は1、Lowもしくは出力ピンとして指定している場合は0とした
		8ビットの値が出力される。
		例えば、C7, C5,
		C4がHigh、他がLowもしくは出力ピンである場合には10110000、つまり176が出力され
		る。
		全てのピンが出力ピンに指定されている場合は出力を行わない。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._C7_0inIn = OpenRTM_aist.InPort("C7_0in", self._d_C7_0in)
        self._d_D4in = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        D4を入力ピンとしている場合のピンへの入力に対応する値。
		Highの場合は1が、Lowの場合は0が出力される。
		出力ピンに指定されている場合は出力を行わない。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._D4inIn = OpenRTM_aist.InPort("D4in", self._d_D4in)
        self._d_D5in = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        D5を入力ピンとしている場合のピンへの入力に対応する値。
		Highの場合は1が、Lowの場合は0が出力される。
		出力ピンに指定されている場合は出力を行わない。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._D5inIn = OpenRTM_aist.InPort("D5in", self._d_D5in)
        self._d_D6in = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        D6を入力ピンとしている場合のピンへの入力に対応する値。
		Highの場合は1が、Lowの場合は0が出力される。
		出力ピンに指定されている場合は出力を行わない。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._D6inIn = OpenRTM_aist.InPort("D6in", self._d_D6in)
        self._d_D7in = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        D7を入力ピンとしている場合のピンへの入力に対応する値。
		Highの場合は1が、Lowの場合は0が出力される。
		出力ピンに指定されている場合は出力を行わない。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._D7inIn = OpenRTM_aist.InPort("D7in", self._d_D7in)
        self._d_I2C_SPIread = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        I2CもしくはSPI通信で受信したデータ。
         - Type: RTC::TimedOctetSeq
         - Number: データに依存。
        """
        self._I2C_SPIreadIn = OpenRTM_aist.InPort("I2C_SPIread", self._d_I2C_SPIread)
        self._d_C7_0out = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        C7~C0のうち、出力ピンとしているピンからの出力に対応した値。
		C7から順に、Highとする場合は1、Lowとする場合は0とした8ビットの値を入力する。
		入力ピンとして指定されているピンに対してはどちらを入力しても影響はない。
		例えば、C7, C5,
		C4をHigh、他をLowとする場合には10110000、つまり176を入力する。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._C7_0outOut = OpenRTM_aist.OutPort("C7_0out", self._d_C7_0out)
        self._d_D4out = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        D4を出力ピンとしている場合のピンからの出力に対応した値。
		Highとする場合は1を、Lowとする場合は0を入力する。
		入力ピンとして指定されている場合はどちらを入力しても影響はない。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._D4outOut = OpenRTM_aist.OutPort("D4out", self._d_D4out)
        self._d_D5out = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        D5を出力ピンとしている場合のピンからの出力に対応した値。
		Highとする場合は1を、Lowとする場合は0を入力する。
		入力ピンとして指定されている場合はどちらを入力しても影響はない。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._D5outOut = OpenRTM_aist.OutPort("D5out", self._d_D5out)
        self._d_D6out = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        D6を出力ピンとしている場合のピンからの出力に対応した値。
		Highとする場合は1を、Lowとする場合は0を入力する。
		入力ピンとして指定されている場合はどちらを入力しても影響はない。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._D6outOut = OpenRTM_aist.OutPort("D6out", self._d_D6out)
        self._d_D7out = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        D7を出力ピンとしている場合のピンからの出力に対応した値。
		Highとする場合は1を、Lowとする場合は0を入力する。
		入力ピンとして指定されている場合はどちらを入力しても影響はない。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._D7outOut = OpenRTM_aist.OutPort("D7out", self._d_D7out)
        self._d_I2C_SPIwcommand_rbytes = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        I2CもしくはSPI通信で送信するデータ・受信するデータのバイト数。
		最終要素の前までが送信データ、最終要素が受信バイト数となる。例えば、1,2,3とい
		うデータの場合は1,2という2バイトの値をデバイスに送信し、その後3バイトの情報を
		デバイスから受信する。
		受信バイト数が0の場合は送信だけを行い、受信を行わない（例: 1,2,0）。
		受信バイト数のみが指定されている場合（要素が1つの場合）は送信を行わず受信だけ
		を行う（例: 3）。
         - Type: RTC::TimedOctetSeq
         - Number: データに依存。
        """
        self._I2C_SPIwcommand_rbytesOut = OpenRTM_aist.OutPort("I2C_SPIwcommand_rbytes", self._d_I2C_SPIwcommand_rbytes)


        


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
        C7~C0をそれぞれディジタル入力ピンとして使用するか、ディジタル出力ピンとして使
		用するかを指定する。
		C7から順に入力ピンとして指定する場所は1、出力ピンとして使用するところは0とし
		、それを2進法で表現された数とみなして整数値を入力する。0bや0xを値の前につける
		ことで2進法や16進法で指定することも可能。
		例えば、C7,C5,C4を出力ピン、他を入力ピンとする場合は01001111となるため、その
		まま2進法で0b01001111としても良いし、16進法に直して0x4f、10進法に直して79とし
		ても良い。
		アクティブ状態での変更は無効（反映されない）。
         - Name: GPIO_C7_0_IO_select GPIO_C7_0_IO_select
         - DefaultValue: 0b11111111
        """
        self._GPIO_C7_0_IO_select = ['0b11111111']
        """
        D7~D4をそれぞれディジタル入力ピンとして使用するか、ディジタル出力ピンとして使
		用するかを指定する。
		D7から順に入力ピンとして指定する場所は1、出力ピンとして使用するところは0とし
		、それを2進法で表現された数とみなして整数値を入力する。0bや0xを値の前につける
		ことで2進法や16進法で指定することも可能。
		例えば、D7,D5,D4を出力ピン、他を入力ピンとする場合は0100となるため、そのまま
		2進法で0b0100としても良いし、16進法に直して0x4、10進法に直して4としても良い。
		アクティブ状態での変更は無効（反映されない）。
         - Name: GPIO_D7_4_IO_select GPIO_D7_4_IO_select
         - DefaultValue: 0b1111
        """
        self._GPIO_D7_4_IO_select = ['0b1111']
        """
        SPI通信のクロックレート。
		アクティブ状態での変更は無効（反映されない）。
         - Name: SPI_baudrate SPI_baudrate
         - DefaultValue: 100000
         - Unit: Hz
         - Constraint: x>0
        """
        self._SPI_baudrate = [100000]
        """
        SPI通信のクロックの極性(polarity)と位相(phase)を決定する番号。0の時はいずれも
		0、1の時は極性が0で位相が1、2の時は極性が1で位相が0、3の時はいずれも1となる。
		SPIを使用しない場合はこの設定は無視される。
		アクティブ状態での変更は無効（反映されない）。
         - Name: SPI_mode SPI_mode
         - DefaultValue: 0
         - Constraint: (0,1,2,3)
        """
        self._SPI_mode = [0]
        """
        SPI通信でCS(chip
		select)ピンとして利用するピン（BlinkaではCS0(D3)ピンを使用しないため、GPIOの
		1つをCSピンとして使用する必要がある）。D4～D7の中から1つを選択する。CSピンと
		して使用されるピンはGPIOの設定(GPIO_D7_4_IO_select)で出力ピンとする必要がある
		。また、CSピンとして指定したピンに対する入力ポートからの値の変更は無視される
		。
		SPIを使用しない場合はこの設定は無視される。
		アクティブ状態での変更は無効（反映されない）。
         - Name: SPI_cs_pin SPI_cs_pin
         - DefaultValue: D4
         - Constraint: (D4,D5,D6,D7)
        """
        self._SPI_cs_pin = ['D4']
        """
        SPI通信での通信時のCS(chip
		select)ピンの状態。通信時にLowとする場合は0、Highとする場合には1となる。
		SPIを使用しない場合はこの設定は無視される。
		アクティブ状態での変更は無効（反映されない）。
         - Name: SPI_cs_talking SPI_cs_talking
         - DefaultValue: 0
         - Constraint: (0,1)
        """
        self._SPI_cs_talking = [0]
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
        I2CもしくはSPI通信を使用するか、使用しないかを選択する。I2CかSPIであればそれ
		ぞれの通信を使用し、Noneであれば使用しない。
		アクティブ状態での変更は無効（反映されない）。
         - Name: SER_select SER_select
         - DefaultValue: None
         - Constraint: (None,I2C,SPI)
        """
        self._SER_select = ['None']
        """
        I2CもしくはSPI通信においてバスをロックするときの最大待ち時間。この時間を超え
		てもバスがロックできない場合はエラーとする。
		SPIやI2Cを使用しない場合はこの設定は無視される。
         - Name: SER_timeout SER_timeout
         - DefaultValue: 1000
         - Unit: ms
         - Constraint: x>=0
        """
        self._SER_timeout = [1000]
        
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
        self.bindParameter("GPIO_C7_0_IO_select", self._GPIO_C7_0_IO_select, "0b11111111")
        self.bindParameter("GPIO_D7_4_IO_select", self._GPIO_D7_4_IO_select, "0b1111")
        self.bindParameter("SPI_baudrate", self._SPI_baudrate, "100000")
        self.bindParameter("SPI_mode", self._SPI_mode, "0")
        self.bindParameter("SPI_cs_pin", self._SPI_cs_pin, "D4")
        self.bindParameter("SPI_cs_talking", self._SPI_cs_talking, "0")
        self.bindParameter("I2C_device_address", self._I2C_device_address, "0x08")
        self.bindParameter("SER_select", self._SER_select, "None")
        self.bindParameter("SER_timeout", self._SER_timeout, "1000")
        
        # Set InPort buffers
        self.addInPort("C7_0in",self._C7_0inIn)
        self.addInPort("D4in",self._D4inIn)
        self.addInPort("D5in",self._D5inIn)
        self.addInPort("D6in",self._D6inIn)
        self.addInPort("D7in",self._D7inIn)
        self.addInPort("I2C_SPIread",self._I2C_SPIreadIn)
        
        # Set OutPort buffers
        self.addOutPort("C7_0out",self._C7_0outOut)
        self.addOutPort("D4out",self._D4outOut)
        self.addOutPort("D5out",self._D5outOut)
        self.addOutPort("D6out",self._D6outOut)
        self.addOutPort("D7out",self._D7outOut)
        self.addOutPort("I2C_SPIwcommand_rbytes",self._I2C_SPIwcommand_rbytesOut)
        
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
        # コンフィギュレーション変数を読み込み、GPIOの各ピンを入力もしくは出力ピンに設
	# 定する。また、I2CもしくはSPI通信の設定を行う。
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
        # GPIOの全ての出力ピンにLowを出力する。I2CもしくはSPI通信を終了する。
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
        # InPortから値を読み込み、GPIOの各出力ピンから値に対応してHighまたはLowを出力す
	# る。
	# GPIO各入力ピンからHighまたはLowを読み込みOutPortから対応する値を出力する。
	# I2CもしくはSPI通信が設定されている場合は、InPortから読み込んだ値に応じてデバ
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
        # GPIOの全ての出力ピンにLowを出力する。I2CもしくはSPI通信を終了する。
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
    comp = manager.getComponent("Adafruit_FT232H_BreakoutTest0")
    if comp is None:
        print('Component get failed.', file=sys.stderr)
        return False
    return comp.runTest()

def Adafruit_FT232H_BreakoutTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=adafruit_ft232h_breakouttest_spec)
    manager.registerFactory(profile,
                            Adafruit_FT232H_BreakoutTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    Adafruit_FT232H_BreakoutTestInit(manager)
    Adafruit_FT232H_Breakout.Adafruit_FT232H_BreakoutInit(manager)

    # Create a component
    comp = manager.createComponent("Adafruit_FT232H_BreakoutTest")

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

