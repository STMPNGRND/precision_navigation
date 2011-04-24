#! /usr/bin/env python
import roslib
roslib.load_manifest('precision_steering')
import rospy

from std_msgs.msg import String
from precision_navigation_msgs.msg import Path
from precision_navigation_msgs.msg import PathSegment


def makeDummyPaths():
	paths = {}
	p1 = Path()
	p = PathSegment()
	p.frame_id = "map"
	p.segType = 1
	p.xRef = 0.0436
	p.yRef = 2.18822
	p.tangentAng = 2.42426
	p.rho = 0.0
	p.length = 2.3202
	p.vDes = 0.5
	p.accel = 0.1
	p1.segs.append(p)

	p = PathSegment()
	p.frame_id = "map"
	p.segType = 2
	p.xRef = -1.6972
	p.yRef = 3.70692
	p.tangentAng = 2.42426
	p.rho = -100.0
	p.length = 0.0157
	p.vDes = 0.005
	p.accel = 0.05
	p1.segs.append(p)

	p = PathSegment()
	p.frame_id = "map"
	p.segType = 1
	p.xRef = -1.7532
	p.yRef = 3.847
	p.tangentAng = 0.8272
	p.rho = 0.0
	p.length = 13.0
	p.vDes = 0.5
	p.accel = 0.1
	p1.segs.append(p)
	paths['hallway'] = p1

	# start path to elevator
	p2 = Path()
	p = PathSegment()
	p.frame_id = "map"
	p.segType = 1
	p.xRef = 7.0274
	p.yRef = 13.4659
	p.tangentAng = 0.7121
	p.rho = 0.0
	p.length = 1.7752
	p.vDes = 0.5
	p.accel = 0.2
	p2.segs.append(p)

	p = PathSegment()
	p.frame_id = "map"
	p.segType = 2
	p.xRef = 7.6093
	p.yRef = 15.5085
	p.tangentAng = 0.7121
	p.rho = 0.8576
	p.length = 1.8316
	p.vDes = 0.4
	p.accel = 0.2
	p2.segs.append(p)
	paths['elevator'] = p2

	# start go to bathroom
	p3 = Path()
	p = PathSegment()
	p.frame_id = "map"
	p.segType = 2
	p.xRef = 8.4844
	p.yRef = 16.2639
	p.tangentAng =  2.2829
	p.rho = 100.0
	p.length = 0.0157 
	p.vDes = 0.008
	p.accel = 0.02
	p3.segs.append(p)

	p = PathSegment()
	p.frame_id = "map"
	p.segType = 1
	p.xRef = 8.4778
	p.yRef = 16.2715
	p.tangentAng = -2.2326
	p.rho = 0.0
	p.length = 4.3851
	p.vDes = 0.5
	p.accel = 0.1
	p3.segs.append(p)

	p = PathSegment()
	p.frame_id = "map"
	p.segType = 2
	p.xRef = 5.2784
	p.yRef = 13.2053
	p.tangentAng = -2.2326
	p.rho =  -1.5628
	p.length = 1.0865
	p.vDes = 0.3
	p.accel = 0.2
	p3.segs.append(p)


	p = PathSegment()
	p.frame_id = "map"
	p.segType = 1
	p.xRef =  4.8243
	p.yRef = 12.7544
	p.tangentAng = 2.3526
	p.rho = 0.0
	p.length = 5.6957
	p.vDes = 0.5
	p.accel = 0.2
	p3.segs.append(p)

	p = PathSegment()
	p.frame_id = "map"
	p.segType = 2
	p.xRef = 0.8112
	p.yRef = 16.7962
	p.tangentAng = 2.3526
	p.rho = -100.0
	p.length = 0.0157
	p.vDes = 0.008
	p.accel = 0.02
	p3.segs.append(p)
	paths['bathroom'] = p3

	# start path from bathroom to vending machines
	p4 = Path()
	p = PathSegment()
	p.frame_id = "map"
	p.segType = 2
	p.xRef =  0.8042
	p.yRef = 16.8174
	p.tangentAng =  0.7818
	p.rho = 100.0
	p.length = 0.0157 
	p.vDes = 0.003
	p.accel = 0.01
	p4.segs.append(p)

	p = PathSegment()
	p.frame_id = "map"
	p.segType = 1
	p.xRef =  0.8113
	p.yRef = 16.8244
	p.tangentAng = 2.3606
	p.rho = 0.0
	p.length = 4.7258
	p.vDes = 0.5
	p.accel = 0.1
	p4.segs.append(p)

	p = PathSegment()
	p.frame_id = "map"
	p.segType = 2
	p.xRef = -2.0264
	p.yRef = 20.6746
	p.tangentAng = 2.3606
	p.rho =  -1.3571
	p.length = 1.1600
	p.vDes = 0.4
	p.accel = 0.1
	p4.segs.append(p)

	p = PathSegment()
	p.frame_id = "map"
	p.segType = 1
	p.xRef =  -2.5480
	p.yRef = 21.1951
	p.tangentAng =  0.7864
	p.rho = 0.0
	p.length = 2.7161
	p.vDes = 0.5
	p.accel = 0.1
	p4.segs.append(p)
	paths['vending'] = p4

