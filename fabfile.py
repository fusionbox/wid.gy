from fabric.api import env, roles, task


def dev():
    env.project_name = 'wid.gy.dev'
    env.vassal_name = 'wid_gy_dev'

    return ['fusionbox@widgy.dev.fusionbox.com']


def live():
    env.project_name = 'wid.gy'
    env.vassal_name = 'wid_gy'

    return ['fusionbox@wid.gy']


@task
@roles('live')
def deploy(branch='origin/live', force=False, backupdb=False):
    from fusionbox.fabric.django.new import deploy as base_deploy
    base_deploy(branch, force, backupdb)


@task
@roles('dev')
def stage(branch='HEAD', qad=True, force=False, backupdb=False):
    from fusionbox.fabric.django.new import stage as base_stage
    base_stage(branch, qad, force, backupdb)


env.roledefs['dev'] = dev
env.roledefs['live'] = live

stage = roles('dev')(stage)
deploy = roles('live')(deploy)
