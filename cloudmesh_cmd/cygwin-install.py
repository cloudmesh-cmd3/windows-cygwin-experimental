import urllib
import os

from subprocess import Popen


directory = 'C:\\Temp\\cygwindownload'
if not os.path.isdir(directory):
   os.makedirs(directory)
urllib.urlretrieve("https://cygwin.com/setup-x86.exe", directory + '\\setup.exe')

p = Popen("cygwin-install.bat")
stdout, stderr = p.communicate()