#start return from vending to lab door
#spin from pt 12 to pt13
	p5 = Path()
	p = PathSegment()
	p.frame_id = "map"
	p.segType = 2
	p.xRef =  -0.6364
	p.yRef = 23.1246
	p.tangentAng =  0.7864
	p.rho = -100.0
	p.length =  0.0314
	p.vDes = 0.003
	p.accel = 0.01
	p5.segs.append(p)
#seg from p13 to p14
	p = PathSegment()
	p.frame_id = "map"
	p.segType = 1
	p.xRef =  -0.6293
	p.yRef = 23.1175
	p.tangentAng = -2.3222
	p.rho = 0.0
	p.length = 2.9072
	p.vDes = 0.5
	p.accel = 0.1
	p5.segs.append(p)

#turn from p14 to p15
	p = PathSegment()
	p.frame_id = "map"
	p.segType = 2
	p.xRef = -1.8012
	p.yRef = 20.2338
	p.tangentAng = -2.3222
	p.rho =  0.8990
	p.length = 1.5431
	p.vDes = 0.4
	p.accel = 0.1
	p5.segs.append(p)

#lineseg from p15 to p16
	p = PathSegment()
	p.frame_id = "map"
	p.segType = 1
	p.xRef =  -2.5908
	p.yRef = 19.4503
	p.tangentAng =  -0.7892
	p.rho = 0.0
	p.length = 11.4321
	p.vDes = 0.5
	p.accel = 0.1
	p5.segs.append(p)
	paths['lab'] = p5

# start path from crawford conference room to women's restroom
	p6 = Path()
	p = PathSegment()
	p.frame_id = "map"
	p.segType = 1
	p.xRef =  0.0
	p.yRef = 0.0
	p.tangentAng =  0.0
	p.rho = 0.0
	p.length = 5.2 
	p.vDes = 0.5
	p.accel = 0.1
	p6.segs.append(p)

	p = PathSegment()
	p.frame_id = "map"
	p.segType = 2
	p.xRef =  5.2
	p.yRef = 0.0
	p.tangentAng = 0.0
	p.rho = -100.0
	p.length = 0.0153
	p.vDes = 0.005
	p.accel = 0.05
	p6.segs.append(p)

	p = PathSegment()
	p.frame_id = "map"
	p.segType = 1
	p.xRef =  5.2
	p.yRef = 0.0
	p.tangentAng =  -1.53
	p.rho = 0.0
	p.length = 11.3 
	p.vDes = 0.5
	p.accel = 0.1
	p6.segs.append(p)

	p = PathSegment()
	p.frame_id = "map"
	p.segType = 2
	p.xRef =  5.66
	p.yRef = -11.291
	p.tangentAng =  -1.53
	p.rho = -100.0
	p.length = 0.0153
	p.vDes = 0.005
	p.accel = 0.05
	p6.segs.append(p)
	paths['womens_room'] = p6

