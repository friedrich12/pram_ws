#from flask import Flask, render_template, request
from jinja2 import Template
import random
import string
import cherrypy
from os.path import abspath
from render import Render

CP_CONF = {
        '/': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': abspath('./dist') # staticdir needs an absolute path
        },
        '/css': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': abspath('./dist/css')
        },
         '/assets': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': abspath('./dist/assets')
        },
        '/js': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': abspath('./dist/js')
        },
        '/scripts': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': abspath('./dist/scripts')
        }
}


class PramWebServer(object):

    @cherrypy.expose
    def index(self):
        return self.getpage("index.html")

    @cherrypy.expose
    def index2(self):
        data = self.getpage("dist/index.html")
        tm = Template(str(data))
        job = "NONE RUNNING"
        out = "NO JOBS"
        rez = tm.render(jobname=job, output=out)
        return str(rez) 

    @cherrypy.expose
    def simple(self):
       name = "NAME"
       out = "LALALA"
       render.setjob(name,out) 
    

if __name__ == '__main__':
    cherrypy.quickstart(PramWebServer(),'/', CP_CONF)
