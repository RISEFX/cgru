#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import sys
import time
from datetime import datetime

sys.path.append(os.getcwd())

import afstatsrv

from optparse import OptionParser
Parser = OptionParser(usage="%prog [Options]\nType \"%prog -h\" for help", version="%prog 1.0")
Parser.add_option('-t', '--table',    dest='table',    type   = 'string',     default = None,       help = 'Table: logs, jobs, tasks')
Parser.add_option(      '--min',      dest='timemin',  type   = 'string',     default = None,       help = 'Record minimum time: 2026-02-23')
Parser.add_option(      '--max',      dest='timemax',  type   = 'string',     default = None,       help = 'Record maximum time: 2026-03-08')
Parser.add_option(      '--select',   dest='select',   type   = 'string',     default = 'folder',   help = 'Select column')
Parser.add_option(      '--favorite', dest='favorite', type   = 'string',     default = 'username', help = 'Favourite column')
Parser.add_option('-V', '--verbose',  dest='verbose',  action = 'store_true', default = False,      help = 'Verbose mode')
Parser.add_option('-D', '--debug',    dest='debug',    action = 'store_true', default = False,      help = 'Debug mode')
Options, Args = Parser.parse_args()

r = afstatsrv.Requests()

TimeMin = Options.timemin
TimeMax = Options.timemax
if TimeMin:
    TimeMin = int(datetime.fromisoformat(TimeMin).timestamp())
if TimeMax:
    TimeMax = int(datetime.fromisoformat(TimeMax).timestamp())

def request(i_name, i_args = None):
    func = 'req_' + i_name
    print('\n' + '#'*8 + ' ' + func)
    print(json.dumps(i_args, indent=4))
    out = dict()
    getattr(r, func)(i_args, out)
    print('# out:')
    print(json.dumps(out, indent=4))
    return out

def showDemo():
    out = request('init')
    folder = out['folders'][0]
    print('# Folder = "%s"' % folder)

    args = dict()
    args['select'] = Options.select
    args['folder'] = folder
    out = request('get_jobs_folders', args)

    args['favorite'] = Options.favorite
    out = request('get_jobs_table', args)

    out = request('get_tasks_folders', args)

    out = request('get_tasks_table', args)

    args['interval'] = 1000000
    out = request('get_tasks_folders_graph', args)

    out = request('get_tasks_graph', args)

    args['folder'] = '/xxx'
    out = request('folder_delete', args)

    args['order'] = 'time'
    out = request('get_logs_table', args)

if Options.table:
    args = dict()
    args['table']    = Options.table
    args['select']   = Options.select
    args['favorite'] = Options.favorite
    args['folder']   = '/'
    if TimeMin:
        args['time_min'] = TimeMin
    if TimeMax:
        args['time_max'] = TimeMax
    print(args)
    reqest_name = 'get_%s_table' % Options.table
    out = request(reqest_name, args)
else:
    showDemo()
