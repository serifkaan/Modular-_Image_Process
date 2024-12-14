import cv2
from app.config import Config
from app.logger import setup_logger
from app.camera_process import CameraProcessor
from app.streamer import Streamer

def main():

    logger = setup_logger()
    logger.info("Log baslatildi")
    config_loader = Config()
    config = config_loader.loadConfig("/home/kaan/PycharmProjects/VideoDetect/config/config.toml")
    processor = CameraProcessor(config)
    logger.info("Goruntu isleme baslatildi")
    streamer = Streamer()

    try:

        for frame in streamer.get_frame():

            processed_frame, detected_colors = processor.process_frame(frame)
            cv2.imshow("Processed Frame", processed_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:

        logger.info("Goruntu isleme bitti")
        streamer.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
