

"""
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("Debug message")
logging.info("Application started")
logging.warning("Low disk space")
logging.error("Database connection failed")
logging.critical("Application crashed")


    #3. Logging to a file
    
import logging
logging.basicConfig(filename="Day26/app.log",level=logging.INFO)
logging.info("Program started")
logging.warning("Invalid password")
logging.error("Connection failed")
"""



    #4. Custom log format
    
import logging
logging.basicConfig(filename="Day26/app.log",level=logging.INFO,format="%(asctime)s | %(levelname)s | %(message)s")
logging.info("Application Started")

""" Useful placce holders
        -->     %(asctime)s
        -->     %(levelname)s
        -->     %(message)s
        -->     %(filename)s
        -->     %(funcName)s            """
        
        
        
    #5. Rotating log files
    #large log files become difficult to manage
    
import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler("Security.log",maxBytes=1024,backupCount=3,force=True)

logging.basicConfig(handler=[handler],level=logging.INFO,format="%(asctime)s | %(levelname)s | %(message)s")

logging.info("Security Event")



    #6. Logging Exception
import logging
logging.basicConfig(level=logging.ERROR)
try:
    number = 10/0
except Exception:
    logging.exception("Unexpected Error")