#
# demo to start os command
#
# from subprocess import check_output

# cmd = r'C:\cygwin64\bin\ps.exe'
# output = check_output(cmd)
# print (output)


import subprocess
import glob
import json
import platform
import os

class Shell(object):

    cygwin_path = 'bin' #i copied fom C:\cygwin\bin

    command = {
        'windows': {},
        'linux':{},
        'darwin': {}
    }

    def __init__(cls):
        if cls.operating_system() == "windows":
            cls.find_cygwin_executables()
        else:
            pass
            # implement for cmd, for linux we can just pass as it includes everything
            
    @classmethod
    def find_cygwin_executables(cls):
        """
        find the executables 
        """
        exe_paths = glob.glob(cls.cygwin_path + r'\*.exe')
        print cls.cygwin_path
        # list all *.exe in  cygwin path, use glob
        for c in exe_paths:
            exe = c.split('\\')
            name = exe[1].split('.')[0]
            #command['windows'][name] = "{:}\{:}.exe".format(cygwin_path, c)
            cls.command['windows'][name] = c


    @classmethod
    def terminal_type(cls):
        """
        returns  darwin, cygwin, cmd, or linux
        """
        what = platform.system().lower()

        kind = None

        if 'linux' in what:
            kind = 'linux'
        elif 'darwin' in what:
            kind = 'darwin'
        elif 'cygwin' in what:
            kind = 'cygwin'
        else:
            kind = 'cmd'

        return kind

    @classmethod
    def ttype(cls):
        t = cls.terminal_type()
        if 'linux' in t or 'darwin' in t or 'cygwin' in t:
            return 'linux'
        elif 'cmd' in t:
            return 'windows'

    @classmethod
    def command_exists(cls, name):
        t = cls.ttype()
        if 'windows' in t:
            #only for windows
            cls.find_cygwin_executables()
            return name in cls.command['windows']
        elif 'linux' in t:
            # r = which(name) we have this somewhere
            # lets just fake it and return True
            return True

    
    @classmethod
    def list_commands(cls):
        t = cls.ttype()
        if 'windows' in t:
            #only for windows
            cls.find_cygwin_executables()
            print '\n'.join(cls.command['windows'])
        else:
            print ("ERROR: this command is not supported for this OS")


    @classmethod
    def operating_system(cls):
        return platform.system().lower()


    @classmethod
    def execute(cls, cmd, arguments="", capture=True, verbose=False):
        """Run Shell command

        :param cmd: command to run
        :param arguments: we dont know yet
        :param capture: if true returns the output
        :return:
        """

        terminal_type = cls.ttype()
        #print cls.command

        if ('linux' in terminal_type):
            os_command = cmd
        elif 'cmd' in terminal_type: # for cmd
            if not cls.command_exists(cmd):
                print "ERROR: the command could not be found", cmd
                return
            else:
                os_command = cls.command[cls.operating_system()][cmd]

        if verbose:
            print os_command
        result = None
        if capture:
            if isinstance(arguments, list):
                arguments.insert(0, os_command)
                os_command = arguments
            elif isinstance(arguments, str):
                if arguments != "arg":
                    os_command = (os_command + " " + arguments).split()
            print os_command
            result = subprocess.check_output(os_command).strip()
        else:
            result = subprocess.check_call(os_command).strip()
        return result


    
def main():
    shell = Shell()

    print shell.terminal_type()
    
    r = shell.execute('pwd') # copy line replace
    print r

    #shell.list()

    #print json.dumps(shell.command, indent=4)

    # test some commands without args
    """
    for cmd in ['whoami', 'pwd']:
        r = shell._execute(cmd)
        print "---------------------"
        print "Command: {:}".format(cmd)
        print "{:}".format(r)        
        print "---------------------"
    """
    r = shell.execute('ls', ["-l", "-a"])
    print "-----{:}-----".format(r)

    r = shell.execute('ls', "-l -a")
    print "-----{:}-----".format(r)


if __name__ == "__main__":
    main()

