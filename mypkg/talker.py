#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2023 Makishi Kiyosawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import random

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.create_timer(0.5, self.cb)

    def cb(self):
        msg = Int16()
        msg.data = random.randint(100, 999)  # 3桁のランダムな数字を生成
        self.pub.publish(msg)

        if msg.data % 111 == 0:  # ゾロ目の判定
            self.get_logger().info('Triples!')
            self.destroy_node()  # ゾロ目が出たらノードを終了

def main():
    rclpy.init()
    talker = Talker()
    rclpy.spin(talker)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

