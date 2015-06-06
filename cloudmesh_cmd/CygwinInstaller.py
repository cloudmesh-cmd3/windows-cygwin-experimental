import urllib
import os
import shutil
import subprocess
import getpass
import glob
import os

from subprocess import Popen



install_bat_file = """
REM do NOT run this file. Must be run cygwin-install.py instead. 
@ECHO OFF
SETLOCAL
  FOR /F %%D in ("%CD%") DO SET DRIVE=%%~dD

  SET DFLTSITE=http://mirror.csclub.uwaterloo.ca/cygwin/

  SET DFLTLOCALDIR=c:\Temp\cygwindownload
  SET DFLTROOTDIR=%DRIVE%\cygwin

  SET SITE=-s %DFLTSITE%
  SET LOCALDIR=-l %DFLTLOCALDIR%
  SET ROOTDIR=-R %DFLTROOTDIR%
  
REM add packages here
SET PACKAGES=-P emacs-w32,curl,openssh

REM installs cygwin
ECHO [INFO] C:\Temp\cygwindownload\setup.exe -q -D -L %SITE% %LOCALDIR% %PACKAGES%
C:\Temp\cygwindownload\setup.exe -q -D -L %SITE% %LOCALDIR% %PACKAGES%

REM removes Temp folder
rd /s /q "C:\Temp\"
ECHO [INFO] Cygwin installation is complete
"""

class Cygwin(object):

    dir_download = 'C:\\Temp\\cygwindownload'
    setup_url = 'https://cygwin.com/setup-x86.exe'
    setup_exe = dir_download + '\\setup.exe')

    @classmethod
    def info(cls):
        print "Version of Cygwin:", "TODO"
        print "Download Path:", "TODO"
        print "Package:" "TODO"
    
    @classmethod
    def install(cls):
        directory = 'C:\\Temp\\cygwindownload'
        if not os.path.isdir(dir_download):
           os.makedirs(dir_download)
        urllib.urlretrieve(setup_url, setup_exe)

        # TODO write install_bat_file to "cygwin-install.bat" I suggest to put this in
        # download dir and than do the popen from download dir 
        p = Popen("cygwin-install.bat")
        stdout, stderr = p.communicate()

    @classmethod
    def uninstall(cls):
        #looks for shortcuts in public and private Desktop
        data = {}
        data['username'] = getpass.getuser()
        desktop_private_path = 'C:\\Users\\{username}\\Desktop'.format(**data)
        desktop_public_path = 'C:\\Users\\Public\\Desktop\\'
        cygwing_shortcut_list = glob.glob(desktop_public_path + r'\Cygwin*.lnk')
        cygwing_shortcut_list += (glob.glob(desktop_private_path + r'\Cygwin*.lnk'))
        if cygwing_shortcut_list:
            for shortcut in cygwing_shortcut_list:
                data['shortcut'] = shortcut
                cmd = r'takeown /F "{shortcut}" /A'.format(data)
                #make the adminstrator the owner of the file
                print cmd
                subprocess.call(cmd, shell=True)
                os.remove(shortcut)
                #print cygwing_shortcut
        else:
            print "There are no cygwin shortcuts"

        #looks for folders with cygwin in their names
        cygwing_folder_list = glob.glob('C:\\*cygwin*')
        if cygwing_folder_list:
            for folder in cygwing_folder_list:
                data['folder'] = folder
                cmd = r'takeown /F "{folder}" /A /R'.format(**data)
                #make the adminstrator the owner of the file.
                subprocess.call(cmd, shell=True)
                shutil.rmtree(folder)
        else:
            print "There are no cygwin folders"


"""
    Usage:

        CygwinInstaller install
        CygwinInstaller uninstall
        CygwinInstaller info
"""

# implement a way to call this. use argpasre
        
