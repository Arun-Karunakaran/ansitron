
# !/usr/bin/python2.7

import psycopg2
import sys


from dbconnection import dbconnect
from config import *

db = dbconnect(DATABASENAME1,USERNAME1,PASSWORD1)

class _verify:

    def __init__(self,tablename,columname=None,no_of_rows=None):

        self.tablename = tablename
        self.columname = columname if columname is not None else columname
        self.no_of_rows = int(no_of_rows) if no_of_rows is not None else no_of_rows
    
    def verifyschemaexists(self):

        con = None
        schemaname = self.tablename.split(".")
        s = len(schemaname)
        try:
            if s == 1:
                pass
            else:
                raise ValueError("schema not specified in format classname('schemaname')")
            cur,con = db.connect()
            sqlselect = "SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_catalog=" + "'" + DATABASENAME1 + "'" + "AND table_schema=" + "'" + schemaname[0] + "');"
            row = cur.execute(sqlselect)
            row = cur.fetchall()
            if row[0][0] == False:
                raise ValueError('schema does not exists')
            else:
                pass
            con.commit()
        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print ('Error %s' % e)
            sys.exit(1)
        finally:
            if con:
                con.close()

    def verifytableexists(self):

        con = None
        schematable = self.tablename.split(".")
        s = len(schematable)
        try:
            if s == 2:
                pass
            else:
                raise ValueError("schema or tablename not specified in format classname('schema.tablename')")
            cur,con = db.connect()
            sqlselect = "SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_catalog=" + "'" + DATABASENAME1 + "'" + "AND table_schema=" + "'" + schematable[0] + "'" + "AND table_name=" + "'" + schematable[1] + "');"
            row = cur.execute(sqlselect)
            row = cur.fetchall()
            if row[0][0] == False:
                raise ValueError('table or schema does not exists')
            else:
                pass
            con.commit()
        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print ('Error %s' % e)
            sys.exit(1)
        finally:
            if con:
                con.close()

    def verifytablecolumnexists(self):

        con = None
        schematable = self.tablename.split(".")
        s = len(schematable)
        c = len(self.columname.split()) if self.columname is not None else 0
        try:
            if s == 2 and c == 1:
                pass
            else:
                raise ValueError("schema or tablename or columname not specified in format classname('schema.tablename','columname')")
            cur,con = db.connect()
            sqlselect = "SELECT EXISTS(SELECT 1 FROM information_schema.columns WHERE table_catalog=" + "'" + DATABASENAME1 + "'" + "AND table_schema=" + "'" + schematable[0] + "'" + "AND table_name=" + "'" + schematable[1] + "'" + "AND column_name=" + "'" + self.columname + "');"
            row = cur.execute(sqlselect)
            row = cur.fetchall()
            if row[0][0] == False:
                raise ValueError('table or schema or column does not exists')
            else:
                pass
            con.commit()
        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print ('Error %s' % e)
            sys.exit(1)
        finally:
            if con:
                con.close() 


class _list:

    def __init__(self,objectname,columname=None,no_of_rows=None):

        self.objectname = objectname
        self.columname = columname if columname is not None else columname
        self.no_of_rows = int(no_of_rows) if no_of_rows is not None else no_of_rows

    def list_schemas(self):

        con = None
        try:
            cur,con = db.connect()
            sqlselect = "SELECT distinct(table_schema) FROM information_schema.tables WHERE table_catalog=" + "'" + self.objectname + "';"
            row = cur.execute(sqlselect)
            row = cur.fetchall()
            if len(row) == 0:
                raise ValueError('No schema found for database')
            else:
                return row
            con.commit()
        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print ('Error %s' % e)
            sys.exit(1)
        finally:
            if con:
                con.close()

    def list_tables(self):

        con = None
        try:
            self.verifyschemaexists()
            cur,con = db.connect()
            sqlselect = "SELECT distinct(table_name) FROM information_schema.tables WHERE table_catalog=" + "'" + DATABASENAME1 + "'" + "AND table_schema=" + "'" + self.verifyschemaexists.schematable[0] + "';"
            row = cur.execute(sqlselect)
            row = cur.fetchall()
            print(row)
            if len(row) == 0:
                raise ValueError('No tables found for schema')
            else:
                return row
            con.commit()
        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print ('Error %s' % e)
            sys.exit(1)
        finally:
            if con:
                con.close()

    def list_columns(self):

        con = None
        try:
            self.verifytableexists()
            cur,con = db.connect()
            sqlselect = "SELECT table_name FROM information_schema.tables WHERE table_catalog=" + "'" + DATABASENAME1 + "'" + "AND table_schema=" + "'" + self.verifytableexists.schematable[0] + "'" + "AND table_name=" + "'" + self.verifytableexists.schematable[1] + "';"
            row = cur.execute(sqlselect)
            row = cur.fetchall()
            print(row)
            if len(row) == 0:
                raise ValueError('No columns found for schema.table')
            else:
                return row
            con.commit()
        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print ('Error %s' % e)
            sys.exit(1)
        finally:
            if con:
                con.close()


