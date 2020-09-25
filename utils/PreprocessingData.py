import pandas as pd
from sqlalchemy import create_engine

class PreprocessingData:
    """ Preprocessing and saving data into database """

    def __init__(self, path_to_db, path_csv, table_name):
        self.path_to_db = "sqlite:///" + path_to_db
        self.path_csv = path_csv
        self.table_name = table_name

    def normalize_data(self):
        data = pd.read_csv(self.path_csv)
        columns = data.columns.tolist()
        cols_to_use = columns[1:len(columns)]
        cols_to_be_del = ['Lat', 'Long']
        df = pd.read_csv(self.path_csv, usecols=cols_to_use)
        df = df.drop(columns=cols_to_be_del)
        return df

    # For retrieve lastest column in sql
    def get_lastest_date(self):
        df = self.normalize_data()
        columns = df.columns.tolist()
        return columns[-1]

    # To store dataframe into sqlite
    def save_to_sql(self):
        engine = create_engine(self.path_to_db, echo=False)
        sqlite_connection = engine.connect()
        df = pd.read_csv(self.path_csv)
        df.to_sql(self.table_name, con=sqlite_connection)
        sqlite_connection.close()