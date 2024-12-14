import cv2
from loguru import logger
class Streamer:
    def __init__(self):

        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            logger.error("Kamera acılamadı")

        logger.info("Kamera acildi")
    def get_frame(self):

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            frame = cv2.flip(frame,1)

            yield frame

    def release(self):

        self.cap.release()
        logger.info("Kamera kapatildi")

