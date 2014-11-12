#! /python34/python.exe
## @package dbases.py
# This package provides basic operations on sqlite3 disk-based databases.
#
# This module allows to store and extract needed tasks for the user.
 
 
import sqlite3


class TaskDBase(object):
    
    def __init__(self,name='tasks.db'):
        self.name=name
        self.con=None
        self.cur=None
        
    def setupDbase(self):
        # The database file is created if it does not exist yet. Open a connector to the database.
        self.con=sqlite3.connect(self.name)
        # Now get a cursor of the connector that enables executing commands.
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE Tasks(task VARCHAR(255) PRIMARY KEY, variables VARCHAR(255),type CHAR NOT NULL,difficulty CHAR NOT NULL)")
        self.cur.execute("CREATE TABLE Solutions(solution VARCHAR(255) NOT NULL, description VARCHAR(255) NOT NULL,task VARCHAR(255) NOT NULL,FOREIGN KEY (task) REFERENCES Tasks (task),PRIMARY KEY \
        (task,solution))")
        
 
    def closeConnection(self):
        self.con.commit()
        self.con.close()
        self.cur.close()
        
    def discardChanges(self):
        pass
database=TaskDBase()
database.setupDbase()