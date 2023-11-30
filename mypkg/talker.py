#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.n = 0
        self.create_timer(0.5, self.cb)

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1

def main():
    rclpy.init()
    talker = Talker()  # Talker インスタンスの作成
    rclpy.spin(talker)  # Talker インスタンスを spin に渡す
    rclpy.shutdown()

if __name__ == '__main__':
    main()

