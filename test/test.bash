#!/bin/bash

# ワークスペースのセットアップ
dir=~
[ "$1" != "" ] && dir="$1"
cd $dir/ros2_ws
sudo rosdep fix-permissions
source source /opt/ros/humble/setup.bash

# ノードの起動とログファイルの設定
ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg_test.log &

# テストのタイムアウト設定
timeout=300
elapsed=0

# ログファイルを監視し、特定のメッセージが現れるかをチェック
while [ $elapsed -lt $timeout ]; do
    if grep -q 'Triples! at count' /tmp/mypkg_test.log; then
        echo "Test passed: 'Triples! at count' message was detected."
        exit 0
    fi
    sleep 1
    ((elapsed++))
done

echo "Test failed: Timed out after ${timeout} seconds."
exit 1

