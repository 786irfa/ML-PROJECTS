import os
import logging
from datetime import datetime

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
logs_path = os.path.join(BASE_DIR, "..", "logs")
logs_path = os.path.abspath(logs_path)
print("Logs folder will be created at:", logs_path)
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_path = os.path.join(logs_path, LOG_FILE)
print("Log file will be created at:", LOG_FILE_path)

logging.basicConfig(
    filename=LOG_FILE_path,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
if __name__ == "__main__":
    logging.info("logging has started")
    print("Script ran. Check the logs folder for log output.")

    

    

