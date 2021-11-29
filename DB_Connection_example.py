'''
database connection dependencies postgresql:
pip install sqlalchemy
pip install psycopg2

database connection dependencies for MySQL
pip install mysql-connector-python
pip intsll mysql
*note: install microsoft C++ Build Tools  https://visualstudio.microsoft.com/visual-cpp-build-tools/
Microsoft Visual C++ 14.0 or greater
'''
from sqlalchemy import create_engine

# importing socket module for ip address identification
import socket
# credentials file
from credentials_example import *

# getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
# getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
# View the ip address you are on
print(f'Your computer ip address in this network: {ip_address}\n')


## Grabbing information from Dictionary
def cred_info_for(database_flavor):
    database_flavor = database_flavor.lower()
    '''
    :param database_flavor: give the database flavor name you use (mysql,oracle,postgres, or sqlite)
    :return: credentials to connect to specified DB based on the ip address your computer has for a given network
    '''
    for key, value in credentials.items():
        if database_flavor == key:
            print("assign ip address")
        for k, v in value.items():
            if ip_address == k:
                # appending to dictionary d
                db = v
    try:
        # Store in variables
        host = db.get('host')
        port = db.get('port')
        pw = db.get('pw')
        user = db.get('user')
    except NameError:
        print(
            f"credentials_example.py file: Variable db not defined since ip address on this computer is not in the "
            f"credentials for {database_flavor} "
            f"dict.\nAdd the ip address({ip_address}) and database connection credentials to the dictionary called "
            f"'credentials' .")
    except Exception as e:
        print("Something Unknown went wrong", e.__class__, "occurred.")

    return host, port, pw, user


## Database connection ##

# PostgreSQL
def PostgresConnection(DbName):
    host, port, pw, user = cred_info_for("postgres")

    DB_PASS = pw  # db password, not postgres login password
    DB_NAME = DbName.lower()
    engine = create_engine(f'postgresql://{user}:{DB_PASS}@{host}:{port}/{DB_NAME}')

    return engine


# MySQL
def MysqlConnection(DbName):
    host, port, pw, user = cred_info_for("mysql")

    DB_PASS = pw
    DB_NAME = DbName.lower()
    engine = create_engine(f'mysql+mysqldb://{user}:{DB_PASS}@{host}:{port}/{DB_NAME}')

    return engine


# Oracle *have not tested
def OracleConnection(DbName):
    host, port, pw, user = cred_info_for("oracle")

    DB_PASS = pw
    DB_NAME = DbName.lower()
    engine = create_engine(f'oracle://{user}:{DB_PASS}@{host}:{port}/{DB_NAME}')

    return engine


# SQLite *have not tested
def SQLiteConnection(DbName):
    host, port, pw, user = cred_info_for("sqlite")

    DB_Path = host
    engine = create_engine(f'sqlite:///{DB_Path}')

    return engine


# test connection
connection = PostgresConnection("db_name_here")
result = connection.execute("select * from table_name")
for row in result:
    print("table_name:", row['column_name'])

# # test connection
# connection = MysqlConnection("world")
# result = connection.execute("select * from city")
# for row in result:
#     print("Name:", row['Name'])