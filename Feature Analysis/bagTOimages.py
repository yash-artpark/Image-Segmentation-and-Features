#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2016 Massachusetts Institute of Technology

"""Extract images from a rosbag.
"""

import os
import cv2
import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():
    """Extract a folder of images from a rosbag.
    """
    
    bag = rosbag.Bag('2021-01-27-12-23-45.bag', "r")
    bridge = CvBridge()
    count = 0
    print('Initializing export...')

    for topic, msg, t in bag.read_messages(topics=['/zedm/zed_node/left/image_rect_color']):
        cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")

        cv2.imwrite(os.path.join('data_indoor', "frame%06i.png" % count), cv_img)

        count += 1
	print('image',count,'done!')

    bag.close()

    return

if __name__ == '__main__':
    main()
