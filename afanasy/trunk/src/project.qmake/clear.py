#!/usr/bin/env python

import os
import shutil

store = ['.svn','build.sh','override.sh','clear.py','project.pro','win_build_mingw.cmd','win_build_msvc.cmd']
projects = ['libafanasy','libafnetwork','libafapi','libafqt','libafsql','libpyaf','cmd','server','render','talk','watch','monitor']

DEBUG = True
DEBUG = False

def delete( item):
   if os.path.isdir( item):
      print 'Deleting directory "%s"' % item
      if not DEBUG: shutil.rmtree( item)
   else:
      print 'Deleting file "%s"' % item
      if not DEBUG: os.remove( item)

for item in os.listdir('.'):
   if item in store: continue
   if item in projects:
      project = item
      for item in os.listdir( project):
         if item == ('%s.pro' % project) or item == '.svn': continue
         delete( os.path.join( project, item))
      continue
   delete( item)
