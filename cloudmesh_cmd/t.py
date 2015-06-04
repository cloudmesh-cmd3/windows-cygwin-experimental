import sys

__author__ = 'PauloR'

import re
import subprocess
import os
import platform

path = 'C:\\cygwin64\\bin\\lol.exe'

#print(path.split('\\'))

import glob

r = glob.glob('*.py')
#print r

#if operating_system = 'cmd':
#env = 'C:\\cygwin64\\bin\\'
#os.path.join(env)
"""
print "ls -l -a".split()
print sys.platform
print os.name
print platform.system()
print platform.uname()
"""
# if operating_system = 'cygwin' or operating_system = 'linux'
#    pass

#result = subprocess.check_output('uname -o').strip()
#print result

#print result
"""
result = 'cmd'
try:
    # if the os is linux uname -o returns GNU/Linux
    result = subprocess.check_output('uname -o').strip()
except Exception: #if os is windows then an exception is caught
    pass
print ("os " + result)
"""
#os.environ["PATH"] = os.environ["PATH"] + ';C:\\Program Files (x86)\\Git\\bin'
print os.environ["PATH"]
print platform.system()
p = os.getcwd() + r'\bin'
result = subprocess.check_output(p + '\\pwd').strip()
print p