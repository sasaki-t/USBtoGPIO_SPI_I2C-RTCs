# Adafruit_FT232H_Breakout

## Overview

USB to Digital IO and I2C/SPI components using Adafruit FT232H Breakout

## Description

Adafruit FT232H Breakoutを使用したUSB-GPIO, SPI, I2C変換コンポーネント。GPIOに関しては、まずコンフィギュレーションから各ピンをディジタル入力として使うか、ディジタル出力として使うかを選択する。出力として設定したピンに対しては、対応するInPortに値が入力されると、その値に応じてHighまたはLowを出力する。入力として設定したピンに対しては、HighまたはLowを読み込み、それに応じた値を対応するOutPortから出力する。I2C/SPIについても、まずコンフィギュレーションからいずれかを利用するか、利用するならばそのパラメータを設定する。送信するデータや受信バイト数はInPortから入力し、受信したデータはOutPortから出力される。<br/>pyusb（Mac, Linuxの場合はlibusb）, pyftdiおよびAdafruit Blinkaのインストールが必要。

### Input and Output

InPort<br/>ポート名/型/説明<br/>C7_0out/TimedLong/C7-C0のうち、出力ピンとしているピンからの出力に対応した値。<br/>C7から順に、Highとする場合は1、Lowとする場合は0とした8ビットの値を入力する。<br/>入力ピンとして指定されているピンに対してはどちらを入力しても影響はない。<br/>例えば、C7, C5, C4をHigh、他をLowとする場合には10110000、つまり176を入力する。<br/>D*out/TimedLong/D*を出力ピンとしている場合のピンからの出力に対応した値。<br/>Highとする場合は1を、Lowとする場合は0を入力する。<br/>入力ピンとして指定されている場合はどちらを入力しても影響はない。<br/>I2C_SPIwcommand_rbytes/TimedOctetSeq/I2CもしくはSPI通信で送信するデータ・受信するデータのバイト数。最終要素の前までが送信データ、最終要素が受信バイト数となる。例えば、1,2,3というデータの場合は1,2という2バイトの値をデバイスに送信し、その後3バイトの情報をデバイスから受信する。受信バイト数が0の場合は送信だけを行い、受信を行わない（例: 1,2,0）。受信バイト数のみが指定されている場合（要素が1つの場合）は送信を行わず受信だけを行う（例: 3）。<br/>OutPort<br/>ポート名/型/説明<br/>C7_0in/TimedLong/C7-C0のうち、入力ピンとしているピンへの入力に対応する値。<br/>C7から順に、Highの場合は1、Lowもしくは出力ピンとして指定している場合は0とした8ビットの値が出力される。<br/>例えば、C7, C5, C4がHigh、他がLowもしくは出力ピンである場合には10110000、つまり176が出力される。<br/>全てのピンが出力ピンに指定されている場合は出力を行わない。<br/>D*in/TimedLong/D*を入力ピンとしている場合のピンへの入力に対応する値。<br/>Highの場合は1が、Lowの場合は0が出力される。<br/>出力ピンに指定されている場合は出力を行わない。<br/>I2C_SPIread/TimedOctetSeq/I2CもしくはSPI通信で受信したデータ。

### Algorithm etc



### Basic Information

|  |  |
----|---- 
| Module Name | Adafruit_FT232H_Breakout |
| Description | USB to Digital IO and I2C/SPI components using Adafruit FT232H Breakout |
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
      <td>コンフィギュレーション変数を読み込み、GPIOの各ピンを入力もしくは出力ピンに設定する。また、I2CもしくはSPI通信の設定を行う。</td>
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
      <td>GPIOの全ての出力ピンにLowを出力する。I2CもしくはSPI通信を終了する。</td>
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
      <td>InPortから値を読み込み、GPIOの各出力ピンから値に対応してHighまたはLowを出力する。<br/>GPIO各入力ピンからHighまたはLowを読み込みOutPortから対応する値を出力する。<br/>I2CもしくはSPI通信が設定されている場合は、InPortから読み込んだ値に応じてデバイスへの書き込みやデバイスからの読み込みを行い、OutPortからの出力を行う。</td>
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
      <td>GPIOの全ての出力ピンにLowを出力する。I2CもしくはSPI通信を終了する。</td>
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

