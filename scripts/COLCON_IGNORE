
import cv2
import numpy as np
from openni import openni2
from openni import _openni2 as c_api

from ultralytics import YOLO

model = YOLO("yolov8-floor-seg.pt")  


openni2.initialize()
dev = openni2.Device.open_any()


depth_stream = dev.create_depth_stream()
depth_stream.start()
depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_100_UM, resolutionX = 640, resolutionY = 480, fps = 30))


colour_stream = dev.create_color_stream()
colour_stream.start()
colour_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_RGB888, resolutionX = 640, resolutionY = 480, fps = 30)) 


while True:
                
        depth = depth_stream.read_frame()
        color = colour_stream.read_frame()

        depth_data = depth.get_buffer_as_uint16()
        color_data = color.get_buffer_as_uint8()


        arr_depth = np.frombuffer(depth_data, dtype=np.uint16)
        arr_depth = arr_depth.reshape(480, 640)

        arr_color = np.frombuffer(color_data, dtype=np.uint8)
        arr_color = arr_color.reshape(480, 640, 3)
    
        image = arr_color
        depth_image = arr_depth

        results = model(image)
        results = results[0].plot()

        image[:, :, [0,2]] = image[:, :, [2,0]]

       
        cv2.imshow('input',image)
        cv2.imshow("depth", depth_image) 
        cv2.imshow("segmentation", results)

        key = cv2.waitKey(30)
        if key == ord('q') or key == 27:
            break



       
             
             
