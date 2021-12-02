import threading
import pandas as pd
from joblib import load
from CustomLogger.logger import Logger
from Database.Database import Connector
from Education_int import EducationGroup

logging = Logger()


class Thread(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
        def function():
            self.result = target(*args, **kwargs)
        super().__init__(group=group, target=function, name=name, daemon=daemon)


def backend(user_data):
    """
    :Desc: This function performs type conversion of the data and creates a
            object of the Connector()
    :param: user_data
    :return: encoded data for the model for prediction and the connector object
    """
    del user_data['submit']
    data = pd.DataFrame(data=[user_data], columns=user_data.keys())
    for col_name in ['Age', 'Capital_Gain', 'Capital_Loss', 'Hours']:
        data[col_name] = data[col_name].astype('int64')
    connector = Connector()
    try:
        connector.master()
        connector.insert_data(data)
    except:
        connector.insert_data(data)
    finally:
        logging.info("INFO", "Data ")
    return connector


def preprocess(user_data):
    """
    :Desc: This function performs preprocessing of the data
    :param: user_data
    :return: encoded data for the model for prediction
    """

    data = pd.DataFrame(data=[user_data], columns=user_data.keys())
    for col_name in ['Age', 'Capital_Gain', 'Capital_Loss', 'Hours']:
        data[col_name] = data[col_name].astype('int64')
    try:
        encoder = load('Encode_Sacler_Pipeline.pkl')
        edu = EducationGroup()
        logging.info('INFO', 'Preprocessing files successfully loaded')
        try:
            transformed_data = edu.transform(data)
            transformed_data = transformed_data.drop(['Name'], axis=1)
            encoded_data = encoder.transform(transformed_data)
            logging.info('INFO', 'Data was PreProcessed successfully')
            return encoded_data
        except:
            logging.info('ERROR', 'While Preprocessing')
    except:
        logging.info('ERROR', 'While loading the preprocessing files')


def getResult(user_data):
    """
    :Desc: This function creates thread for featureCorrection,backend
    :param: encoded_data
    :return: Sends data into for Prediction and connector object
    """
    logging.info('INFO', 'Threading Called !')
    in1 = user_data
    in2 = user_data
    thread1 = Thread(target=backend, args=(in1,))
    thread2 = Thread(target=preprocess, args=(in2,))
    logging.info('INFO', 'Threading Created !')
    thread1.start()
    thread2.start()
    logging.info('INFO', 'Threading Started !')
    thread1.join()
    thread2.join()
    logging.info('INFO', 'Threading join !')
    return thread2.result, thread1.result