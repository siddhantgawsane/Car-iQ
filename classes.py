import os
from sqlobject import *

cariq = os.path.abspath('data.db')
if os.path.exists(cariq):
	os.unlink(cariq)
connection_string = 'mysql://siddhant:password123@host/' + cariq
connection = connectionForURI(connection_string)
sqlhub.processConnection = connection

class User(SQLObject):
     fname = StringCol(),
     password = StringCol()

User.createTable()

Person._connection.debug = True
u1 = User(fname = 'siddhant', password = 'password')

