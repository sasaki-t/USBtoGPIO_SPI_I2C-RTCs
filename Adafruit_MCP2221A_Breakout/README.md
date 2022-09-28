# Adafruit_MCP2221A_Breakout

## Overview

USB to Digital/Analog IO and I2C, UART components using Adafruit MCP2221A Breakout

## Description

Adafruit MCP2221A Breakoutを使用したUSB-GPIO, I2C, UART変換コンポーネント。GPIOに関しては、まずコンフィギュレーションから各ピンの利用方法（アナログ/ディジタル、入力/出力）を選択する。出力として設定したピンに対しては、対応するInPortに値が入力されると、その値に応じてディジタル出力であればHigh/Low、アナログ出力であれば0-最大電圧（ハードウェアのジャンパで3.3Vか5.0Vを設定）を出力する。入力として設定したピンに対しては、ディジタル入力であればHigh/Low、アナログ入力であれば電圧値を読み込み、それに応じた値を対応するOutPortから出力する。I2CやUARTについても、まずコンフィギュレーションからそれぞれを利用するか、利用するならばそのパラメータを設定する。送信するデータや受信バイト数はInPortから入力し、受信したデータはOutPortから出力される。<br/>Windows, Macの場合はhidapi, pyserialおよびAdafruit Blinkaのインストールが必要。Linuxの場合はこれらに加えlibusb、libudevのインストールが必要。

### Input and Output

InPort<br/>ポート名/型/説明<br/>G*out/TimedLong/G*を出力ピンとしている場合のピンからの出力に対応した値。<br/>ディジタル出力の場合、Highとする場合は1を、Lowとする場合は0を入力する。<br/>アナログ出力の場合、0（0V）から65535（最大電圧、ハードウェアのジャンパで3.3Vか5.0Vを設定）の値で出力電圧を指定する。<br/>DAコンバータは1つのみのため、G2とG3をどちらもアナログ出力とした場合にはG2, G3からは同じ電圧が出力される。<br/>入力ピンとして指定されている場合は何を入力しても影響はない。<br/>I2Cwcommand_rbytes/TimedOctetSeq/I2C通信で送信するデータ・受信するデータのバイト数。<br/>最終要素の前までが送信データ、最終要素が受信バイト数となる。例えば、1,2,3というデータの場合は1,2という2バイトの値をデバイスに送信し、その後3バイトの情報をデバイスから受信する。<br/>受信バイト数が0の場合は送信だけを行い、受信を行わない（例: 1,2,0）。<br/>受信バイト数のみが指定されている場合（要素が1つの場合）は送信を行わず受信だけを行う（例: 3）。<br/>UARTwcommand_rbytes/TimedOctetSeq/UART通信で送信するデータ・受信するデータのバイト数。<br/>最終要素の前までが送信データ、最終要素が受信バイト数となる。例えば、1,2,3というデータの場合は1,2という2バイトの値をデバイスに送信し、その後3バイトの情報をデバイスから受信する。<br/>受信バイト数が0の場合は送信だけを行い、受信を行わない（例: 1,2,0）。<br/>受信バイト数のみが指定されている場合（要素が1つの場合）は送信を行わず受信だけを行う（例: 3）。<br/>例外として、受信バイト数が255の場合には1行受信を行う。<br/>OutPort<br/>ポート名/型/説明<br/>G*in/TimedLong/G*を入力ピンとしている場合のピンへの入力に対応する値。<br/>ディジタル入力の場合、Highの場合は1が、Lowの場合は0が出力される。<br/>アナログ入力の場合、入力電圧に応じて0（0V）から65535（最大電圧、ハードウェアのジャンパで3.3Vか5.0Vを設定）の値が出力される。<br/>出力ピンに指定されている場合は出力を行わない。<br/>I2Cread/TimedOctetSeq/I2C通信で受信したデータ。<br/>UARTread/TimedOctetSeq/UART通信で受信したデータ。

### Algorithm etc



### Basic Information

|  |  |
----|---- 
| Module Name | Adafruit_MCP2221A_Breakout |
| Description | USB to Digital/Analog IO and I2C, UART components using Adafruit MCP2221A Breakout |
| Version | 1.0.0 |
| Vendor | TakeshiSasaki |
| Category | GPIO |
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
      <td>コンフィギュレーション変数を読み込み、GPIOの各ピンのアナログ/ディジタル、入力/は出力を設定する。また、I2CおよびUART通信の設定を行う。</td>
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
    <td rowspan="4">on_deactivated</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td>GPIOの全ての出力ピンにLowもしくは0Vを出力する。I2CおよびUART通信を終了する。</td>
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
    <td rowspan="4">on_execute</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td>InPortから値を読み込み、GPIOの各出力ピンから値に対応してHigh/Lowやアナログ電圧を出力する。<br/>GPIOの各入力ピンからHighまたはLowを読み込みOutPortから対応する値を出力する。<br/>I2CもしくはUART通信が設定されている場合は、InPortから読み込んだ値に応じてデバイスへの書き込みやデバイスからの読み込みを行い、OutPortからの出力を行う。</td>
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
    <td rowspan="4">on_aborting</td>
    <td colspan="2">implemented</td>
    <tr>
      <td>Description</td>
      <td>GPIOの全ての出力ピンにLowもしくは0Vを出力する。I2CおよびUART通信を終了する。</td>
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

