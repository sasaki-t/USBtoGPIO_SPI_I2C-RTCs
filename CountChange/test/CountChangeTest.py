#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file CountChangeTest.py
 @brief Count input data change
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

import CountChange

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
countchangetest_spec = ["implementation_id", "CountChangeTest", 
         "type_name",         "CountChangeTest", 
         "description",       "Count input data change", 
         "version",           "1.0.0", 
         "vendor",            "TakeshiSasaki", 
         "category",          "generic", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.min", "0",
         "conf.default.max", "9",
         "conf.default.step", "1",
         "conf.default.change", "increase",

         "conf.__widget__.min", "text",
         "conf.__widget__.max", "text",
         "conf.__widget__.step", "text",
         "conf.__widget__.change", "radio",
         "conf.__constraints__.change", "(increase,decrease,change,nochange)",

         "conf.__type__.min", "int",
         "conf.__type__.max", "int",
         "conf.__type__.step", "int",
         "conf.__type__.change", "string",

         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class CountChangeTest
# @brief Count input data change
# 
# 入力値が1つ前の入力値と比べ指定の変化をするたびに出力値が増加する。出力の変化範
# 囲、変化幅はコンフィギュレーションで変更可能。どのような変化をカウントするか（増
# 加する、減少する、変化する、変化しない）もコンフィギュレーションで指定できる。
# 例）min=0, max=4, step=2, change=increaseのとき、
# 入力値の変化が1→4→7→3→5→2→2→5なら入力値が増加した1→4で0、4→7で2、3→5で
# 4、0→5で0が出力される。
# 
# InPort
# ポート名/型/説明
# data/TimedLong/変化を検知する対象。
# OutPort
# ポート名/型/説明
# count/TimedLong/
# 入力値が変化するたびに出力される値。出力される値の範囲や変化のタイミングについて
# はコンフィギュレーションで指定できる。
# 
# 
# </rtc-template>
class CountChangeTest(OpenRTM_aist.DataFlowComponentBase):
    
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_count = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        入力値が変化するたびに出力される値。出力される値の範囲や変化のタイミングにつ
		いてはコンフィギュレーションで指定できる。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._countIn = OpenRTM_aist.InPort("count", self._d_count)
        self._d_data = OpenRTM_aist.instantiateDataType(RTC.TimedLong)
        """
        変化を検知する対象。
         - Type: RTC::TimedLong
         - Number: 1
        """
        self._dataOut = OpenRTM_aist.OutPort("data", self._d_data)


        


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
        出力される値の最小値。min<=maxでなければならない。出力値が[min,
		max]の範囲を超えた場合、stepが正ならこの値が出力される。stepが非負のとき、最
		初に入力が指定の条件を満たしたときに出力される値もこの値になる。
         - Name: min min
         - DefaultValue: 0
        """
        self._min = [0]
        """
        出力される値の最大値。min<=maxでなければならない。出力値が[min,
		max]の範囲を超えた場合、stepが負ならこの値が出力される。stepが負のとき、最初
		に入力が指定の条件を満たしたときに出力される値もこの値になる。
         - Name: max max
         - DefaultValue: 9
        """
        self._max = [9]
        """
        指定された入力の変化を検知するたびに出力値が変化する幅。例えば、現在の出力値
		が0でstepが2なら次に出力される値は2、その次に出力される値は4となる。
         - Name: step step
         - DefaultValue: 1
        """
        self._step = [1]
        """
        出力ポートから値が出力されるタイミング。increaseの場合は入力値が1つ前の入力値
		と比べ増加した場合に、decreaseの場合は減少した場合に、changeの場合は増加もし
		くは減少した場合に、nochangeの場合は変化しなかった場合に出力ポートから値が出
		力される。
         - Name: change change
         - DefaultValue: increase
        """
        self._change = ['increase']
        
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
        self.bindParameter("min", self._min, "0")
        self.bindParameter("max", self._max, "9")
        self.bindParameter("step", self._step, "1")
        self.bindParameter("change", self._change, "increase")
        
        # Set InPort buffers
        self.addInPort("count",self._countIn)
        
        # Set OutPort buffers
        self.addOutPort("data",self._dataOut)
        
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
        # 初期化を行う。
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
        # 入力ポートから値を読み込み、直前の入力値と比較する。入力値にコンフィギュレー
	# ションで指定の変化があれば出力を行う。
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
    comp = manager.getComponent("CountChangeTest0")
    if comp is None:
        print('Component get failed.', file=sys.stderr)
        return False
    return comp.runTest()

def CountChangeTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=countchangetest_spec)
    manager.registerFactory(profile,
                            CountChangeTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    CountChangeTestInit(manager)
    CountChange.CountChangeInit(manager)

    # Create a component
    comp = manager.createComponent("CountChangeTest")

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

