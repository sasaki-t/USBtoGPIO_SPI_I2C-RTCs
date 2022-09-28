# USBtoGPIO_SerialCommunication-RTCs
Adafruit FT232H BreakoutおよびAdafruit MCP2221A Breakoutを使用したUSB-GPIO, SPI, I<sup>2</sup>C, UART変換コンポーネントとその利用例を提供するOpenRTM-aist用コンポーネント群です。

A USB to GPIO, SPI, I<sup>2</sup>C, UART components and sample components for OpenRTM-aist using an Adafruit FT232H breakout and Adafruit MCP2221A breakout boards  

# 概要
## 開発の背景
ロボットシステムやRTシステムでは、センサやLEDといった電子部品や、モータなどのアクチュエータを利用した開発が行われます。
このような場合にはGPIO(General Purpose Input/Output)ポートや、SPIやI<sup>2</sup>C, UART通信といったシリアル通信インタフェースが必要となるため、PCに加えてRaspberry PiやArduinoといったワンボードコンピュータやワンボードマイコンを利用してRTコンポーネントの開発を行う必要がありました。そこで、USBポートを介してGPIOやシリアル通信機能を利用することができる変換ボードをコンポーネント化しました。

開発したUSB-GPIO, SPI, I<sup>2</sup>C変換コンポーネントおよびUSB-GPIO, I<sup>2</sup>C, UART変換コンポーネントにはそれぞれ以下のような機能があります。
- USB-GPIO, SPI, I<sup>2</sup>C変換コンポーネント
	- ディジタル入出力機能（入力・出力はピンごとに選択可能）
	- シリアル通信（I<sup>2</sup>C, SPI）機能
- USB-GPIO, I<sup>2</sup>C, UART変換コンポーネント
	- ディジタル/アナログ入出力機能（入力・出力はピンごとに選択可能）
	- シリアル通信（I<sup>2</sup>C, UART）機能

いずれの機能についても設定はConfigurationから行うことができ、またデータは全てコンポーネントの入出力ポートを通してやり取りできるため、プログラムの記述やマイコンへの書き込みを行うことなくこれらの機能を利用することができます。
また、様々なOS(Windows, macOS, Linux)で利用することが可能です。

## コンポーネント群
- USB-GPIO, シリアル通信変換コンポーネント群
	- USB-GPIO, SPI, I<sup>2</sup>C変換コンポーネント(Adafruit_FT232H_Breakout)
		- Adafruit FT232H BreakoutボードをPCにUSB接続することでGPIOやSPI, I<sup>2</sup>C通信を使用可能にするコンポーネント。
	- USB-GPIO, I<sup>2</sup>C, UART変換コンポーネント(Adafruit_MCP2221A_Breakout)
		- Adafruit MCP2221A BreakoutボードをPCにUSB接続することでGPIOやI<sup>2</sup>C, UART通信を使用可能にするコンポーネント。
- GPIOの利用例で使用するコンポーネント群
	- 入力データ変化カウントコンポーネント(CountChange)
		- 入力値が1つ前の入力値と比べ指定の変化をするたびに出力値が増加するコンポーネント。
	- Lookup Tableコンポーネント(ConfigLUT)
		- Configurationに列挙した値のうちの1つを入力値に応じて出力する1次元のLookup Table(LUT)コンポーネント。
- シリアル通信の利用例で使用するコンポーネント群
	- OctetSeqデータ出力コンポーネント(SendOctetSeq)
		- コンソールから入力した値をTimedOctetSeq型のデータとして出力するコンポーネント。
	- 気圧・温湿度センサ計算コンポーネント(BME280Decode)
		- 気圧・温湿度センサBME280からシリアル通信で得られた計測値（バイト列）を、気圧、温度、湿度の値に変換して出力するコンポーネント。

