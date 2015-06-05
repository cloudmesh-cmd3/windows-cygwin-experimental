
import shutil
import subprocess
import getpass
import glob
import os

#looks for shortcuts in public and private Desktop
username = getpass.getuser()
desktop_private_path = 'C:\\Users\\' + username + '\\Desktop'
desktop_public_path = 'C:\\Users\\Public\\Desktop\\'
cygwing_shortcut_list = glob.glob(desktop_public_path + r'\Cygwin*.lnk')
cygwing_shortcut_list += (glob.glob(desktop_private_path + r'\Cygwin*.lnk'))
if cygwing_shortcut_list:
    for shortcut in cygwing_shortcut_list:
        cmd = r'takeown /F "' + shortcut + r'" /A' #make the adminstrator the owner of the file
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
        cmd = r'takeown /F "' + folder + r'" /A /R' #make the adminstrator the owner of the file.
        subprocess.call(cmd, shell=True)
        shutil.rmtree(folder)
else:
    print "There are no cygwin folders"


