from roslibpy import *

class RosBridgeClient:

  def __init__(self, host:str='127.0.0.1', port:int=9090):
    self.client = Ros(host, port)
    self.client.run()
    self.topics = []

  def __del__(self):
    self.client.close()
  
  def __enter__(self, host:str='127.0.0.1', port:int=9090):
    self.__init__(host, port)
    return self
  
  def __exit__(self, exc_type, exc_value, traceback):
    self.__del__()
    return True

  def add_topic(self, topic:str, type:str) -> Topic:
    topic = Topic(self.client, topic, type)
    self.topics.append(topic)
    return topic
  

# sample code
from keyboard import *

if __name__ == '__main__':
  with RosBridgeClient() as ros:

    # define callback function for subscription in advance or use lambda function directly

    sub1 = ros.add_topic('rosout', 'rosgraph_msgs/Log') # ROS1
    #sub1 = ros.add_topic('rosout', 'rcl_interfaces/msg/Log') # ROS2
    sub1.subscribe(lambda x: print(x))

    sub2 = ros.add_topic('turtle1/pose', 'turtlesim/Pose') # ROS1
    #sub2 = ros.add_topic('turtle1/pose', 'turtlesim/msg/Pose') # ROS2
    sub2.subscribe(lambda x: print(x))

    # use multi-threading if you need parallel-publishing
    pub = ros.add_topic('turtle1/cmd_vel', 'geometry_msgs/Twist') # ROS1
    #pub = ros.add_topic('turtle1/cmd_vel', 'geometry_msgs/msg/Twist') # ROS2

    while True:
      key = read_key()
      x = 0
      y = 0
      if (key == 'esc'): break
      elif (key == 'left'): x -= 1
      elif (key == 'right'): x += 1
      elif (key == 'up'): y += 1
      elif (key == 'down'): y -= 1
      msg = Message({
        'linear': { 'x': x, 'y': y, 'z': 0 },
        'angular': { 'x': 0, 'y': 0, 'z': 0 }
      })
      pub.publish(msg)
