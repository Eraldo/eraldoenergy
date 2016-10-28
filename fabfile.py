from fabric.api import env, local, require

project_name = 'eraldoenergy'


def backup():
    """fab [environment] backup"""
    require('environment')
    if env.environment == "development":
        local('pg_dump -Fc {project} > backups/{project}-{environment}_`date +%Y-%m-%d_%H%M%S`.dump'.format(
            project=project_name, environment=env.environment))
    elif env.environment in ['staging', 'production']:
        local(
            'curl -o backups/{project}-{environment}_`date +%Y-%m-%d_%H%M%S`.dump `heroku pg:backups public-url --app {app}`'.format(
                project=project_name, environment=env.environment, app=env.app))


def deploy():
    """fab [environment] deploy"""
    require('environment')
    maintenance_on()
    push()
    migrate()
    maintenance_off()
    ps()


def maintenance_on():
    """fab [environment] maintenance_on"""
    require('environment')
    local('heroku maintenance:on --app %s' % env.app)


def maintenance_off():
    """fab [environment] maintenance_off"""
    require('environment')
    local('heroku maintenance:off --app %s' % env.app)


def push():
    """fab [environment] push"""
    require('environment')
    local('git push origin {branch}'.format(branch=env.branch))


def migrate(app=None):
    """fab [environment] migrate"""
    require('environment')
    if env.environment == "development":
        if app is not None:
            local('python manage.py migrate %s' % app)
        else:
            local('python manage.py migrate')
    else:
        if app is not None:
            local('heroku run python manage.py migrate %s --app %s' % (app, env.app))
        else:
            local('heroku run python manage.py migrate --app %s' % env.app)


def ps():
    """fab [environment] ps"""
    require('environment')
    local('heroku ps --app %s' % env.app)


def open():
    """fab [environment] open"""
    require('environment')
    local('heroku open --app %s' % env.app)


def development():
    """fab development [command]"""
    env.environment = 'development'
    env.app = 'local'
    env.branch = 'development'


def staging():
    """fab staging [command]"""
    env.environment = 'staging'
    env.app = 'eraldoenergy-staging'
    env.branch = 'staging'


def production():
    """fab production [command]"""
    env.environment = 'production'
    env.app = 'eraldoenergy'
    env.branch = 'master'
