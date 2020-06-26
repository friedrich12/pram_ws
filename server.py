#from flask import Flask, render_template, request
from jinja2 import Template
import random
import string
import cherrypy
from os.path import abspath


CP_CONF = {
        '/dist': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': abspath('./dist') # staticdir needs an absolute path
        },
        '/dist/css': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': abspath('./dist/css')
        },
         '/dist/assets': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': abspath('./dist/assets')
        },
        '/dist/js': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': abspath('./dist/js')
        },
        '/dist/scripts': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': abspath('./dist/scripts')
        }
}


class PramWebServer(object):
    sample = False
    
    def getpage(self, path):
        with open(path) as file:
            data = file.readlines()
            page = ''.join(data)
            return str(page)

    @cherrypy.expose
    def index(self):
        return self.getpage("index.html")

    @cherrypy.expose
    def index2(self):
        data = self.getpage("dist/index.html")
        if self.sample == True:
            tm = Template(str(data))
            job = "SAMPLE"
            out = "LALAL"
            rez = tm.render(jobname=job, output=out)
            return str(rez)
        else: 
            tm = Template(str(data))
            job = "NONE RUNNING"
            out = "NO JOBS"
            rez = tm.render(jobname=job, output=out)
            return str(rez) 

    @cherrypy.expose
    def simple(self):
        with open("index.html") as file:
            data = file.readlines()
            self.sample = True
            return data
    

if __name__ == '__main__':
    cherrypy.quickstart(PramWebServer(),'/', CP_CONF)
