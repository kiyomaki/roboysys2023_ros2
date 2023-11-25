1 #!/bin/bash
2
3 dir=~
4 [ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。
5
6 cd $dir/ros2_ws
7 colcon build
8 source $dir/.bashrc
9 timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log
10
11 cat /tmp/mypkg.log |
12 grep 'Listen: 10'
