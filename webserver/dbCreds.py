def getURI():
    POSTGRES = {
        'user': 'sssst',
        'pw': 'YouTube1000',
        'db': 'postgres',
        'host': 'localhost',
        'port': '5432',
    }
    return 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

if __name__ == '__main__':
    getURI()


'''
REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM postgres;
REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM postgres;
REVOKE ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public FROM postgres;
DROP USER postgers;
'''