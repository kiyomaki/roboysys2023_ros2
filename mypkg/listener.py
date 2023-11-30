#!/usr/bin/env python3
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
        if msg.data == 10:
            self.get_logger().info('Listen: 10')
        else:
            self.get_logger().info('Received: "{}"'.format(msg.data))

def main():
    rclpy.init()
    listener = Listener()
    rclpy.spin(listener)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

