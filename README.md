# ROS2 Triples Package

## 概要
このROS 2パッケージは、メッセージを定期的にパブリッシュする `talker` ノードと、これらのメッセージを受け取る `listener` ノードを含んでいます。 `talker` ノードは、カウントとランダムな数値を組み合わせたメッセージを生成し、 `countup` トピックにパブリッシュします。 `listener` ノードはこのトピックからメッセージを受け取り、ログにその内容とカウントを出力します。

[![test](https://github.com/kiyomaki/roboysys2023_ros2/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/kiyomaki/roboysys2023_ros2/actions/workflows/test.yml)

## 動作環境

このパッケージは、下記の環境での動作が確認されています。
- OS: Ubuntu 22.04 LTS
- ROS2バージョン: Humble Hawksbill

## 使用方法

ROS 2がインストールされている環境で、以下の手順に従ってパッケージを使用します：

1. ソースコードをROS 2ワークスペースにクローンします。
- githubアカウントがある場合
   ```
   git clone git@github.com:kiyomaki/robosys2023_ros2.git
   cd ~/ros2_ws/src
   ```

- githubアカウントがない場合
   ```
   git clone https://github.com:kiyomaki/robosys2023_ros2
   cd ~/ros2_ws/src
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

## ノードとトピックの概要

- **Talker** (`talker`): 0.5秒ごとに、連番とランダムな数値（100〜999の範囲）を含むメッセージを生成し、 `countup` トピックにパブリッシュします。ランダムな数値が111で割り切れる場合、ノードはログに `'Triples! at count [カウント数]'` と出力し、シャットダウンします。
- **Listener** (`listener`): `countup` トピックからメッセージを受け取り、受信したメッセージの数値とカウントをログに出力します。受信した数値が111で割り切れる場合、ノードはログに同様のメッセージを出力し、シャットダウンします。
- **トピック** (`countup`) : `String` 型のメッセージを使用し、 `talker` ノードからパブリッシュされるメッセージを含みます。各メッセージはカウントとランダムな数値を含んでいます。

## ライセンス・著作権

- © 2023 Makishi Kiyosawa
- このソフトウェアは3条項BSDライセンスの下で再頒布および使用が許可されています。
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。
 - https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022
