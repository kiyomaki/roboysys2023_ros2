#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"   # 引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/ros2_ws/install/setup.bash

# 'ros2 launch' をバックグラウンドで実行
ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log &

# ログファイルを監視し、'Triples!' メッセージが現れたら終了
timeout=300  # 5分のタイムアウト
elapsed=0

while [ $elapsed -lt $timeout ]; do
    if grep -q 'Triples! at count' /tmp/mypkg.log; then
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

