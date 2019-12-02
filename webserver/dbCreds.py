def getURI():
    POSTGRES = {
        'user': 'joe',
        'pw': '',
        'db': 'postgres',
        'host': 'localhost',
        'port': '5432',
    }
    return 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

if __name__ == '__main__':
    getURI()