class _selecttables:

    def __init__(self,tablename,columname='*',no_of_rows=None):
        
        self.tablename = tablename
        self.columname = columname
        self.no_of_rows = int(no_of_rows) if no_of_rows is not None else no_of_rows 

    def select_allrows(self):

        con = None
        try:
            verify = _verify()
            verify.self.verifytableexists()
            del verify
            cur,con = db.connect()
            sqlselect = "select * from " + self.tablename + ";"
            rows = cur.execute(sqlselect)
            rows = cur.fetchall()
            print(rows)
            con.commit()
        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print ('Error %s' % e)
            sys.exit(1)
        finally:
            if con:
                con.close()

    def select_onerow(self):

        con = None
        try:
            verify = _verify()
            verify.self.verifytableexists()
            del verify
            cur,con = db.connect()
            sqlselect = "select * from " + self.tablename + ";"
            rows = cur.execute(sqlselect)
            rows = cur.fetchone()
            print(rows)
            con.commit()
        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print ('Error %s' % e)
            sys.exit(1)
        finally:
            if con:
                con.close()

    def select_rows(self):

        con = None
        try:
            verify = _verify()
            verify.self.verifytableexists()
            del verify
            cur, con = db.connect()
            sqlselect = "select * from " + self.tablename + ";"
            sqlcount = "select count(*) from " + self.tablename + ";"
            rows = cur.execute(sqlselect)
            rows = cur.fetchmany(self.no_of_rows)
            count = cur.execute(sqlcount)
            count = cur.fetchone()
            print (int(count[0]))
            if int(count[0]) >= self.no_of_rows:
                print(rows)
            else:
                print ('Error: You are looking for rows beyond the total no of records present in the table')
            con.commit()
        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print ('Error %s' % e)
            sys.exit(1)
        finally:
            if con:
                con.close()

    def select_totalcount(self):

        con = None
        try:
            verify = _verify()
            verify.self.verifytableexists()
            del verify
            cur, con = db.connect()
            sqlcount = "select count(*) from " + self.tablename + ";"
            count = cur.execute(sqlcount)
            count = cur.fetchone()
            print(int(count[0]))
            con.commit()
        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print ('Error %s' % e)
            sys.exit(1)
        finally:
            if con:
                con.close()

    def select_allrowsforcolumn(self):

        con = None
        try:
            verify = _verify()
            verify.self.verifytablecolumnexists()
            del verify
            cur,con = db.connect()
            sqlselect = "select " + self.columname + " from " + self.tablename + ";"
            rows = cur.execute(sqlselect)
            rows = cur.fetchall()
            print(rows)
            con.commit()    
        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print ('Error %s' % e)
            sys.exit(1)
        finally:
            if con:
                con.close()

    def select_onerowforcolumn(self):

        con = None
        try:
            verify = _verify()
            verify.self.verifytablecolumnexists()
            del verify
            cur,con = db.connect()
            sqlselect = "select " + self.columname + " from " + self.tablename + ";"
            rows = cur.execute(sqlselect)
            rows = cur.fetchone()
            print(rows)
            con.commit()
        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print ('Error %s' % e)
            sys.exit(1)
        finally:
            if con:
                con.close()

    def select_rowsforcolumn(self):

        con = None
        try:
            verify = _verify()
            verify.self.verifytablecolumnexists()
            del verify
            cur, con = db.connect()
            sqlselect = "select " + self.columname + " from " + self.tablename + ";"
            sqlcount = "select count(*) from " + self.tablename + ";"
            rows = cur.execute(sqlselect)
            rows = cur.fetchmany(self.no_of_rows)
            count = cur.execute(sqlcount)
            count = cur.fetchone()
            print (int(count[0]))
            if int(count[0]) >= self.no_of_rows:
                print(rows)
            else:
                print ('Error: You are looking for rows beyond the total no of records present in the table')
            con.commit()
        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print ('Error %s' % e)
            sys.exit(1)
        finally:
            if con:
                con.close()
