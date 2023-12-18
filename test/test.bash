#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/ros2_ws/install/setup.bash

ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log &

timeout=300  # 5分のタイムアウト
elapsed=0

while [ $elapsed -lt $timeout ]; do
    if grep -q 'ゾロ目！' /tmp/mypkg.log; then
        echo "Test passed: 'ゾロ目！' message was received."
        kill %1
        exit 0
    fi
    sleep 1
    ((elapsed++))
done

echo "Test failed: Timed out after ${timeout} seconds."
kill %1
exit 1

