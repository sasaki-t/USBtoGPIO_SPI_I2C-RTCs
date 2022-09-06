#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file BME280DecodeTest.py
 @brief Convert BME280 raw data to pressure, temperature, and humidity measurement
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

import BME280Decode

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
bme280decodetest_spec = ["implementation_id", "BME280DecodeTest", 
         "type_name",         "BME280DecodeTest", 
         "description",       "Convert BME280 raw data to pressure, temperature, and humidity measurement", 
         "version",           "1.0.0", 
         "vendor",            "TakeshiSasaki", 
         "category",          "Sensor", 
         "activity_type",     "COMMUTATIVE", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.calib00_25", "346f03673200cc8c1bd6d00bb1146c00f9ff0c3020d18813004b",
         "conf.default.calib26_41", "4c0100182e031e",
         "conf.default.calib_data_type", "hex",

         "conf.__widget__.calib00_25", "text",
         "conf.__widget__.calib26_41", "text",
         "conf.__widget__.calib_data_type", "radio",
         "conf.__constraints__.calib_data_type", "(utf-8,hex)",

         "conf.__type__.calib00_25", "string",
         "conf.__type__.calib26_41", "string",
         "conf.__type__.calib_data_type", "string",

         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class BME280DecodeTest
# @brief Convert BME280 raw data to pressure, temperature, and humidity measurement
# 
# BME280の8バイトのバイト列(press_msb, press_lsb, press_xlsb, temp_msb,
# temp_lsb, temp_xlsb, hum_msb,
# hum_lsb)とキャリブレーションデータ(calib00～calib41)から気圧、温度、湿度を計算し
# 、各出力ポートから出力する。キャリブレーションデータはコンフィギュレーションから
# 入力する。
# 
# InPort
# ポート名/型/説明
# SensorByteData/TimedOctetSeq/センサから得られるアドレス0xF7から0xFEの8バイトのバ
# イト列。
# OutPort
# ポート名/型/説明
# Pressure/TimedDouble/計測した圧力[hPa]。
# Temperature/TimedDouble/計測した温度[℃]。
# Humidity/TimedDouble/計測した湿度[%]。
# 
# 気圧、温度、湿度の計算式はBME280データシートを参照。
# 
# 
# </rtc-template>
class BME280DecodeTest(OpenRTM_aist.DataFlowComponentBase):
    
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_Pressure = OpenRTM_aist.instantiateDataType(RTC.TimedDouble)
        """
        計測した圧力。
         - Type: RTC::TimedDouble
         - Number: 1
         - Unit: hPa
        """
        self._PressureIn = OpenRTM_aist.InPort("Pressure", self._d_Pressure)
        self._d_Temperature = OpenRTM_aist.instantiateDataType(RTC.TimedDouble)
        """
        計測した温度。
         - Type: RTC::TimedDouble
         - Number: 1
         - Unit: ℃
        """
        self._TemperatureIn = OpenRTM_aist.InPort("Temperature", self._d_Temperature)
        self._d_Humidity = OpenRTM_aist.instantiateDataType(RTC.TimedDouble)
        """
        計測した湿度。
         - Type: RTC::TimedDouble
         - Number: 1
         - Unit: %
        """
        self._HumidityIn = OpenRTM_aist.InPort("Humidity", self._d_Humidity)
        self._d_SensorByteData = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        センサから得られるアドレス0xF7から0xFEの8バイトのバイト列。
         - Type: RTC::TimedOctetSeq
         - Number: 8
        """
        self._SensorByteDataOut = OpenRTM_aist.OutPort("SensorByteData", self._d_SensorByteData)


        


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
        アドレス0x88から0xA1の26バイトのキャリブレーションデータ。
		バイト列をhex文字列（1バイトにつき
		2つの16進数を含む文字列）もしくはutf-8でデコードした文字列で指定する。どちら
		の文字列なのかによってコンフィギュレーション変数calib_data_typeも変更すること
		。
		アクティブ状態での変更は無効（反映されない）。
         - Name: calib00_25 calib00_25
         - DefaultValue: 346f03673200cc8c1bd6d00bb1146c00f9ff0c3020d18813004b
        """
        self._calib00_25 = ['346f03673200cc8c1bd6d00bb1146c00f9ff0c3020d18813004b']
        """
        アドレス0xE1から0xF0の16バイトのキャリブレーションデータのバイト列。使用する
		のは最初の7バイトのため、7バイト以上のデータがあればよい。
		バイト列をhex文字列（1バイトにつき
		2つの16進数を含む文字列）もしくはutf-8でデコードした文字列で指定する。どちら
		の文字列なのかによってコンフィギュレーション変数calib_data_typeも変更すること
		。
		アクティブ状態での変更は無効（反映されない）。
         - Name: calib26_41 calib26_41
         - DefaultValue: 4c0100182e031e
        """
        self._calib26_41 = ['4c0100182e031e']
        """
        キャリブレーションデータ(calib0_25, calib26_41）をhex文字列（1バイトにつき
		2つの16進数を含む文字列）として入力したのかutf-8でデコードした文字列で入力し
		たのかを指定する。
         - Name: calib_data_type calib_data_type
         - DefaultValue: hex
         - Constraint: (utf-8, hex)
        """
        self._calib_data_type = ['hex']
        
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
        self.bindParameter("calib00_25", self._calib00_25, "346f03673200cc8c1bd6d00bb1146c00f9ff0c3020d18813004b")
        self.bindParameter("calib26_41", self._calib26_41, "4c0100182e031e")
        self.bindParameter("calib_data_type", self._calib_data_type, "hex")
        
        # Set InPort buffers
        self.addInPort("Pressure",self._PressureIn)
        self.addInPort("Temperature",self._TemperatureIn)
        self.addInPort("Humidity",self._HumidityIn)
        
        # Set OutPort buffers
        self.addOutPort("SensorByteData",self._SensorByteDataOut)
        
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
        # キャリブレーションデータをコンフィギュレーションから読み取る。
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
    
    #    ##
    ##
    ## The deactivated action (Active state exit action)
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onDeactivated(self, ec_id):
    #
    #    return RTC.RTC_OK
    
    ##
        # 入力ポートからのセンサデータとキャリブレーションパラメータから気圧、温度、湿
	# 度を計算し、それぞれの出力ポートから出力する。
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
    
    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    #    #
    ##
    #def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK
    
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
    comp = manager.getComponent("BME280DecodeTest0")
    if comp is None:
        print('Component get failed.', file=sys.stderr)
        return False
    return comp.runTest()

def BME280DecodeTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=bme280decodetest_spec)
    manager.registerFactory(profile,
                            BME280DecodeTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    BME280DecodeTestInit(manager)
    BME280Decode.BME280DecodeInit(manager)

    # Create a component
    comp = manager.createComponent("BME280DecodeTest")

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

