import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MoveBot(Node):
    def __init__(self):
        super().__init__('move_bot')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.move_cmd = Twist()
        self.move_cmd.linear.x = 0.2
        self.move_cmd.angular.z = 0.0

    def timer_callback(self):
        self.publisher_.publish(self.move_cmd)
        self.get_logger().info('Publishing: linear.x=%.2f angular.z=%.2f' %
                               (self.move_cmd.linear.x, self.move_cmd.angular.z))

def main(args=None):
    rclpy.init(args=args)
    node = MoveBot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
