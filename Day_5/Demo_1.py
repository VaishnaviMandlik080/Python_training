
'''
Create a module containing:
- A function to display file names.
- A class to store and return two values.
- A function that returns a connection object.
'''


def display():
    '''Display a list of file names.'''
    for var in ['f1', 'f2', 'f3']:
        print(var)


class Cname:
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def display(self):
        '''Return the initialized values.'''
        return self.a1, self.a2


def connect(dsn):
    class Connection:
        def __init__(self, dsn, dbname, password):
            self.dsn = dsn
            self.dbname = dbname
            self.password = password

        def method1(self):
            return 'Query process'

    obj = Connection(dsn, 'sqlite3', 'password')
    return obj