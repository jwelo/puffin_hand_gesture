import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/user/hand_gesture_robot/turtlebot_ws/install/turtlebot3_mover'
