#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(
            String, 'countup', self.listener_callback, 10)
        self.numbers = []

    def listener_callback(self, msg):
        count, number = msg.data.split(':')
        number = int(number)
        self.numbers.append(number)

        self.get_logger().info(f'Received: "{number}" at count {count}')

        if number % 111 == 0:
            self.calculate_and_display_statistics()
            self.destroy_node()
            rclpy.shutdown()

    def calculate_and_display_statistics(self):
        if self.numbers:
            avg = sum(self.numbers) / len(self.numbers)
            median = self.calculate_median(self.numbers)
            total = sum(self.numbers)
            max_value = max(self.numbers)
            min_value = min(self.numbers)

            self.get_logger().info(
                f'Statistics - Count: {len(self.numbers)}, '
                f'Average: {avg:.2f}, Median: {median}, '
                f'Max: {max_value}, Min: {min_value}, '
                f'Sum: {total}'
            )

    def calculate_median(self, data):
        data = sorted(data)
        n = len(data)
        if n % 2 == 0:
            mid1 = data[n // 2]
            mid2 = data[n // 2 - 1]
            return (mid1 + mid2) / 2
        else:
            return data[n // 2]

def main():
    rclpy.init()
    listener = Listener()
    rclpy.spin(listener)

if __name__ == '__main__':
    main()

