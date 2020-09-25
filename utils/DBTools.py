import sqlite3


# Create connection to database
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = sqlite3.connect(db_file)

    return conn


def retrieve_datum(conn, queries):
    """ Retrieve a single data from queries """
    result = ''
    c = conn.cursor()
    c.execute(queries)
    result = c.fetchone()
    # except Exception as e:
    #     print("Query failed: " + str(e))
    #     return 'failed'
    # finally:

    return result
