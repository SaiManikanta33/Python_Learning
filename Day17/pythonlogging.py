        #Python loggging 
    #Instead of using print(), use the logging module
#Basic Example

import logging
logging.basicConfig(level=logging .INFO)

logging.info("Application Started")
logging.warning("Low disk space")
logging.error("Connection failed")


#Log to a File
import logging 
logging.basicConfig(
    filename="Day17/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)
logging.info("Programming started")
logging.warning("Warning message")
logging.error("Error occured")


import logging 
try:
    result = 10/0
except ZeroDivisionError:
    logging.exception("Division by Zero")