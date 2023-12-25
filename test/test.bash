#!/bin/bash
# Copyright 2023 Makishi Kiyosawa
# SPDX-License-Identifier: BSD-3-Clause

# ワークスペースのセットアップ
dir=~
[ "$1" != "" ] && dir="$1"
cd $dir/ros2_ws
source install/setup.bash

# ノードの起動とログファイルの設定
ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg_test.log &

# ノードが完全に起動するのを待つ
sleep 5

# テストのタイムアウト設定
timeout=30
elapsed=0

# ログファイルを監視し、ロボットの動作が記録されているかをチェック
while [ $elapsed -lt $timeout ]; do
    if grep -q 'Robot is executing:' /tmp/mypkg_test.log; then
        echo "Test passed: 'Robot is executing' message was detected."
        exit 0
    fi
    sleep 1
    ((elapsed++))
done

echo "Test failed: 'Robot is executing' message was not found after ${timeout} seconds."
exit 1

