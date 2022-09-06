# SendOctetSeq

## Overview

Output console input data as OctetSeq

## Description

コンソールから入力された値をRTC::TimedOctetSeq型のデータとして出力する。データはカンマ区切りで入力する。カンマで区切られた各データは[0, 255]の整数である必要がある。また、各データは0bや0xを値の前につけることで2進法や16進法で指定することも可能。

### Input and Output

InPort<br/>ポート名/型/説明<br/>out/TimedOctetSeq/コンソールから入力された値をRTC::TimedOctetSeq型のデータとしたもの。

### Algorithm etc



### Basic Information

|  |  |
----|---- 
| Module Name | SendOctetSeq |
| Description | Output console input data as OctetSeq |
| Version | 1.0.0 |
| Vendor | TakeshiSasaki |
| Category | generic |
| Comp. Type | COMMUTATIVE |
| Act. Type | PERIODIC |
| Kind | DataFlowComponent |
| MAX Inst. | 1 |

### Activity definition

<table>
  <tr>
    <td rowspan="4">on_initialize</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td></td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
  <tr>
    <td>on_finalize</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_startup</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_shutdown</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_activated</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_deactivated</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td rowspan="4">on_execute</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td>コンソールから入力された値をRTC::TimedOctetSeq型のデータとして出力する。</td>
    </tr>
    <tr>
      <td>PreCondition</td>
      <td></td>
    </tr>
    <tr>
      <td>PostCondition</td>
      <td></td>
    </tr>
  </tr>
  <tr>
    <td>on_aborting</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_error</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_reset</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_state_update</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>on_rate_changed</td>
    <td colspan="2"></td>
  </tr>
</table>

### InPorts definition


### OutPorts definition

#### out

コンソールから入力された値をRTC::TimedOctetSeq型のデータとしたもの。

<table>
  <tr>
    <td>DataType</td>
    <td>RTC::TimedOctetSeq</td>
    <td>RTC::TimedOctetSeq</td>
  </tr>
  <tr>
    <td>IDL file</td>
    <td colspan="2">BasicDataType.idl</td>
  </tr>
  <tr>
    <td>Number of Data</td>
    <td colspan="2">データに依存</td>
  </tr>
  <tr>
    <td>Semantics</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Unit</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Occirrence frecency Period</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Operational frecency Period</td>
    <td colspan="2"></td>
  </tr>
</table>


### Service Port definition


### Configuration definition


## Demo

## Requirement

## Setup

### Windows

### Ubuntu

## Usage

## Running the tests

## LICENCE




## References




## Author

佐々木毅 (Takeshi SASAKI) <sasaki-t(_at_)ieee.org>
