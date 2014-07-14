from fabric.api import env, roles

from fusionbox.fabric import fb_env
from fusionbox.fabric.django import stage, deploy

env.roledefs['live'] = ['fusionbox@demo.wid.gy']

fb_env.virtualenv = 'wid.gy'
fb_env.project_name = 'wid'
fb_env.tld = '.gy'
fb_env.vassal = 'wid.gy'

stage = roles('dev')(stage)
deploy = roles('live')(deploy)
