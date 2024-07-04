
import rclpy
from rclpy.node import Node

import numpy as np
import cv2

from cv_bridge import CvBridge
from sensor_msgs.msg import Image


class ImgSubscriber(Node):

    def __init__(self):
        super().__init__('img_subscriber')
        self.subscription = self.create_subscription( Image,'/r0/camera/color/image_raw', self.listener_callback, 10)
        self.img = None
        self.bridge = CvBridge()
        self.i = 0
        self.timer = self.create_timer(1, self.timer_callback)

    def listener_callback(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg)
        if img is not None:
            self.img = img
        
    def timer_callback(self):
        if self.img is not None:
            self.i += 1
            image_path = "/home/nvidia/car_pictures/image" + str(self.i) + ".png"   

            cv2.imwrite(image_path, self.img)
        


def main(args=None):
    rclpy.init(args=args)

    img_subscriber = ImgSubscriber()

    rclpy.spin(img_subscriber)


    img_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
