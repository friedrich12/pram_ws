import random
import string
import cherrypy


class PramWebServer(object):
    @cherrypy.expose
    def hello(self):
        return "Hello World!"

    @cherrypy.expose
    def simple(self):
        return "Running simple test"


if __name__ == '__main__':
    cherrypy.quickstart(PramWebServer())
