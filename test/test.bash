#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/ros2_ws/install/setup.bash

# 'ros2 launch' をバックグラウンドで実行
ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log &

# タイムアウト設定
timeout=300
elapsed=0

while [ $elapsed -lt $timeout ]; do
    # ログファイルの内容をチェック
    if cat /tmp/mypkg.log | grep -q 'Triples! at count'; then
        echo "Test passed: 'Triples! at count' message was received."
        kill %1
        exit 0
    fi
    sleep 1
    ((elapsed++))
done

echo "Test failed: Timed out after ${timeout} seconds."
kill %1
exit 1

