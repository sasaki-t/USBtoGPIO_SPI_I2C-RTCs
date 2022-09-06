# BME280Decode

## Overview

Convert BME280 raw data to pressure, temperature, and humidity measurement

## Description

BME280の8バイトのバイト列(press_msb, press_lsb, press_xlsb, temp_msb, temp_lsb, temp_xlsb, hum_msb, hum_lsb)とキャリブレーションデータ(calib00～calib41)から気圧、温度、湿度を計算し、各出力ポートから出力する。キャリブレーションデータはコンフィギュレーションから入力する。

### Input and Output

InPort<br/>ポート名/型/説明<br/>SensorByteData/TimedOctetSeq/センサから得られるアドレス0xF7から0xFEの8バイトのバイト列。<br/>OutPort<br/>ポート名/型/説明<br/>Pressure/TimedDouble/計測した圧力[hPa]。<br/>Temperature/TimedDouble/計測した温度[℃]。<br/>Humidity/TimedDouble/計測した湿度[%]。

### Algorithm etc

気圧、温度、湿度の計算式はBME280データシートを参照。

### Basic Information

|  |  |
----|---- 
| Module Name | BME280Decode |
| Description | Convert BME280 raw data to pressure, temperature, and humidity measurement |
| Version | 1.0.0 |
| Vendor | TakeshiSasaki |
| Category | Sensor |
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
    <td rowspan="4">on_activated</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td>キャリブレーションデータをコンフィギュレーションから読み取る。</td>
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
      <td>入力ポートからのセンサデータとキャリブレーションパラメータから気圧、温度、湿度を計算し、それぞれの出力ポートから出力する。</td>
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

#### SensorByteData

センサから得られるアドレス0xF7から0xFEの8バイトのバイト列。

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
    <td colspan="2">8</td>
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

#### Pressure

計測した圧力。

<table>
  <tr>
    <td>DataType</td>
    <td>RTC::TimedDouble</td>
    <td>RTC::TimedDouble</td>
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
    <td colspan="2">hPa</td>
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

#### Temperature

計測した温度。

<table>
  <tr>
    <td>DataType</td>
    <td>RTC::TimedDouble</td>
    <td>RTC::TimedDouble</td>
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
    <td colspan="2">℃</td>
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

#### Humidity

計測した湿度。

<table>
  <tr>
    <td>DataType</td>
    <td>RTC::TimedDouble</td>
    <td>RTC::TimedDouble</td>
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
    <td colspan="2">%</td>
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

#### calib00_25

アドレス0x88から0xA1の26バイトのキャリブレーションデータ。<br/>バイト列をhex文字列（1バイトにつき 2つの16進数を含む文字列）もしくはutf-8でデコードした文字列で指定する。どちらの文字列なのかによってコンフィギュレーション変数calib_data_typeも変更すること。<br/>アクティブ状態での変更は無効（反映されない）。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>346f03673200cc8c1bd6d00bb1146c00f9ff0c3020d18813004b</td>
    <td></td>
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

#### calib26_41

アドレス0xE1から0xF0の16バイトのキャリブレーションデータのバイト列。使用するのは最初の7バイトのため、7バイト以上のデータがあればよい。<br/>バイト列をhex文字列（1バイトにつき 2つの16進数を含む文字列）もしくはutf-8でデコードした文字列で指定する。どちらの文字列なのかによってコンフィギュレーション変数calib_data_typeも変更すること。<br/>アクティブ状態での変更は無効（反映されない）。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>4c0100182e031e</td>
    <td></td>
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

#### calib_data_type

キャリブレーションデータ(calib0_25, calib26_41）をhex文字列（1バイトにつき 2つの16進数を含む文字列）として入力したのかutf-8でデコードした文字列で入力したのかを指定する。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>hex</td>
    <td>hex</td>
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
    <td>(utf-8,hex)</td>
    <td>(utf-8, hex)</td>
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
