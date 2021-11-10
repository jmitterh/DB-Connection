'''
database connection dependencies (postgresql so far):
pip install sqlalchemy
pip install psycopg2

'''
from sqlalchemy import create_engine

# importing socket module for ip address identification
import socket

# Credentials Dictionary to connecting to database via different networks
credentials = {
    'mysql': {
        'computer ip address': {'host': 'localhost', 'port': '3306', 'pw': '*****', 'user': 'mysql'},
        'computer ip address2': {'host': 'localhost', 'port': '3306', 'pw': '*****', 'user': 'mysql'}
    },
    'postgresql': {
        'computer ip address': {'host': 'localhost', 'port': '5432', 'pw': '****', 'user': 'postgres'},
        'computer ip address2': {'host': 'localhost', 'port': '5432', 'pw': '*****', 'user': 'postgres'}
    },
    'oracle': {
        'computer ip address': {'host': '127.0.0.1', 'port': '1521', 'pw': '*****', 'user': 'username'},
        'computer ip address2': {'host': '127.0.0.1', 'port': '1521', 'pw': '*****', 'user': 'username'}
    },
    'sqlite': {
        'computer ip address': {'host': 'C:\\path\\to\\foo.db', 'port': 'none', 'pw': 'none', 'user': 'none'},
        'computer ip address2': {'host': 'C:\\path\\to\\foo.db', 'port': 'none', 'pw': 'none', 'user': 'none'}
    }
}

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
            f"DB_Connection.py file: Variable db not defined since ip address on this computer is not in the "
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


# MySQL *have not tested
def MysqlConnection(DbName):
    host, port, pw, user = cred_info_for("mysql")

    DB_PASS = pw
    DB_NAME = DbName.lower()
    engine = create_engine(f'mysql://{user}:{DB_PASS}@{host}:{port}/{DB_NAME}')

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
