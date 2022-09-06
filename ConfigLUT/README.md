# ConfigLUT

## Overview

one-dimensional lookup table (LUT) component

## Description

1次元のLookup Table (LUT)コンポーネント。コンフィギュレーションでLUTの値となる整数のリストを指定する。要素番号を入力ポートから指定するとLUTの対応する値が出力ポートから出力される。範囲外の要素の番号が指定された場合は何も行わない。

### Input and Output

InPort<br/>ポート名/型/説明<br/>indext/TimedLong/値を出力するLUTの要素番号。先頭要素の番号は0番とする。負の値を入力した場合は、-1であれば最終要素の値、-2であれば最終要素の1つ前の値というように、逆順に数えた要素の値を出力する。<br/>OutPort<br/>ポート名/型/説明<br/>value/TimedLong/LUTの指定された要素の値。

### Algorithm etc



### Basic Information

|  |  |
----|---- 
| Module Name | ConfigLUT |
| Description | one-dimensional lookup table (LUT) component |
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
      <td>コンフィギュレーションから値を読み込み、LUTを作成する。入力ポートから要素番号の値を読み込み、LUTから対応する値を出力する。</td>
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

#### index

値を出力するLUTの要素番号。先頭要素の番号は0番とする。負の値を入力した場合は、-1であれば最終要素の値、-2であれば最終要素の1つ前の値というように、逆順に数えた要素の値を出力する。

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

#### value

LUTの指定された要素の値。

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

#### table

LUTの値。値はカンマ区切りで指定する（カンマ区切りで値を増減することで要素数を変更可能）。各要素は整数値で指定する。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>0,1,2,3</td>
    <td>0,1,2,3</td>
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
