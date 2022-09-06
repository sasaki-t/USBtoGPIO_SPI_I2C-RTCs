# CountChange

## Overview

Count input data change

## Description

入力値が1つ前の入力値と比べ指定の変化をするたびに出力値が増加する。出力の変化範囲、変化幅はコンフィギュレーションで変更可能。どのような変化をカウントするか（増加する、減少する、変化する、変化しない）もコンフィギュレーションで指定できる。<br/>例）min=0, max=4, step=2, change=increaseのとき、<br/>入力値の変化が1→4→7→3→5→2→2→5なら入力値が増加した1→4で0、4→7で2、3→5で4、0→5で0が出力される。

### Input and Output

InPort<br/>ポート名/型/説明<br/>data/TimedLong/変化を検知する対象。<br/>OutPort<br/>ポート名/型/説明<br/>count/TimedLong/ 入力値が変化するたびに出力される値。出力される値の範囲や変化のタイミングについてはコンフィギュレーションで指定できる。

### Algorithm etc



### Basic Information

|  |  |
----|---- 
| Module Name | CountChange |
| Description | Count input data change |
| Version | 1.0.0 |
| Vendor | TakeshiSasaki |
| Category | generic |
| Comp. Type | STATIC |
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
    <td rowspan="4">on_activated</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td>初期化を行う。</td>
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
    <td>on_deactivated</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td rowspan="4">on_execute</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td>入力ポートから値を読み込み、直前の入力値と比較する。入力値にコンフィギュレーションで指定の変化があれば出力を行う。</td>
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

#### data

変化を検知する対象。

<table>
  <tr>
    <td>DataType</td>
    <td>RTC::TimedLong</td>
    <td>RTC::TimedLong</td>
  </tr>
  <tr>
    <td>IDL file</td>
    <td colspan="2">BasicDataType.idl</td>
  </tr>
  <tr>
    <td>Number of Data</td>
    <td colspan="2">1</td>
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


### OutPorts definition

#### count

入力値が変化するたびに出力される値。出力される値の範囲や変化のタイミングについてはコンフィギュレーションで指定できる。

<table>
  <tr>
    <td>DataType</td>
    <td>RTC::TimedLong</td>
    <td>RTC::TimedLong</td>
  </tr>
  <tr>
    <td>IDL file</td>
    <td colspan="2">BasicDataType.idl</td>
  </tr>
  <tr>
    <td>Number of Data</td>
    <td colspan="2">1</td>
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

#### min

出力される値の最小値。min<=maxでなければならない。出力値が[min, max]の範囲を超えた場合、stepが正ならこの値が出力される。stepが非負のとき、最初に入力が指定の条件を満たしたときに出力される値もこの値になる。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">int</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Unit</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Widget</td>
    <td colspan="2">text</td>
  </tr>
  <tr>
    <td>Step</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Constraint</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### max

出力される値の最大値。min<=maxでなければならない。出力値が[min, max]の範囲を超えた場合、stepが負ならこの値が出力される。stepが負のとき、最初に入力が指定の条件を満たしたときに出力される値もこの値になる。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">int</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>9</td>
    <td>9</td>
  </tr>
  <tr>
    <td>Unit</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Widget</td>
    <td colspan="2">text</td>
  </tr>
  <tr>
    <td>Step</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Constraint</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### step

指定された入力の変化を検知するたびに出力値が変化する幅。例えば、現在の出力値が0でstepが2なら次に出力される値は2、その次に出力される値は4となる。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">int</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Unit</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Widget</td>
    <td colspan="2">text</td>
  </tr>
  <tr>
    <td>Step</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Constraint</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### change

出力ポートから値が出力されるタイミング。increaseの場合は入力値が1つ前の入力値と比べ増加した場合に、decreaseの場合は減少した場合に、changeの場合は増加もしくは減少した場合に、nochangeの場合は変化しなかった場合に出力ポートから値が出力される。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>increase</td>
    <td>increase</td>
  </tr>
  <tr>
    <td>Unit</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Widget</td>
    <td colspan="2">radio</td>
  </tr>
  <tr>
    <td>Step</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Constraint</td>
    <td>(increase,decrease,change,nochange)</td>
    <td></td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>


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
