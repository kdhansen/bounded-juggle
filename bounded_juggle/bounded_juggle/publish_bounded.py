import rclpy
from rclpy.node import Node

from bounded_interfaces.msg import BoundedNumbers, Numbers

import random


class BoundedPublisher(Node):

    def __init__(self):
        super().__init__('bounded_publisher')
        self.bounded_publisher_ = self.create_publisher(BoundedNumbers, 'bounded_numbers', 10)
        self.unbounded_publisher_ = self.create_publisher(Numbers, 'numbers', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        bounded_msg = BoundedNumbers()
        unbounded_msg = Numbers()
        for i in range(5):
            random_offset = random.randint(0, 5)
            bounded_msg.numbers.append(i + random_offset)
            unbounded_msg.numbers.append(i + random_offset)
        self.bounded_publisher_.publish(bounded_msg)
        self.unbounded_publisher_.publish(unbounded_msg)


def main(args=None):
    rclpy.init(args=args)

    publisher = BoundedPublisher()

    rclpy.spin(publisher)

    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()