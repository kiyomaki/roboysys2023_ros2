#!/usr/bin/env python3
# Copyright 2023 Makishi Kiyosawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(
            String,
            'countup',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        count, number = msg.data.split(':')
        number = int(number)
        self.get_logger().info(f'Received: "{number}" {count}回目')

        if number % 111 == 0:
            self.get_logger().info(f'ゾロ目！ {count}回目')
            self.destroy_node()
            rclpy.shutdown()

def main():
    rclpy.init()
    listener = Listener()
    rclpy.spin(listener)

if __name__ == '__main__':
    main()

