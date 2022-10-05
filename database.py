import psycopg2

'''
class Database:
    def __init__(self, host='localhost', db_name='restoran_user', dbuser='postgres', password='admin'):
        self.host = host
        self.db_name = db_name
        self.dbuser = dbuser
        self.password = password
        self.cursor = ''
        self.conn = ''

    def connection(self):
        self.conn = psycopg2.connect(
            host=self.host,
            database=self.db_name,
            user=self.dbuser,
            password=self.password)
        self.cursor = self.conn.cursor()
        return True

    def commit(self):
        try:
            self.conn.commit()
        except Exception as e:
            print(e, 'Ошибка с коммитов в базу; Возможно, при таком взаимоджействии коммит не нужен')
            pass

    def close_connection(self):
        self.conn.close()
        self.cursor.close()
        #return True
'''
