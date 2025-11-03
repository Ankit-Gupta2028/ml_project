import logging
import os 
from datetime import datetime

LOF_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOF_FILE)
os.makedirs(logs_path,exist_ok=True) #os.makedirs(logs_path,exist_ok=True) Because your logs (messages about what your program is doing) need a folder to be saved inside.

LOG_FILE_PATH=os.path.join(logs_path,LOF_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has started")
    