#### C7_0out

C7-C0のうち、出力ピンとしているピンからの出力に対応した値。<br/>C7から順に、Highとする場合は1、Lowとする場合は0とした8ビットの値を入力する。<br/>入力ピンとして指定されているピンに対してはどちらを入力しても影響はない。<br/>例えば、C7, C5, C4をHigh、他をLowとする場合には10110000、つまり176を入力する。

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

#### D4out

D4を出力ピンとしている場合のピンからの出力に対応した値。<br/>Highとする場合は1を、Lowとする場合は0を入力する。<br/>入力ピンとして指定されている場合はどちらを入力しても影響はない。

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

#### D5out

D5を出力ピンとしている場合のピンからの出力に対応した値。<br/>Highとする場合は1を、Lowとする場合は0を入力する。<br/>入力ピンとして指定されている場合はどちらを入力しても影響はない。

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

#### D6out

D6を出力ピンとしている場合のピンからの出力に対応した値。<br/>Highとする場合は1を、Lowとする場合は0を入力する。<br/>入力ピンとして指定されている場合はどちらを入力しても影響はない。

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

#### D7out

D7を出力ピンとしている場合のピンからの出力に対応した値。<br/>Highとする場合は1を、Lowとする場合は0を入力する。<br/>入力ピンとして指定されている場合はどちらを入力しても影響はない。

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

#### I2C_SPIwcommand_rbytes

I2CもしくはSPI通信で送信するデータ・受信するデータのバイト数。<br/>最終要素の前までが送信データ、最終要素が受信バイト数となる。例えば、1,2,3というデータの場合は1,2という2バイトの値をデバイスに送信し、その後3バイトの情報をデバイスから受信する。<br/>受信バイト数が0の場合は送信だけを行い、受信を行わない（例: 1,2,0）。<br/>受信バイト数のみが指定されている場合（要素が1つの場合）は送信を行わず受信だけを行う（例: 3）。

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

#### C7_0in

C7-C0のうち、入力ピンとしているピンへの入力に対応する値。<br/>C7から順に、Highの場合は1、Lowもしくは出力ピンとして指定している場合は0とした8ビットの値が出力される。<br/>例えば、C7, C5, C4がHigh、他がLowもしくは出力ピンである場合には10110000、つまり176が出力される。<br/>全てのピンが出力ピンに指定されている場合は出力を行わない。

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

#### D4in

D4を入力ピンとしている場合のピンへの入力に対応する値。<br/>Highの場合は1が、Lowの場合は0が出力される。<br/>出力ピンに指定されている場合は出力を行わない。

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

#### D5in

D5を入力ピンとしている場合のピンへの入力に対応する値。<br/>Highの場合は1が、Lowの場合は0が出力される。<br/>出力ピンに指定されている場合は出力を行わない。

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

#### D6in

D6を入力ピンとしている場合のピンへの入力に対応する値。<br/>Highの場合は1が、Lowの場合は0が出力される。<br/>出力ピンに指定されている場合は出力を行わない。

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

#### D7in

D7を入力ピンとしている場合のピンへの入力に対応する値。<br/>Highの場合は1が、Lowの場合は0が出力される。<br/>出力ピンに指定されている場合は出力を行わない。

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

#### I2C_SPIread

I2CもしくはSPI通信で受信したデータ。

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

#### GPIO_C7_0_IO_select

