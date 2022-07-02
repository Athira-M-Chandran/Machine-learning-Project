from flask import Flask
import sys
import housing
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)


@app.route("/",methods = ['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom Exception")
    except Exception as e:
        housing = HousingException(e,sys)
        # raise HousingException(e,sys) from e
        logging.info((housing.error_message))
        logging.info("We are testing loggiing module")
    return 'CI CD pipeline has been established'


if __name__=='main':
    
    app.run()