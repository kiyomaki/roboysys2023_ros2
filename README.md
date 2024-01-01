# ROS2 Countup Publisher with Statistical Analysis

[![test](https://github.com/kiyomaki/roboysys2023_ros2/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/kiyomaki/roboysys2023_ros2/actions/workflows/test.yml)

このROS 2パッケージは、ランダムに生成された数値を使用して統計解析を行う機能を備えています。パッケージには、メッセージを定期的にパブリッシュする `talker` ノードと、これらのメッセージを受け取り統計情報を計算する `listener` ノードが含まれています。 `talker` ノードはカウントとランダムな数値を組み合わせたメッセージを `countup` トピックにパブリッシュし、`listener` ノードはこのトピックからメッセージを受け取り、データの統計的傾向を分析します。

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

以下は `launch` ファイルのコマンドを使用して `talker` および `listener` ノードを実行した際の出力例です。
   ```
   [INFO] [launch]: Default logging verbosity is set to INFO
   [INFO] [talker-1]: process started with pid [1075]
   [INFO] [listener-2]: process started with pid [1077]
   [listener-2] [INFO] [1704095987.633712183] [listener]: Received: "164" at count 1
   [listener-2] [INFO] [1704095988.119657203] [listener]: Received: "309" at count 2
   [listener-2] [INFO] [1704095988.619007484] [listener]: Received: "850" at count 3
   ,,,(省略),,,
   [listener-2] [INFO] [1704096027.620142934] [listener]: Received: "899" at count 81
   [listener-2] [INFO] [1704096028.120085688] [listener]: Received: "666" at count 82
   [listener-2] [INFO] [1704096028.121525863] [listener]: Statistics - Count: 82, Average: 551.93, Median: 585.0, Max: 994, Min: 113, Sum: 45258
   [talker-1] [INFO] [1704096028.150836400] [talker]: Triples! at count 82

   ```

## ノードとトピックの概要

- **Talker** (`talker`): 0.5秒ごとに、連番とランダムな数値（100〜999の範囲）を含むメッセージを生成し、 `countup` トピックにパブリッシュします。

- **Listener** (`listener`): `countup` トピックからメッセージを受け取り、受信したメッセージの数値とカウントをログに出力します。また、ランダム数値が111で割り切れる場合に、受け取ったデータの平均、中央値、最大値、最小値、合計を計算し、統計的な洞察を提供します。

- **トピック** (`countup`): `String` 型のメッセージを使用し、`talker` ノードからパブリッシュされるメッセージを含みます。各メッセージはカウントとランダムな数値を含んでいます。

## ライセンス・著作権

- このソフトウェアは3条項BSDライセンスの下で再頒布および使用が許可されています。
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。
  [Ryuichi Ueda's slides](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
- © 2023 Makishi Kiyosawa