C7-C0をそれぞれディジタル入力ピンとして使用するか、ディジタル出力ピンとして使用するかを指定する。<br/>C7から順に入力ピンとして指定する場所は1、出力ピンとして使用するところは0とし、それを2進法で表現された数とみなして整数値を入力する。0bや0xを値の前につけることで2進法や16進法で指定することも可能。<br/>例えば、C7,C5,C4を出力ピン、他を入力ピンとする場合は01001111となるため、そのまま2進法で0b01001111としても良いし、16進法に直して0x4f、10進法に直して79としても良い。<br/>アクティブ状態での変更は無効（反映されない）。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>0b11111111</td>
    <td>0b11111111</td>
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

#### GPIO_D7_4_IO_select

D7-D4をそれぞれディジタル入力ピンとして使用するか、ディジタル出力ピンとして使用するかを指定する。<br/>D7から順に入力ピンとして指定する場所は1、出力ピンとして使用するところは0とし、それを2進法で表現された数とみなして整数値を入力する。0bや0xを値の前につけることで2進法や16進法で指定することも可能。<br/>例えば、D7,D5,D4を出力ピン、他を入力ピンとする場合は0100となるため、そのまま2進法で0b0100としても良いし、16進法に直して0x4、10進法に直して4としても良い。<br/>アクティブ状態での変更は無効（反映されない）。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>0b1111</td>
    <td>0b1111</td>
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

#### SPI_baudrate

SPI通信のクロックレート。<br/>アクティブ状態での変更は無効（反映されない）。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">int</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>100000</td>
    <td>100000</td>
  </tr>
  <tr>
    <td>Unit</td>
    <td></td>
    <td>Hz</td>
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

#### SPI_mode

SPI通信のクロックの極性(polarity)と位相(phase)を決定する番号。0の時はいずれも0、1の時は極性が0で位相が1、2の時は極性が1で位相が0、3の時はいずれも1となる。<br/>SPIを使用しない場合はこの設定は無視される。<br/>アクティブ状態での変更は無効（反映されない）。


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
    <td>(0,1,2,3)</td>
    <td>(0,1,2,3)</td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### SPI_cs_pin

SPI通信でCS(chip select)ピンとして利用するピン（BlinkaではCS0(D3)ピンを使用しないため、GPIOの1つをCSピンとして使用する必要がある）。D4～D7の中から1つを選択する。CSピンとして使用されるピンはGPIOの設定(GPIO_D7_4_IO_select)で出力ピンとする必要がある。また、CSピンとして指定したピンに対する入力ポートからの値の変更は無視される。<br/>SPIを使用しない場合はこの設定は無視される。<br/>アクティブ状態での変更は無効（反映されない）。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>D4</td>
    <td>D4</td>
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
    <td>(D4,D5,D6,D7)</td>
    <td>(D4,D5,D6,D7)</td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### SPI_cs_talking

SPI通信での通信時のCS(chip select)ピンの状態。通信時にLowとする場合は0、Highとする場合には1となる。<br/>SPIを使用しない場合はこの設定は無視される。<br/>アクティブ状態での変更は無効（反映されない）。


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

#### SER_select

I2CもしくはSPI通信を使用するか、使用しないかを選択する。I2CかSPIであればそれぞれの通信を使用し、Noneであれば使用しない。<br/>アクティブ状態での変更は無効（反映されない）。


<table>
  <tr>
    <td>DataType</td>
    <td colspan="2">string</td>
  </tr>
  <tr>
    <td>DefaultValue</td>
    <td>None</td>
    <td>None</td>
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
    <td>(None,I2C,SPI)</td>
    <td>(None,I2C,SPI)</td>
  </tr>
  <tr>
    <td>Range</td>
    <td colspan="2"></td>
  </tr>
</table>

#### SER_timeout

I2CもしくはSPI通信においてバスをロックするときの最大待ち時間。この時間を超えてもバスがロックできない場合はエラーとする。<br/>SPIやI2Cを使用しない場合はこの設定は無視される。


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


## Demo

## Requirement

## Setup

### Windows

### Ubuntu

## Usage

## Running the tests

## LICENCE




## References

ライブラリのセットアップについて<br/>https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h


## Author

佐々木毅 (Takeshi SASAKI) <sasaki-t(_at_)ieee.org>
