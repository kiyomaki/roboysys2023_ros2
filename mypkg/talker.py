#!/usr/bin/env python3
# Copyright 2023 Makishi Kiyosawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(String, 'countup', 10)
        self.count = 0
        self.create_timer(0.5, self.cb)

    def cb(self):
        self.count += 1
        random_number = random.randint(100, 999)
        msg = String()
        msg.data = f'{self.count}:{random_number}'
        self.pub.publish(msg)

        if random_number % 111 == 0:
            self.get_logger().info(f'ゾロ目！{self.count}回目')
            self.destroy_node()
            rclpy.shutdown()

def main():
    rclpy.init()
    talker = Talker()
    rclpy.spin(talker)

if __name__ == '__main__':
    main()

