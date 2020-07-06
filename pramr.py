#from flask import Flask, render_template, request
from jinja2 import Template
import random
import pram
import string
import sys
import cherrypy
from os.path import abspath
from render import Render

#pram stuff
from pram.data   import GroupSizeProbe, ProbeMsgMode
from pram.entity import Group, GroupQry, GroupSplitSpec, Site
from pram.rule   import GoToRule, DiscreteInvMarkovChain, TimeInt
from pram.sim    import Simulation


class PramRunner(object):
    def simple(self):
        progress_flu_rule = DiscreteInvMarkovChain('flu-status', { 's': [0.95, 0.05, 0.00], 'i': [0.00, 0.50, 0.50], 'r': [0.10, 0.00, 0.90] })
        # s - susceptible
        # i - infectious
        # r - recovered

        sites = { 'home': Site('h'), 'work': Site('w') }

        probe_grp_size_flu = GroupSizeProbe.by_attr('flu', 'flu-status', progress_flu_rule.get_states(), msg_mode=ProbeMsgMode.DISP, memo='Mass distribution across flu status')
        probe_grp_size_site = GroupSizeProbe.by_rel('site', Site.AT, sites.values(), msg_mode=ProbeMsgMode.DISP, memo='Mass distribution across sites')


    # ----------------------------------------------------------------------------------------------------------------------
    # (1) Simulations testing the basic operations on groups and rules:

        # (1.1) A single-group, single-rule (1g.1r) simulation:
        s = Simulation()
        s.add_rule(progress_flu_rule)
        s.add_probe(probe_grp_size_flu)
        s.add_group(Group('g0', 1000, { 'flu-status': 's' }))
        sys.stdout = open('out.dat', 'w')
        s.run(24)
        sys.stdout.close()
        
        with open('out.dat') as file:
            data = file.readlines()
            return str(data).replace("\n'","<br>")