#### G0out

G0をディジタル出力ピンとしている場合のピンからの出力に対応した値。<br/>Highとする場合は1を、Lowとする場合は0を入力する。<br/>入力ピンとして指定されている場合はどちらを入力しても影響はない。

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

#### G1out

G1をディジタル出力ピンとしている場合のピンからの出力に対応した値。<br/>Highとする場合は1を、Lowとする場合は0を入力する。<br/>入力ピンとして指定されている場合はどちらを入力しても影響はない。

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

#### G2out

G2を出力ピンとしている場合のピンからの出力に対応した値。<br/>ディジタル出力の場合、Highとする場合は1を、Lowとする場合は0を入力する。<br/>アナログ出力の場合、0（0V）から65535（最大電圧、ハードウェアのジャンパで3.3Vか5.0Vを設定）の値で出力電圧を指定する。<br/>DAコンバータは1つのみのため、G2とG3をどちらもアナログ出力とした場合にはG3からも同じ電圧が出力される。<br/>入力ピンとして指定されている場合は何を入力しても影響はない。

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

#### G3out

G3を出力ピンとしている場合のピンからの出力に対応した値。<br/>ディジタル出力の場合、Highとする場合は1を、Lowとする場合は0を入力する。<br/>アナログ出力の場合、0（0V）から65535（最大電圧、ハードウェアのジャンパで3.3Vか5.0Vを設定）の値で出力電圧を指定する。<br/>DAコンバータは1つのみのため、G2とG3をどちらもアナログ出力とした場合にはG3からも同じ電圧が出力される。<br/>入力ピンとして指定されている場合は何を入力しても影響はない。

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

#### I2Cwcommand_rbytes

I2C通信で送信するデータ・受信するデータのバイト数。<br/>最終要素の前までが送信データ、最終要素が受信バイト数となる。例えば、1,2,3というデータの場合は1,2という2バイトの値をデバイスに送信し、その後3バイトの情報をデバイスから受信する。<br/>受信バイト数が0の場合は送信だけを行い、受信を行わない（例: 1,2,0）。<br/>受信バイト数のみが指定されている場合（要素が1つの場合）は送信を行わず受信だけを行う（例: 3）。

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
    <td colspan="2">データに依存。</td>
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

#### UARTwcommand_rbytes

UART通信で送信するデータ・受信するデータのバイト数。<br/>最終要素の前までが送信データ、最終要素が受信バイト数となる。例えば、1,2,3というデータの場合は1,2という2バイトの値をデバイスに送信し、その後3バイトの情報をデバイスから受信する。<br/>受信バイト数が0の場合は送信だけを行い、受信を行わない（例: 1,2,0）。<br/>受信バイト数のみが指定されている場合（要素が1つの場合）は送信を行わず受信だけを行う（例: 3）。<br/>例外として、受信バイト数が255の場合には1行受信を行う。

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
    <td colspan="2">データに依存。</td>
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

#### G0in

G0をディジタル入力ピンとしている場合のピンへの入力に対応する値。<br/>Highの場合は1が、Lowの場合は0が出力される。<br/>出力ピンに指定されている場合は出力を行わない。

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

#### G1in

G1を入力ピンとしている場合のピンへの入力に対応する値。<br/>ディジタル入力の場合、Highの場合は1が、Lowの場合は0が出力される。<br/>アナログ入力の場合、入力電圧に応じて0（0V）から65535（最大電圧、ハードウェアのジャンパで3.3Vか5.0Vを設定）の値が出力される。<br/>出力ピンに指定されている場合は出力を行わない。

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

#### G2in

G2を入力ピンとしている場合のピンへの入力に対応する値。<br/>ディジタル入力の場合、Highの場合は1が、Lowの場合は0が出力される。<br/>アナログ入力の場合、入力電圧に応じて0（0V）から65535（最大電圧、ハードウェアのジャンパで3.3Vか5.0Vを設定）の値が出力される。<br/>出力ピンに指定されている場合は出力を行わない。

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

#### G3in

G3を入力ピンとしている場合のピンへの入力に対応する値。<br/>ディジタル入力の場合、Highの場合は1が、Lowの場合は0が出力される。<br/>アナログ入力の場合、入力電圧に応じて0（0V）から65535（最大電圧、ハードウェアのジャンパで3.3Vか5.0Vを設定）の値が出力される。<br/>出力ピンに指定されている場合は出力を行わない。

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

#### I2Cread

I2C通信で受信したデータ。

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
    <td colspan="2">データに依存。</td>
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

#### UARTread

UART通信で受信したデータ。

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
    <td colspan="2">データに依存。</td>
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

#### GPIO_G0_select