# start path from crawford women's restroom back to conference room 
	p7 = Path()
	p = PathSegment()
	p.frame_id = "map"
	p.segType = 2
	p.xRef =  5.66
	p.yRef = -11.291
	p.tangentAng =  -3.06
	p.rho = -100.0
	p.length = 0.0157 
	p.vDes = 0.005
	p.accel = 0.05
	p7.segs.append(p)

	p = PathSegment()
	p.frame_id = "map"
	p.segType = 1
	p.xRef =  5.66
	p.yRef = -11.291
	p.tangentAng = -4.63
	p.rho = 0.0
	p.length = 11.4
	p.vDes = 0.5
	p.accel = 0.1
	p7.segs.append(p)

	p = PathSegment()
	p.frame_id = "map"
	p.segType = 2
	p.xRef =  4.26
	p.yRef = 0.07
	p.tangentAng =  -4.63
	p.rho = 100.0
	p.length = 0.0157
	p.vDes = 0.005
	p.accel = 0.05
	p7.segs.append(p)

	p = PathSegment()
	p.frame_id = "map"
	p.segType = 1
	p.xRef =  4.26
	p.yRef = 0.07
	p.tangentAng =  -3.06
	p.rho = 0.0
	p.length = 2.9
	p.vDes = 0.5
	p.accel = 0.1
	p7.segs.append(p)

	p = PathSegment()
	p.frame_id = "map"
	p.segType = 2
	p.xRef =  1.3696
	p.yRef = -0.166
	p.tangentAng =  -3.06
	p.rho = -100.0
	p.length = 0.016
	p.vDes = 0.005
	p.accel = 0.05
	p7.segs.append(p)
	paths['conference_room'] = p7

# a test path for the lab
	p8 = Path()
	p = PathSegment()
	p.frame_id = "odom"
	p.segType = 1
	p.xRef =  0.0
	p.yRef = 0.0
	p.tangentAng =  0.0
	p.rho = 0.0
	p.length = 2.0
	p.vDes = 0.5
	p.accel = 0.1
	p8.segs.append(p)

	p = PathSegment()
	p.frame_id = "odom"
	p.segType = 2
	p.xRef =  2.0
	p.yRef = 1.0
	p.tangentAng = 0.0
	p.rho = 1.0
	p.length = 3.1416
	p.vDes = 0.5
	p.accel = 0.1
	p8.segs.append(p)

	p = PathSegment()
	p.frame_id = "odom"
	p.segType = 1
	p.xRef =  2.0
	p.yRef = 2.0
	p.tangentAng =  3.1416
	p.rho = 0.0
	p.length = 1.0
	p.vDes = 0.5
	p.accel = 0.1
	p8.segs.append(p)

	p = PathSegment()
	p.frame_id = "odom"
	p.segType = 2
	p.xRef =  1.0
	p.yRef = 2.01
	p.tangentAng =  3.1416
	p.rho = -100.0
	p.length = 0.0157
	p.vDes = 0.01
	p.accel = 0.1
	p8.segs.append(p)

	p = PathSegment()
	p.frame_id = "odom"
	p.segType = 1
	p.xRef =  0.99
	p.yRef = 2.01
	p.tangentAng =  1.5708
	p.rho = 0.0
	p.length = 1.0
	p.vDes = 0.5
	p.accel = 0.1
	p8.segs.append(p)

    	p = PathSegment()
	p.frame_id = "odom"
	p.segType = 2
	p.xRef =  1.49
	p.yRef = 3.01
	p.tangentAng =  1.5708
	p.rho = -2.0
	p.length = 0.7854
	p.vDes = 0.5
	p.accel = 0.1
	p8.segs.append(p)
	paths['lab_test'] = p8

        p9 = Path()
        p.frame_id = "base_link"
	p.segType = 2
	p.xRef =  0.0
	p.yRef = 0.0
	p.tangentAng =  0.0
	p.rho = 100.0
	p.length = 3.14159
	p.vDes = 0.5
	p.accel = 0.1
        p9.segs.append(p)
        paths['spin_in_place_test'] = p9

	return paths

class PathSender:
	def __init__(self):
		self.paths = makeDummyPaths()
		self.halt_path = Path()
		self.path_pub = rospy.Publisher('desired_path', Path)
		self.command_sub = rospy.Subscriber('chatter', String, self.handle_chatter)

	def handle_chatter(self, msg):
		if 'open' in msg.data or 'close' in msg.data:
			pass
		else:
		    path = self.paths.get(msg.data, self.halt_path)
		    self.path_pub.publish(path)

if __name__ == "__main__":
	rospy.init_node("path_sender")
	ps = PathSender()
	rospy.spin()
