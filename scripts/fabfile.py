#encoding:utf-8
"""
author:tianyu0915@gmail.com
version:1.2
datetime:2013-08-19

"""
import time
from datetime import datetime
import requests
import sys
import os
from cuisine import *
from fabric.api import *
from cuisine import *
from fabric.contrib.project import rsync_project, upload_project
from fabric.operations import get,put
from fabric.contrib.files import  exists
today = time.strftime("%Y-%m-%d-%H%M", time.localtime())

env.name            = 'prphoto'
env.hosts           = ['linode.t-y.me']
env.user            = 'ubuntu'
env.path            = '/srv/{}'.format(env.name)
env.nginx_conf      = '/usr/local/nginx/conf/vhost/{}'.format(env.name)
env.repositories    = 'git@github.com:titainium/PRPHOTO.git'
env.db_name         = env.name

def dump_db():
    tar_name = '{}.dump.{}.tar'.format(env.db_name,time.strftime("%Y-%m-%d-%H", time.localtime()))
    tar_fp  = os.path.join('/tmp/',tar_name)
    if not exists(tar_fp):
        with cd('/tmp'):
            run('rm -rf {}.dump*'.format(evn.db_name))
            run('mongodump -d {} -o buzz.dump'.format(env.db_name))
            run('tar -czvf {} {}.dump'.format(tar_name,env.db_name))

    get(tar_fp,'backup/')
    run('rm -rf /tmp/{}.dump*'.format(env.db_name))

def restart():
    """ restart the uwsgi & nginx """
    with mode_sudo():
        run('rm -rf /tmp/{}.log'.format(env.name))
        with cd(env.path):
            run('sudo rm -rf cache/*')
        
        for tname in ['buzz','buzz-taksk']:
            run('sudo supervisorctl restart {}'.format(tname))

        run('sudo nginx -s reload')
        run('ps -ef |grep {}'.format(env.name))
        run('tail /tmp/{}.log'.format(env.name))

def sync_code(tag=None):

    # backup nginx config
    with mode_sudo():
        if exists(env.nginx_conf):
            get(env.nginx_conf,'backup/{}.nginx-{}'.format(env.name,today))
        put('config/%s' %env.name,env.nginx_conf)

        with cd(env.path):
            run('sudo git checkout -- .')
            run('sudo git pull origin master')
            if tag:
                run('sudo git fetch --tags')
                run('sudo git checkout {0}'.format(tag))
            else:
                try:
                    run('sudo git branch {0}'.format(today))
                except:
                    pass
                run('sudo git checkout {0}'.format(today))

def init():
    with mode_sudo():
        if not exists('/srv/'):
            run('mkdir /srv/')
        with cd('/srv/'):
            try:
                run('git clone %s' %env.repositories)
            except:
                pass

def setup():
    with mode_sudo():
        if not exists(env.path):
            init()
        
        with cd(env.path):
            with cd('scripts'):
                run('sudo sh setupenv.sh')

def deploy():
    sync_code()
    setup()
    restart()

