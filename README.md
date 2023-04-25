# rosbridge_client

rosbridge is a server process which connect ROS processes and non-ROS processes.  
This repository demonstrates how to construct a minimum connection using rosbridge.  

## ROS side
```
sudo apt-get install ros-<rosdistro>-rosbridge-suite
source /opt/ros/<rosdistro>/setup.bash
// ROS1
roslaunch rosbridge_server rosbridge_websocket.launch
// ROS2
ros2 launch rosbridge_server rosbridge_websocket_launch.xml
```
and open one more terminal for testing
```
// ROS1
rosrun turtlesim turtlesim_node
// ROS2
ros2 run turtlesim turtlesim_node
```

## non-ROS side
```
pip install roslibpy
pip install keyboard
```
and execute 'main.py'

### commands for search
#### ROS1
```
rosmsg list
rossrv list
rosmsg show <msg>
rossrv show <srv>
rosnode list
rosnode info <node>
rostopic list
rostopic info <topic>
rostopic echo <topic>
```
#### ROS2
```
ros2 interface list
ros2 interface show <msg/srv>
ros2 node list
ros2 node info <node>
ros2 topic list
ros2 topic info <topic>
ros2 topic echo <topic>
```