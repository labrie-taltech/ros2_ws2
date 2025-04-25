def setup_initial_pose(self):
    initial_pose = PoseWithCovarianceStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.pose.pose.position.x = 3737.406
    initial_pose.pose.pose.position.y = 73728.133
    initial_pose.pose.pose.orientation.z = -0.966
    initial_pose.pose.pose.orientation.w = 0.258
    self.initial_pose_publisher.publish(initial_pose)

def setup_goals(self):
    self.goal_poses = [
    {'x': 3694.478, 'y': 73729.523, 'xx': 0.0, 'yy': 0.0, 'zz':0.862, 'w': 0.505},
    {'x': 3766.84, 'y': 73796.742, 'xx': 0.0, 'yy': 0.0, 'zz':0.268, 'w': 0.963},
    {'x': 3827.455, 'y': 73724.625, 'xx': 0.0, 'yy': 0.0, 'zz':-0.969, 'w': 0.246},
    ]
    self.publish_goal()

def publish_goal(self):
    goal = self.goal_poses[self.current_goal_index]
    pose_msg = PoseStamped()
    pose_msg.header.frame_id = 'map'
    pose_msg.pose.position.x = goal['x']
    pose_msg.pose.position.y = goal['y']
    pose_msg.pose.orientation.z = goal['zz']
    pose_msg.pose.orientation.w = goal['w']
    self.goal_pose_publisher.publish(pose_msg)
    self.get_logger().info(f"Published goal:{self.current_goal_index}")

