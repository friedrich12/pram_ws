import random
import string
import cherrypy
from os.path import abspath

CP_CONF = {
        '/dist': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': abspath('./dist') # staticdir needs an absolute path
            }
        }


class PramWebServer(object):
    @cherrypy.expose
    def index(self):
        with open("index.html") as file:
            data = file.readlines()
            page = ''.join(data)
            return str(data)

    @cherrypy.expose
    def simple(self):
        return "Running simple"
    

if __name__ == '__main__':
    cherrypy.quickstart(PramWebServer(),'/', CP_CONF)
