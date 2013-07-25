#encoding:utf-8
import datetime
import sys
import os
from fabric.api import *
#from cuisine import *
from fabric.contrib.project import rsync_project, upload_project
from fabric.operations import get,put
from fabric.contrib.files import  exists
d = datetime.datetime.today()
today = '{0}{1}{2}-{3}{4}'.format(d.year,d.month,d.day,d.hour,d.minute)
print today

env.hosts = ['pythoner.net']
env.user = 'root'
path = '/home/pythoner.net'

def mysqldump():
    today = '{0}{1}{2}{3}'.format(d.year,d.month,d.day,d.hour)
    dbs = ['pythoner_db']
    for db in dbs:
        file_name = "{0}_{1}.sql".format(db,today)
        if not exists('/tmp/{0}'.format(file_name)):
            run("mysqldump -hlocalhost -uroot  %s> /tmp/%s" %(db,file_name))

        with cd('/tmp/'):
            if not exists('{0}.tar'.format(file_name)):
                run('tar -czvf {0}.tar {0}'.format(file_name))
            get('/tmp/{0}.tar'.format(file_name),'~/Dev/vps/sqls/')
            run('rm -rf pythoner*.sql')
            run('rm -rf pythoner*.tar')

def mysqlrestore():
    dbs = ['pythoner_db']
    for host in env.hosts:
        for db in dbs:
            local("scp -rC %s.sql %s@%s:~/" %(db,env.user,host))

    #with run('mysql'):
    #    run('source ~/s.sql;')

def restart():
    """ restart the pythoner uwsgi & nginx """
        
    with cd(path):
        run('rm -rf pythoner/cache/*')
        with cd('scripts'):
            run('. env.sh')
            run('. uwsgi.sh')
            run('nginx -s reload')

def sync_code(tag=None):
    get('/etc/nginx/conf.d/pythoner','config/pythoner-{0}'.format(today))
    put('config/pythoner','/etc/nginx/conf.d/pythoner')
    with cd(path):
        run('git checkout -- .')
        run('git checkout production')
        run('git pull origin production')
        if tag:
            run('git checkout {0}'.format(tag))
        else:
            run('git branch {0}'.format(today))
            run('git checkout {0}'.format(today))

    get('/www/pythoner/settings.py','config/settings-{0}.py'.format(today))
    put('../pythoner/settings.py','/www/pythoner/settings.py')

def sync_sitemap():
    if exists('/www/pythoner/static/sitemap.html'):
        get('/www/pythoner/static/sitemap.xml','config/sitemap-{0}.xml'.format(today))
    put('config/sitemap.xml','/www/pythoner/static/sitemap.xml')

def migrate(app=None):
    with cd(env.path):
        with cd('pythoner'):
            if app:
                run('python manage.py  migrate {0}'.format(app))
            else:
                run('python manage.py migrate')
        
def setup():
    if not exists('/www/pythoner'):
        run('mkdir /www/')
        with cd('/www/'):
            run('ln -s /home/pythoner.net/pythoner .')

    with cd(path):
        with cd('scripts'):
            run('source setupenv.sh')

def deploy():
    sync_code()
    setup()
    migrate()
    restart()



