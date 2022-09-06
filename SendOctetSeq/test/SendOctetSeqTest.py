#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file SendOctetSeqTest.py
 @brief Output console input data as OctetSeq
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

import SendOctetSeq

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
sendoctetseqtest_spec = ["implementation_id", "SendOctetSeqTest", 
         "type_name",         "SendOctetSeqTest", 
         "description",       "Output console input data as OctetSeq", 
         "version",           "1.0.0", 
         "vendor",            "TakeshiSasaki", 
         "category",          "generic", 
         "activity_type",     "COMMUTATIVE", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class SendOctetSeqTest
# @brief Output console input data as OctetSeq
# 
# コンソールから入力された値をRTC::TimedOctetSeq型のデータとして出力する。データは
# カンマ区切りで入力する。カンマで区切られた各データは[0,
# 255]の整数である必要がある。また、各データは0bや0xを値の前につけることで2進法や
# 16進法で指定することも可能。
# 
# InPort
# ポート名/型/説明
# out/TimedOctetSeq/コンソールから入力された値をRTC::TimedOctetSeq型のデータとした
# もの。
# 
# 
# </rtc-template>
class SendOctetSeqTest(OpenRTM_aist.DataFlowComponentBase):
    
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_out = OpenRTM_aist.instantiateDataType(RTC.TimedOctetSeq)
        """
        コンソールから入力された値をRTC::TimedOctetSeq型のデータとしたもの。
         - Type: RTC::TimedOctetSeq
         - Number: データに依存
        """
        self._outIn = OpenRTM_aist.InPort("out", self._d_out)


        


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        
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
        
        # Set InPort buffers
        self.addInPort("out",self._outIn)
        
        # Set OutPort buffers
        
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
    
    ###
    ##
    ## The activated action (Active state entry action)
    ##
    ## @param ec_id target ExecutionContext Id
    ## 
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onActivated(self, ec_id):
    #
    #    return RTC.RTC_OK
    
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
        # コンソールから入力された値をRTC::TimedOctetSeq型のデータとして出力する。
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
    comp = manager.getComponent("SendOctetSeqTest0")
    if comp is None:
        print('Component get failed.', file=sys.stderr)
        return False
    return comp.runTest()

def SendOctetSeqTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=sendoctetseqtest_spec)
    manager.registerFactory(profile,
                            SendOctetSeqTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    SendOctetSeqTestInit(manager)
    SendOctetSeq.SendOctetSeqInit(manager)

    # Create a component
    comp = manager.createComponent("SendOctetSeqTest")

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

