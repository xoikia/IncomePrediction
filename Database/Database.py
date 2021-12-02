from CustomLogger.logger import Logger
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

logging = Logger()
class Connector:
    def __init__(self):
        """
        :DESC: Creates connection with Database when backend thread runs.
        """
        try:
            self.KEYSPACE = "userincomedata"
            self.Client_id = 'mIpnKGRKdSgfYCWxQtQvhRzA'
            self.Client_secret = 'glIuXDR_wDg9oYv2FaHLCf,5vwhiplWTThGX1qZOstOoKCZjEW1tzLokIGczS7Zg7225p69Z1Qc-7c7ugWTUPA.8lEv0wYRE0b+a4jX9x_icLFmjWP97x3Z5e,RqmuS-'
            cloud_config = {'secure_connect_bundle': 'secure-connect-user-income-db.zip'}
            auth_provider = PlainTextAuthProvider(self.Client_id, self.Client_secret)
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            self.session = cluster.connect()
            logging.info("INFO", "Successfully connected to Database")
        except:
            logging.info("ERROR", 'While connecting to the Database')

    def master(self):
        """
        :DESC: Creates table if not existed into database
        """
        try:
            self.session.execute("use userincomedata")
            self.session.execute("select release_version from system.local").one()
            self.session.execute(
                "CREATE TABLE Data(Name text PRIMARY KEY,Age text,Work_Class text,Education text,Marital_Status text,Occupation text,Race text,Sex text,Capital_Gain text,Capital_Loss text,Hours text,Country text,Income text);")
            logging.info("INFO", "Table successfully created")
        except:
            logging.info("INFO", "The Table already exists")

    def insert_data(self, data):
        """
        :param data: Gets data from user and puts it into database
        """
        try:
            column = "Name,Age,Work_Class,Education,Marital_Status,Occupation,Race,Sex,Capital_Gain,Capital_Loss,Hours,Country"
            value = "'{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}'".format(
                data['Name'][0], data['Age'][0], data['Work_Class'][0], data['Education'][0], data['Marital_Status'][0],
                data['Occupation'][0], data['Race'][0], data['Sex'][0], data['Capital_Gain'][0],
                data['Capital_Loss'][0], data['Hours'][0], data['Country'][0])

            custom = "INSERT INTO data({}) VALUES({});".format(column, value)
            self.session.execute("USE userincomedata")
            self.session.execute(custom)
            logging.info('INFO', "User Data inserted ")
        except:
            logging.info("ERROR", "While adding the data to database")

    def insert_result(self, result, name):
        """
        :param name:
        :param result: Gets result from prediction and puts it into database
                name: name of the user where to put update the income in the database
        """
        try:
            custom = "update data set income='{}' where name='{}';".format(result, name)
            self.session.execute("USE userincomedata")
            self.session.execute(custom)
            logging.info("INFO", "Result added successfully")
        except:
            logging.info("ERROR", 'While adding the result to database')
