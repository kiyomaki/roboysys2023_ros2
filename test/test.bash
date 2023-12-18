#!/bin/bash

# ワークスペースのセットアップ
dir=~
[ "$1" != "" ] && dir="$1"
cd $dir/ros2_ws
source install/setup.bash

# ノードの起動とログファイルの設定
ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg_test.log &

# ノードが完全に起動するのを待つ
sleep 5

# 1分間待機
sleep 60

# ログファイルの内容を表示（デバッグ用）
echo "Log file contents:"
cat /tmp/mypkg_test.log
echo "End of log file contents"

# ログファイルを確認し、特定のメッセージが現れるかをチェック
if grep -q 'Triples! at count' /tmp/mypkg_test.log; then
    echo "Test passed: 'Triples! at count' message was detected."
    exit 0
else
    echo "Test failed: 'Triples! at count' message was not found."
    exit 1
fi

