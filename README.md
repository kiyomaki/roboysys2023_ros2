# ROS2 Countup Publisher

[![test](https://github.com/kiyomaki/roboysys2023_ros2/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/kiyomaki/roboysys2023_ros2/actions/workflows/test.yml)

このROS 2パッケージは、メッセージを定期的にパブリッシュする `talker` ノードと、これらのメッセージを受け取る `listener` ノードを含んでいます。 `talker` ノードは、カウントとランダムな数値を組み合わせたメッセージを生成し、 `countup` トピックにパブリッシュします。 `listener` ノードはこのトピックからメッセージを受け取り、ログにその内容とカウントを出力します。

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
   [listener-2] [INFO] [1703109098.693587310] [listener]: Received: "547" at count 1
   [listener-2] [INFO] [1703109099.188154957] [listener]: Received: "799" at count 2
   [listener-2] [INFO] [1703109099.688553699] [listener]: Received: "430" at count 3
   ...（中略）...
   [listener-2] [INFO] [1703109120.689886059] [listener]: Received: "444" at count 45
   [listener-2] [INFO] [1703109120.690689903] [listener]: Statistics - Count: 45, Average: 570.53, Med   ian: 568, Max: 997, Min: 106, Sum: 25674
   [talker-1] [INFO] [1703109120.697894380] [talker]: Triples! at count 45

   ```
## ノードとトピックの概要

- **Talker** (`talker`): 0.5秒ごとに、連番とランダムな数値（100〜999の範囲）を含むメッセージを生成し、 `countup` トピックにパブリッシュします。ランダムな数値が111で割り切れる場合（ゾロ目の場合）、ノードはログに `'Triples! at count [カウント数]'` と出力し、シャットダウンします。

- **Listener** (`listener`): `countup` トピックからメッセージを受け取り、受信したメッセージの数値とカウントをログに出力します。受信した数値が111で割り切れる場合（ゾロ目の場合）、ノードは平均、中央値、最大値、最小値、合計の統計情報を計算し、ログに出力してからシャットダウンします。これにより、ゾロ目が出るまでに生成されたデータの統計的傾向を理解することができます。

- **トピック** (`countup`): `String` 型のメッセージを使用し、`talker` ノードからパブリッシュされるメッセージを含みます。各メッセージはカウントとランダムな数値を含んでいます。

## ライセンス・著作権

- このソフトウェアは3条項BSDライセンスの下で再頒布および使用が許可されています。
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。
  https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022
- © 2023 Makishi Kiyosawa
