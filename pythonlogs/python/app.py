
import logging 
## logging setting 

logging.basicConfig( 
    level = logging.DEBUG, 
    format = '%(asctime)s- %(name)s-%(levelname)s-%(message)s',
    datefmt = '%Y-%M-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmaticApp")

def add(a,b):
    result=a+b
    logger.debug(f"Adding {a}+{b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    logger.debug(f"Subtraction {a} - {b} = result")
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b}")
    return result

def divide(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error ")
        return None
    
add(10,12)  
subtract(20,30)
multiply(12,13)
divide(10,20)
## we have to write this ->  python pythonlogs/python/app.py  in cmd terminal to run this code
