#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file BME280Decode.py
 @brief Convert BME280 raw data to pressure, temperature, and humidity measurement
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


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
bme280decode_spec = ["implementation_id", "BME280Decode", 
         "type_name",         "BME280Decode", 
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
# @class BME280Decode
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
class BME280Decode(OpenRTM_aist.DataFlowComponentBase):
    
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_SensorByteData = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        センサから得られるアドレス0xF7から0xFEの8バイトのバイト列。
            - Type: RTC::TimedOctetSeq
         - Number: 8
        """
        self._SensorByteDataIn = OpenRTM_aist.InPort("SensorByteData", self._d_SensorByteData)
        self._d_Pressure = OpenRTM_aist.instantiateDataType(RTC.TimedDouble)
        """
        計測した圧力。
         - Type: RTC::TimedDouble
         - Number: 1
         - Unit: hPa
        """
        self._PressureOut = OpenRTM_aist.OutPort("Pressure", self._d_Pressure)
        self._d_Temperature = OpenRTM_aist.instantiateDataType(RTC.TimedDouble)
        """
        計測した温度。
         - Type: RTC::TimedDouble
         - Number: 1
         - Unit: ℃
        """
        self._TemperatureOut = OpenRTM_aist.OutPort("Temperature", self._d_Temperature)
        self._d_Humidity = OpenRTM_aist.instantiateDataType(RTC.TimedDouble)
        """
        計測した湿度。
         - Type: RTC::TimedDouble
         - Number: 1
         - Unit: %
        """
        self._HumidityOut = OpenRTM_aist.OutPort("Humidity", self._d_Humidity)


        


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
        self.addInPort("SensorByteData",self._SensorByteDataIn)
        
        # Set OutPort buffers
        self.addOutPort("Pressure",self._PressureOut)
        self.addOutPort("Temperature",self._TemperatureOut)
        self.addOutPort("Humidity",self._HumidityOut)
        
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
        self.cT = [0] * 3
        self.cP = [0] * 9
        self.cH = [0] * 6

        #data check for calib data 0-25 (calib24 is not used)
        if len(self._calib00_25[0])>=26:
            try:
                if self._calib_data_type[0] == 'hex':
                    calib = bytearray.fromhex(self._calib00_25[0])
                elif self._calib_data_type[0] == 'utf-8':
                    calib = self._calib00_25[0].encode('utf-8')
                else:
                    print('Invalid configuration value (calib_data_type): unknown type')
            except ValueError:
                print('Invalid configuration value (calib00_25): cannot convert to bytearray')
                return RTC.RTC_ERROR
        else:
            print('Invalid configuration value (calib00_25): too short data length')
            return RTC.RTC_ERROR

        #calurate values for compensation
        self.cT[0] = int.from_bytes(calib[0:2], byteorder='little', signed=False)
        self.cT[1] = int.from_bytes(calib[2:4], byteorder='little', signed=True)
        self.cT[2] = int.from_bytes(calib[4:6], byteorder='little', signed=True)

        self.cP[0] = int.from_bytes(calib[6:8], byteorder='little', signed=False)
        self.cP[1] = int.from_bytes(calib[8:10], byteorder='little', signed=True)
        self.cP[2] = int.from_bytes(calib[10:12], byteorder='little', signed=True)
        self.cP[3] = int.from_bytes(calib[12:14], byteorder='little', signed=True)
        self.cP[4] = int.from_bytes(calib[14:16], byteorder='little', signed=True)
        self.cP[5] = int.from_bytes(calib[16:18], byteorder='little', signed=True)
        self.cP[6] = int.from_bytes(calib[18:20], byteorder='little', signed=True)
        self.cP[7] = int.from_bytes(calib[20:22], byteorder='little', signed=True)
        self.cP[8] = int.from_bytes(calib[22:24], byteorder='little', signed=True)

        self.cH[0] = int.from_bytes(calib[25:26], byteorder='little', signed=False)

        #data check for calib data 26-41  (calib33-41 is not used)
        if len(self._calib26_41[0])>=7:
            try:
                if self._calib_data_type[0] == 'hex':
                    calib = bytearray.fromhex(self._calib26_41[0])
                elif self._calib_data_type[0] == 'utf-8':
                    calib = self._calib26_41[0].encode('utf-8')
                else:
                    print('Invalid configuration value (calib_data_type): unknown type')
            except ValueError:
                print('Invalid configuration value  (calib26_41): cannot convert to bytearray')
                return RTC.RTC_ERROR
        else:
            print('Invalid configuration value (calib26_41): too short data length')
            return RTC.RTC_ERROR

        #calurate values for compensation
        self.cH[1] = int.from_bytes(calib[0:2], byteorder='little', signed=True)
        self.cH[2] = int.from_bytes(calib[2:3], byteorder='little', signed=False)
        self.cH[3] = (int.from_bytes(calib[3:4], byteorder='little', signed=True) << 4) + (calib[4] & 0x0F)
        self.cH[4] = int.from_bytes(calib[4:6], byteorder='little', signed=True) >> 4
        self.cH[5] = int.from_bytes(calib[6:7], byteorder='little', signed=True)

        return RTC.RTC_OK
    
    ###
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
        if self._SensorByteDataIn.isNew():
            self._d_SensorByteData = self._SensorByteDataIn.read()
            if len(self._d_SensorByteData.data) >= 8:
                rawP = (self._d_SensorByteData.data[0]<<12) | (self._d_SensorByteData.data[1]<<4) | ((self._d_SensorByteData.data[2]>>4) & 0x0F)
                rawT = (self._d_SensorByteData.data[3]<<12) | (self._d_SensorByteData.data[4]<<4) | ((self._d_SensorByteData.data[5]>>4) & 0x0F)
                rawH = (self._d_SensorByteData.data[6]<<8) | self._d_SensorByteData.data[7]

                (self._d_Pressure.data, self._d_Temperature.data, self._d_Humidity.data) = self.compensate(rawP, rawT, rawH)
                print(f'Pressure: {self._d_Pressure.data} hPa, Temperature: {self._d_Temperature.data} deg C, Humidity: {self._d_Humidity.data} %')
                self._PressureOut.write()
                self._TemperatureOut.write()
                self._HumidityOut.write()
            else:
                print('input data is too short')
    
        return RTC.RTC_OK
    
    ###
    ##
    ## Compensation function
    ##
    ## @param rawP raw pressure measurement data
    ## @param rawT raw temperature measurement data
    ## @param rawH raw humidity measurement data
    ##
    ## @return pressure [hPa], temperature [degree C] , humidity [%]
    ##
    ##
    def compensate(self, rawP, rawT, rawH):
        #calculate compensation parameter
        var1  = ((((rawT>>3) - (self.cT[0]<<1))) * self.cT[1]) >> 11
        var2  = (((((rawT>>4) - self.cT[0]) * ((rawT>>4) - self.cT[0])) >> 12) * self.cT[2]) >> 14
        t_fine = var1 + var2

        #compensation
        t = self.compensate_T(t_fine) / 100.0 #convert to degree C
        h = self.compensate_H(rawH, t_fine) / 1024.0 #convert to %
        p = self.compensate_P64(rawP, t_fine) / 25600.0 #convert to hPa
        #p = self.compensate_P32(rawP, t_fine) / 100.0 #convert to hPa
        return p, t, h

    ###
    ##
    ## Compensation for temperature
    ##
    ## @param t_fine compensation parameter
    ##
    ## @return value proportional to temperature 
    ##
    ##
    def compensate_T(self, t_fine):
        return (t_fine * 5 + 128) >> 8

    ###
    ##
    ## Compensation for humidity
    ##
    ## @param rawH raw humidity measurement data
    ## @param t_fine compensation parameter
    ##
    ## @return value proportional to humidity
    ##
    ##
    def compensate_H(self, rawH, t_fine):
        v_x1_u32r = t_fine - 76800
        v_x1_u32r = (((((rawH << 14) - (self.cH[3] << 20) - (self.cH[4] * v_x1_u32r)) + 16384) >> 15) * (((((((v_x1_u32r * self.cH[5]) >> 10) * (((v_x1_u32r * self.cH[2]) >> 11) + 32768)) >> 10) + 2097152) * self.cH[1] + 8192) >> 14))
        v_x1_u32r = v_x1_u32r - (((((v_x1_u32r >> 15) * (v_x1_u32r >> 15)) >> 7) * self.cH[0]) >> 4)

        if v_x1_u32r < 0:
            v_x1_u32r = 0
        elif v_x1_u32r > 419430400:
            v_x1_u32r = 419430400
        return v_x1_u32r>>12

    ###
    ##
    ## Compensation for pressure
    ##
    ## @param rawP raw pressure measurement data
    ## @param t_fine compensation parameter
    ##
    ## @return value proportional to pressure
    ##
    ##
    def compensate_P64(self, rawP, t_fine):
        var1 = t_fine - 128000
        var2 = var1 * var1 * self.cP[5] + ((var1*self.cP[4])<<17) + (self.cP[3]<<35)
        var1 = ((var1 * var1 * self.cP[2])>>8) + ((var1 * self.cP[1])<<12)
        var1 = (((1<<47)+var1)*self.cP[0])>>33
        if var1 == 0:
            return 0

        p = 1048576-rawP
        p = int((((p<<31)-var2)*3125)/var1)
        var1 = (self.cP[8] * (p>>13) * (p>>13)) >> 25
        var2 = (self.cP[7] * p) >> 19
        p = ((p + var1 + var2) >> 8) + (self.cP[6]<<4)
        return p
    '''
    def compensate_32(self, rawP, t_fine):
        var1 = (t_fine>>1) - 64000
        var2 = (((var1>>2) * (var1>>2)) >> 11) * self.cP[5] + ((var1*self.cP[4])<<1)
        var2 = (var2>>2)+(self.cP[3]<<16)
        var1 = (((self.cP[2] * (((var1>>2) * (var1>>2)) >> 13 )) >> 3) + ((self.cP[1] * var1)>>1))>>18
        var1 =((32768+var1)*self.cP[0])>>15
        if var1 == 0:
            return 0

        p = ((1048576-rawP)-(var2>>12))*3125
        p = int((p << 1) / var1)
        var1 = (self.cP[8] * (((p>>3) * (p>>3))>>13))>>12;
        var2 = ((p>>2) * self.cP[7])>>13
        p = p + ((var1 + var2 + self.cP[6]) >> 4)

        return p
    '''

    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
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
    



def BME280DecodeInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=bme280decode_spec)
    manager.registerFactory(profile,
                            BME280Decode,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    BME280DecodeInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("BME280Decode" + args)

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

