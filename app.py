# All Necessary Library Imports
from forms import DataForm
from joblib import load
from Utility import getResult
from CustomLogger.logger import Logger
from flask import Flask, request, render_template


logging = Logger()

# Flask App and Secret Key
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'


@app.route("/", methods=['GET', 'POST'])
def home():
    """
    :Desc: This is our home api, It handles exception together with rendering.
           Adds combination provided by user into Database
           Stores all the steps using logger
    :return: Render index.html Template
]
    """
    form = DataForm()
    if request.method == 'POST':
        logging.info('INFO', 'Requested method : POST')
        if form.is_submitted():
            logging.info('INFO', 'form submitted, there is an active request and the method is POST')
            try:
                user_data = request.form.to_dict()
                logging.info('INFO', 'Values retrieved from the form')
                try:
                    encoded_data, connector = getResult(user_data)
                    try:
                        model = load('xgb.pickle')
                        logging.info('INFO', 'XGB model successfully loaded!')
                        try:
                            result = ('above 50K' if model.predict(encoded_data)[0] == 1 else 'below 50K')
                            logging.info('INFO', 'Model prediction completed')
                            try:
                                connector.insert_result(result, user_data['Name'])
                                logging.info('INFO', 'Uploaded to Database')
                            except:
                                logging.info('ERROR', 'While uploading the result to database')
                            finally:
                                return render_template('index.html', form=form, value=result)
                        except:
                            logging.info('ERROR', 'While Prediction')
                    except:
                        logging.info('ERROR', 'While loading the ML model')
                        return render_template('error.html')
                except:
                    logging.info('ERROR', 'While executing getResult()')
                    return render_template('error.html')
            except:
                logging.info('ERROR', 'While retrieving data')
                return render_template('error.html')
    return render_template('index.html', form=form, value=None)


# Main File Run Debug Mode
if __name__ == "__main__":
    app.run(debug=True)
