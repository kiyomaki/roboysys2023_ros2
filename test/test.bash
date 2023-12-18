#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"   # 引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/ros2_ws/install/setup.bash

# 'ros2 launch' をバックグラウンドで実行
ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log &

# ログファイルを監視し、'Triples!' メッセージが現れたら終了
while :
do
    if grep -q 'Triples!' /tmp/mypkg.log; then
        echo "Test passed: 'Triples!' message was received."
        break
    fi
    sleep 1  # CPU使用率を抑えるために短い休憩を挟む
done

# バックグラウンドプロセスの終了
kill %1

