
#!/usr/bin/python2.7

import psycopg2
import sys


class connection:

    def __init__(self, dbname, user, password, host='localhost', port='5432', sslmode='disable'):

        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.sslmode = sslmode

    def connect(self):

        con = None
        try:
            cs = "host=%s port=%s dbname=%s user=%s password=%s sslmode=%s" % (self.host,self.port,self.dbname,self.user,self.password,self.sslmode)
            con = psycopg2.connect(cs)
            cur = con.cursor() 
        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print ('Error %s' % e)
            sys.exit(1)
        finally:
            if con:
                return cur,con