## 利用ハードウェア
- USB-GPIO, SPI, I<sup>2</sup>C変換ボード: [Adafruit FT232H Breakoutボード](https://learn.adafruit.com/adafruit-ft232h-breakout)
- USB-GPIO, I<sup>2</sup>C, UART変換ボード: [Adafruit MCP2221A Breakoutボード](https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-mcp2221)

## 依存ライブラリ
- Adafruit_FT232H_Breakout
	- pyusb（Windowsの場合）, libusb（macOS, Linuxの場合）
	- [pyftdi](https://eblot.github.io/pyftdi/)
	- [Adafruit Blinka](https://pypi.org/project/Adafruit-Blinka/)
- Adafruit_MCP2221A_Breakout
	- libusb（Linuxの場合）, libudev（Linuxの場合）
	- hidapi
	- pyserial
	- [Adafruit Blinka](https://pypi.org/project/Adafruit-Blinka/)

# 利用方法
Adafruit_FT232H_Breakout, Adafruit_MCP2221A_Breakoutの基本的な使用手順を説明します。
コンポーネントの仕様、使い方の詳細に関しましては付属のマニュアルに記述されておりますのでそちらをご覧ください。

## 使用前の準備
### Adafruit_FT232H_Breakoutの使用準備
Adafruit_FT232H_Breakoutの使用にあたり、事前にソフトウェアのインストールなどの準備が必要となります。
OSごとの概要は下記のとおりですが、詳細は[公式サイトの手順](https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h/setup)を参照してください。
- Windowsの場合
	1. FT232Hのドライバーを更新する
	2. pyftdiとpyusbをインストールする
	3. Adafruit Blinkaをインストールする
- macOS の場合
	1. libusbをインストールする
	2. pyftdiとAdafruit Blinkaをインストールする
- Linuxの場合
	1. libusbをインストールする
	2. udev rulesファイルを作成する
	3. pyftdiとAdafruit Blinka をインストールする

### Adafruit_MCP2221A_Breakoutの使用準備
Adafruit_MCP2221A_Breakoutの使用にあたり、事前にソフトウェアのインストールなどの準備が必要となります。
OSごとの概要は下記のとおりですが、詳細は[公式サイトの手順](https://learn.adafruit.com/circuitpython-libraries-on-any-computer-with-mcp2221/setup)を参照してください。
- Windows, macOSの場合
	1. hidapiをインストールする
	2. Adafruit Blinkaをインストールする
	3. pyserialをインストールする
- Linuxの場合
	1. libusb, libudevをインストールする
	2. hidapiをインストールする
	3. Adafruit Blinkaをインストールする
	4. pyserialをインストールする

## 使用手順
### Adafruit_FT232H_Breakoutの使用手順
1. （コンポーネント実行前の準備）
	- Adafruit FT232H Breakoutボードが新しいタイプ（コネクタがUSB Type-Cのもの)の場合、I<sup>2</sup>C通信を使うならボードのI<sup>2</sup>C Modeスイッチをオンに、SPI通信を使うならオフにする
	- 入出力の対象となる回路を作成し、Adafruit FT232H Breakoutボードの各ピンに接続する
	- Adafruit FT232H BreakoutボードとPCをUSBで接続する
1. Configurationを設定する
	- シリアル通信（I<sup>2</sup>CもしくはSPI通信）を利用するか、利用する場合はどちらを利用するのかをSER_selectで指定する
	- GPIOを利用する場合は、GPIO_C7_0_IO_selectとGPIO_D7_4_IO_selectで各ピンをそれぞれディジタル入力ピンとして使用するか、ディジタル出力ピンとして使用するかを指定する。SPI通信を利用する場合はCS (chip select)ピンをSPI_cs_pinで指定し、GPIO_D7_4_IO_select設定時にそのピンは出力ピンに指定する
	- I<sup>2</sup>C通信を利用する場合はI2C_device_addressでデバイスの7ビットアドレスを、SPI通信を利用する場合はSPI_baudrate, SPI_mode, SPI_cs_talkingで通信パラメータを設定する
1. コンポーネントをアクティブ化する
1. InPort, OutPortを他のコンポーネントに接続し、システムを拡張していく

### Adafruit_MCP2221A_Breakoutの使用手順
1. （コンポーネント実行前の準備）
	- 入出力の対象となる回路を作成し、Adafruit MCP2221A Breakoutボードの各ピンに接続する
	- Adafruit MCP2221A BreakoutボードとPCをUSBで接続する
1. Configurationを設定する
	- GPIOを利用する場合は、GPIO_G0_select～GPIO_G3_selectで各ピンの利用方法（アナログ/ディジタル、入力/出力）を指定する
	- シリアル通信（I<sup>2</sup>CおよびUART通信）を利用するかをそれぞれI2C_use, UART_useで指定する
	- I<sup>2</sup>C通信を利用する場合はI2C_device_addressでデバイスの7ビットアドレスを、UART通信を利用する場合はUART_port, UART_baudrate, UART_read_timeoutで通信パラメータを設定する
1. コンポーネントをアクティブ化する
1. InPort, OutPortを他のコンポーネントに接続し、システムを拡張していく


## 使用例
Adafruit_FT232H_Breakoutについて、GPIO, シリアル通信機能それぞれの使用例の動画を公開しています。  
https://www.youtube.com/watch?v=tZ5US8G4aX8
