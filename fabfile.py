from fabric.api import env, roles

from fusionbox.fabric.django.new import stage, deploy


def dev():
    env.project_name = 'wid.gy.dev'
    env.vassal_name = 'wid_gy_dev'

    return ['fusionbox@widgy.dev.fusionbox.com']


def live():
    env.project_name = 'wid.gy'
    env.vassal_name = 'wid_gy'

    return ['fusionbox@wid.gy']


env.roledefs['dev'] = dev
env.roledefs['live'] = live

stage = roles('dev')(stage)
deploy = roles('live')(deploy)

