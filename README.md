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
   [INFO] [talker-1]: process started with pid [1075]
   [INFO] [listener-2]: process started with pid [1077]
   [listener-2] [INFO] [1703090915.388954260] [listener]: Received: "729" at count 1
   [listener-2] [INFO] [1703090915.880331977] [listener]: Received: "388" at count 2
   [listener-2] [INFO] [1703090916.381651076] [listener]: Received: "385" at count 3
   ...（中略）...
   [listener-2] [INFO] [1703090922.381005589] [listener]: Received: "555" at count 15
   [listener-2] [INFO] [1703090922.381614854] [listener]: Triples! at count 15
   [talker-1] [INFO] [1703090922.388203096] [talker]: Triples! at count 15

   ```
## ノードとトピックの概要

- **Talker** (`talker`): 0.5秒ごとに、連番とランダムな数値（100〜999の範囲）を含むメッセージを生成し、 `countup` トピックにパブリッシュします。ランダムな数値が111で割り切れる場合、ノードはログに `'Triples! at count [カウント数]'` と出力し、シャットダウンします。
- **Listener** (`listener`): `countup` トピックからメッセージを受け取り、受信したメッセージの数値とカウントをログに出力します。受信した数値が111で割り切れる場合、ノードはログに同様のメッセージを出力し、シャットダウンします。
- **トピック** (`countup`) : `String` 型のメッセージを使用し、 `talker` ノードからパブリッシュされるメッセージを含みます。各メッセージはカウントとランダムな数値を含んでいます。

## ライセンス・著作権

- このソフトウェアは3条項BSDライセンスの下で再頒布および使用が許可されています。
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。
  https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022
- © 2023 Makishi Kiyosawa
