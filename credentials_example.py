# Credentials Dictionary to connecting to database via different networks
credentials = {
        'mysql': {
            'computer ip address': {'host': 'localhost', 'port': '3306', 'pw': '*****', 'user': 'mysql'},
            'computer ip address2': {'host': 'localhost', 'port': '3306', 'pw': '*****', 'user': 'mysql'}
        },
        'postgresql': {
            'computer ip address': {'host': 'localhost', 'port': '5432', 'pw': '*****', 'user': 'postgres'},
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