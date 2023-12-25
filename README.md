# ROS2 Robot Simulation commands

[![test](https://github.com/kiyomaki/roboysys2023_ros2/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/kiyomaki/roboysys2023_ros2/actions/workflows/test.yml)

  このROS 2パッケージは、シンプルなロボットの動作をシミュレートする `talker` ノードと `listener` ノードを含んでいます。
 
  `talker` ノードはランダムな動作コマンド（前進、後退、左回転、右回転など）を生成し、`robot_commands` トピックにパブリッシュします。`listener` ノードはこのトピックからコマンドを受け取り、GUI上でロボットの動きをシミュレートします。

## 動作環境

このパッケージは、下記の環境での動作が確認されています。
- OS: Ubuntu 22.04 LTS
- ROS2バージョン: Humble Hawksbill

## 使用方法

ROS 2がインストールされている環境で、以下の手順に従ってパッケージを使用します：

1. ソースコードをROS 2ワークスペースに`clone`します。
   ```
   cd ~/ros2_ws/src
   git clone https://github.com:kiyomaki/robosys2023_ros2
   ```

2. ワークスペースに移動し、ビルドします。
   ```
   cd ~/ros2_ws
   colcon build
   ```

3. `talker` および `listener` ノードを実行するには、以下の `launch` ファイルのコマンドを使用します。
   ```
   ros2 launch mypkg talk_listen.launch.py
   ```

## 実行例
以下は`launch`ファイルのコマンドを使用し、`talker`および`listener`ノードを実行した際の出力例です。
   ```
   [INFO] [launch]: Default logging verbosity is set to INFO
   [INFO] [talker-1]: process started with pid [4178]
   [INFO] [listener-2]: process started with pid [4180]
   [listener-2] [INFO] [1703109098.693587310] [listener]: Robot is executing: forward
   [listener-2] [INFO] [1703109099.188154957] [listener]: Robot is executing: turn_left
   [listener-2] [INFO] [1703109099.688553699] [listener]: Robot is executing: turn_right
   ...（中略）...
   [listener-2] [INFO] [1703109120.689886059] [listener]: Robot is executing: stop

   ```
## ノードとトピックの概要

- **Talker** (`talker`): このノードはランダムなロボットの動作コマンドを生成し、`robot_commands` トピックにパブリッシュします。

- **Listener** (`listener`): `robot_commands` トピックからコマンドを受け取り、Tkinterウィンドウ上でロボットの動きをシミュレートします。

- **トピック** (`robot_commands`): `String` 型のメッセージを使用し、`talker` ノードからパブリッシュされるコマンドを含みます。

## ライセンス・著作権

- このソフトウェアは3条項BSDライセンスの下で再頒布および使用が許可されています。
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。
  https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022
- © 2023 Makishi Kiyosawa
