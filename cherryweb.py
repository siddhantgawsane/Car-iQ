import cherrypy
from sys import *

class WelcomePage:

	def index(self):
		return '''
			<h1> Welcome To Car-IQ </h1>
			<head> Smart cars for a smarter you </head>
			<form action="greetUser" method="POST">
	        	<br/>Username<input type="text" name="name" />
	        	<br/>Password <input type="password" name="pwd" />

	        	<br/><input type="submit" value="Login"/><input type="button" value="CANCEL"><br>
	        	</form>'''
	index.exposed = True
	def greetUser(self, name = None, pwd = None):
		if name:
			return "Hi %s, your pwd is %s" % (name, pwd)
		else:
               		return 'Please enter your name <a href="./">here</a>.'
	greetUser.exposed = True

import os.path
tutconf = os.path.join(os.path.dirname(__file__), 'tutorial.conf')

if __name__ == '__main__':
    cherrypy.quickstart(WelcomePage(), config=tutconf)
else:
    cherrypy.tree.mount(WelcomePage(), config=tutconf)



