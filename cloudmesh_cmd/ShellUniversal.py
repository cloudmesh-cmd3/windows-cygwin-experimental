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
        'linux':{}
    }

    def __init__(cls):
        if cls.operating_system() == "windows":
            cls.find_cygwin_executables()
        else:
            pass
            # implement for cmd, for linux we can just pass as it includes everything
            

    """
    ahh is see you outcommented ;-)
    command = {
        'windows': {
            'ps': r'C:\cygwin64\bin\ps.exe',
            'whoami': r'C:\cygwin64\bin\whoami.exe',
            'ls' : "C:\\cygwin64\\bin\\ls.exe"
        },
        'linux': {
            'ps' : 'ps'
        }
    }
    """

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
        returns  cygwin, cmd, or bash
        """
        result = 'cmd'
        try:
            # if the os is linux uname -o returns GNU/Linux
            result = subprocess.check_output('uname -o').strip()
        except Exception: #if os is windows then an exception is caught
            pass
        if result == "GNU/Linux":
           result = "bash"
        elif result == "Cygwin":
            result = "cygwin"
        return result
    
    @classmethod
    def exists(cls, name): #only for windows
        cls.find_cygwin_executables()
        return name in cls.command['windows']
    
    @classmethod
    def list(cls): #only for windows
        cls.find_cygwin_executables()
        print '\n'.join(cls.command['windows'])
        # prins all available commands in cygwin bin
        #TODO
        pass

    @classmethod
    def operating_system(cls):
        return platform.system().lower()


    @classmethod
    def _execute(cls, cmd, arguments="", capture=True, verbose=False):
        """Run Shell command

        :param cmd: command to run
        :param arguments: we dont know yet
        :param capture: if true returns the output
        :return:
        """

        terminal_type = cls.terminal_type()
        #print cls.command

        if terminal_type == "cygwin" or cls.operating_system() == "linux":
            os_command = cmd
        elif terminal_type == "cmd": # for cmd
            os_command = cls.command[cls.operating_system()][cmd]
            if not cls.exists(cmd):
                print "ERROR: the command could not be found", cmd
                return

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
    
    r = shell._execute('pwd') # copy line replace
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
    r = shell._execute('ls', ["-l", "-a"])
    print "-----{:}-----".format(r)

    r = shell._execute('ls', "-l -a")
    print "-----{:}-----".format(r)


if __name__ == "__main__":
    main()

