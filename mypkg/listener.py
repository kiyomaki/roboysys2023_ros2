#!/usr/bin/env python3
# Copyright 2023 Makishi Kiyosawa
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import tkinter as tk
import threading

class RobotSimulator:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.robot = self.canvas.create_rectangle(180, 180, 220, 220, fill="blue")

    def move_robot(self, command):
        if command == 'forward':
            self.canvas.move(self.robot, 0, -10)
        elif command == 'backward':
            self.canvas.move(self.robot, 0, 10)
        elif command == 'turn_left':
            self.canvas.move(self.robot, -10, 0)
        elif command == 'turn_right':
            self.canvas.move(self.robot, 10, 0)

class Listener(Node):
    def __init__(self, simulator):
        super().__init__('robot_listener')
        self.subscription = self.create_subscription(
            String, 'robot_commands', self.execute_command, 10)
        self.simulator = simulator

    def execute_command(self, msg):
        command = msg.data
        self.simulator.move_robot(command)
        # コマンド実行時のログメッセージを追加
        self.get_logger().info(f'Robot is executing: {command}')

def main(args=None):
    rclpy.init(args=args)
    root = tk.Tk()
    simulator = RobotSimulator(root)
    listener = Listener(simulator)

    def spin():
        rclpy.spin(listener)
        listener.destroy_node()
        rclpy.shutdown()

    spin_thread = threading.Thread(target=spin)
    spin_thread.start()

    root.mainloop()
    spin_thread.join()

if __name__ == '__main__':
    main()

