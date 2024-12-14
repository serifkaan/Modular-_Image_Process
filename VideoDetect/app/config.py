import toml
from loguru import logger

class Config :
    def loadConfig(self,config_file):

        try:
            with open(config_file, "r") as f:
                config_data = toml.load(f)
                logger.info("Config.toml okundu")
            return config_data
        except Exception as e:
            logger.error(f"Config.toml okunamadi: {e}")
            return None
