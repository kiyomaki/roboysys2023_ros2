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
timeout=300
elapsed=0

# ログファイルを監視し、特定のメッセージが現れるかをチェック
while [ $elapsed -lt $timeout ]; do
    if grep -q 'Triples! at count' /tmp/mypkg_test.log; then
        echo "Test passed: 'Triples! at count' message was detected."
        # 統計情報の確認
        if grep -q 'Statistics - Count' /tmp/mypkg_test.log &&
           grep -q 'Average:' /tmp/mypkg_test.log &&
           grep -q 'Median:' /tmp/mypkg_test.log &&
           grep -q 'Max:' /tmp/mypkg_test.log &&
           grep -q 'Min:' /tmp/mypkg_test.log &&
           grep -q 'Sum:' /tmp/mypkg_test.log; then
            echo "Test passed: Statistical information was found."
        else
            echo "Test failed: Statistical information was not found."
        fi
        exit 0
    fi
    sleep 1
    ((elapsed++))
done

echo "Test failed: 'Triples! at count' message was not found after ${timeout} seconds."
exit 1

