#!/usr/bin/env python3
# Copyright 2023 Makishi Kiyosawa
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class Talker(Node):
    def __init__(self):
        super().__init__('command_talker')
        self.publisher = self.create_publisher(String, 'robot_commands', 10)
        self.timer = self.create_timer(1.0, self.publish_command)

    def publish_command(self):
        commands = ['forward', 'backward', 'turn_left', 'turn_right', 'stop']
        command = random.choice(commands)
        msg = String()
        msg.data = command
        self.publisher.publish(msg)
        self.get_logger().info(f'Sending Command: {command}')

def main(args=None):
    rclpy.init(args=args)
    talker = Talker()
    rclpy.spin(talker)
    talker.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

