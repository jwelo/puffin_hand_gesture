import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MoveBot(Node):
    def __init__(self):
        super().__init__('move_bot')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.publish_command)
        self.move_cmd = Twist()
        self.active = False  # Only publish when gesture detected

    def publish_command(self):
        if self.active:
            self.publisher_.publish(self.move_cmd)
            self.get_logger().info(f'Publishing: linear.x={self.move_cmd.linear.x:.2f}, angular.z={self.move_cmd.angular.z:.2f}')

    def set_move(self, linear_x=0.0, angular_z=0.0):
        self.move_cmd.linear.x = linear_x
        self.move_cmd.angular.z = angular_z
        self.active = True

    def stop(self):
        self.set_move(0.0, 0.0)
        self.active = True
