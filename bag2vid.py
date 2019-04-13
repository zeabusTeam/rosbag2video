import cv2

import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import re


class bag2vid:

    TOPIC_TYPE = {
        'com': 'sensor_msgs/CompressedImage',
        'raw': 'sensor_msgs/Image'
    }

    def __init__(self, name=None):
        if name is None:
            print('Please enter bag file name')
        self.name = name
        self.bag = rosbag.Bag(self.name)

    def getalltopic(self):
        if self.name is None:
            return False
        return self.bag.get_type_and_topic_info()

    def filterImg(self, rostopic):
        topics = []
        for i in rostopic:
            topic_attrib = i.values()[0]
            if type(topic_attrib) == str:
                continue
            msg_type = getattr(topic_attrib, 'msg_type', None)
            if msg_type is None:
                continue
            if msg_type in self.TOPIC_TYPE.values():
                topics.append(
                    (i.keys()[0], msg_type, topic_attrib.frequency))
        return topics

    def convert(self, topic_name, img_type=None, freq=10):
        bridge = CvBridge()
        filename = self.name[0:-4]+'_' + \
            ".".join(re.findall("[a-zA-Z]+", topic_name))+'.avi'
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        writer = None
        for topic, msg, t in self.bag.read_messages(topics=[topic_name]):
            if self.TOPIC_TYPE['com'] == img_type or img_type is None:
                cv_img = bridge.compressed_imgmsg_to_cv2(msg)
            else:
                cv_img = bridge.imgmsg_to_cv2(msg)
            if writer is None:
                writer = cv2.VideoWriter(
                    filename, fourcc, freq, tuple(cv_img.shape[:2][::-1]))
            writer.write(cv_img)
            # cv2.imshow('img', cv2.resize(cv_img, None, fx=0.25, fy=0.25))
            # cv2.waitKey(1)
        writer.release()