G0ピンの利用方法（ディジタル入力/ディジタル出力）を指定する。<br/>DIであればディジタル入力、DOであればディジタル出力になる。<br/>アクティブ状態での変更は無効（反映されない）。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>DI</td>
    <td>DI</td>
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
    <td>(DI,DO)</td>
    <td>(DI,DO)</td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### GPIO_G1_select

G1ピンの利用方法（ディジタル入力/ディジタル出力/アナログ入力）を指定する。<br/>DIであればディジタル入力、DOであればディジタル出力、AIであればアナログ入力になる。<br/>アクティブ状態での変更は無効（反映されない）。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>DI</td>
    <td>DI</td>
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
    <td>(DI,DO,AI)</td>
    <td>(DI,DO,AI)</td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### GPIO_G2_select

G2ピンの利用方法（ディジタル入力/ディジタル出力/アナログ入力/アナログ出力）を指定する。<br/>DIであればディジタル入力、DOであればディジタル出力、AIであればアナログ入力、AOであればアナログ出力になる。DAコンバータは1つのみのため、G2とG3をどちらもアナログ出力とした場合にはG3からも同じ電圧が出力される。<br/>アクティブ状態での変更は無効（反映されない）。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>DI</td>
    <td>DI</td>
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
    <td>(DI,DO,AI,AO)</td>
    <td>(DI,DO,AI,AO)</td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### GPIO_G3_select

G3ピンの利用方法（ディジタル入力/ディジタル出力/アナログ入力/アナログ出力）を指定する。<br/>DIであればディジタル入力、DOであればディジタル出力、AIであればアナログ入力、AOであればアナログ出力になる。DAコンバータは1つのみのため、G2とG3をどちらもアナログ出力とした場合にはG2からも同じ電圧が出力される。<br/>アクティブ状態での変更は無効（反映されない）。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>DI</td>
    <td>DI</td>
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
    <td>(DI,DO,AI,AO)</td>
    <td>(DI,DO,AI,AO)</td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### I2C_use

I2C通信を使用するか、使用しないかを選択する。1であれば使用し、0であれば使用しない。<br/>アクティブ状態での変更は無効（反映されない）。


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
    <td colspan="2">radio</td>
  </tr>
  <tr>
    <td>Step</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Constraint</td>
    <td>(0,1)</td>
    <td>(0,1)</td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### I2C_device_address

I2Cデバイスの7ビットアドレス。0bや0xを値の前につけることで2進法や16進法で指定することも可能。<br/>I2Cを使用しない場合はこの設定は無視される。<br/>アクティブ状態での変更は無効（反映されない）。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>0x08</td>
    <td>0x08</td>
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
    <td colspan="2">[0x08, 0x77]</td>
  </tr>
</table>

#### I2C_timeout

I2C通信においてバスをロックするときの最大待ち時間。この時間を超えてもバスがロックできない場合はエラーとする。<br/>I2Cを使用しない場合はこの設定は無視される。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">int</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>1000</td>
    <td>1000</td>
  </tr>
  <tr>
    <td>Unit</td>
    <td>ms</td>
    <td>ms</td>
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
    <td>x>=0</td>
    <td>x>=0</td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### UART_use

UART通信を使用するか、使用しないかを選択する。1であれば使用し、0であれば使用しない。<br/>アクティブ状態での変更は無効（反映されない）。


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
    <td colspan="2">radio</td>
  </tr>
  <tr>
    <td>Step</td>
    <td colspan="2"></td>
  </tr>
  <tr>
    <td>Constraint</td>
    <td>(0,1)</td>
    <td>(0,1)</td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### UART_port

UART通信を行う際のポート。Windowsの場合はCOMx、Linuxの場合は/dev/ttACMx等。<br/>UARTを使用しない場合はこの設定は無視される。<br/>アクティブ状態での変更は無効（反映されない）。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>COM3</td>
    <td>COM3</td>
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

#### UART_baudrate

UART通信の通信速度。<br/>UARTを使用しない場合はこの設定は無視される。<br/>アクティブ状態での変更は無効（反映されない）。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">int</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>115200</td>
    <td>115200</td>
  </tr>
  <tr>
    <td>Unit</td>
    <td>bps</td>
    <td>bps</td>
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
    <td>x>0</td>
    <td>x>0</td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### UART_read_timeout

UART通信における読み込みの最大待ち時間。<br/>この時間を超えても指定のバイト数が読み取れない場合はそれまでに読み込んだデータを出力する。<br/>負の値を設定した場合は指定されたバイト数が読み込まれるまで待つ。<br/>UARTを使用しない場合はこの設定は無視される。<br/>アクティブ状態での変更は無効（反映されない）。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">float</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>10.0</td>
    <td>10.0</td>
  </tr>
  <tr>
    <td>Unit</td>
    <td>sec</td>
    <td>sec</td>
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

ライブラリのセットアップについて<br/>https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-mcp2221


## Author

佐々木毅 (Takeshi SASAKI) <sasaki-t(_at_)ieee.org>
