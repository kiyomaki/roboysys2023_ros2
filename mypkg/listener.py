#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2023 Makishi Kiyosawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(
            Int16,
            'countup',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')
        if msg.data % 111 == 0:  # ゾロ目の判定
            self.get_logger().info('Triples!')
            self.destroy_node()  # ゾロ目が出たらノードを終了

def main():
    rclpy.init()
    listener = Listener()
    rclpy.spin(listener)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

