import cv2
import numpy as np

class CameraProcessor:
    def __init__(self, config):
        self.config = config


    def process_frame(self, frame):


        blurred = cv2.GaussianBlur(frame, (15, 15), 0)

        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        detected_colors = []


        for  color_name,color_bounds in self.config['colors'].items():

            lower = np.array(color_bounds['lower'])
            upper = np.array(color_bounds['upper'])
            mask = cv2.inRange(hsv, lower, upper)


            kernel = np.ones((5, 5), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                area = cv2.contourArea(contour)
                min_area = 1000

                if area > min_area:

                    ((x, y), radius) = cv2.minEnclosingCircle(contour)
                    center = (int(x), int(y))
                    radius = int(radius)


                    if color_name == "blue":
                        color_code = (255, 0, 0)
                    elif color_name == "green":
                        color_code = (0, 255, 0)
                    elif color_name == "red":
                        color_code = (0, 0, 255)
                    elif color_name == "yellow":
                        color_code = (0, 255, 255)
                    else:
                        continue


                    cv2.circle(frame, center, radius, color_code, 3)
                    cv2.putText(frame, color_name, (center[0] - 40, center[1] - 20),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_code, 2)

                    detected_colors.append(color_name)

        return frame, detected_colors

