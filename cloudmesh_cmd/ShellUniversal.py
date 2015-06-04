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

    '''

    big question for badi and others

    how do we now define dynamically functions based on a list that we want to support

    what we want is where args are multiple unlimited parameters to the function

    def f(args...):
        name = get the name from f
        a = list of args...

        cls.execute(cmd, arguments=a, capture=True, verbose=False)

    commands = ['ps', 'ls', ..... ]
    for c in commands:
        generate this command and add to this class dynamically

    or do something more simple

    ls = cls.execute('cmd', args...)   # i think that is what badi does

    '''
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
    def which(cls, command):
        t = cls.ttype()
        if 'windows' in t and cls.command_exists(name):
            return cls.command['windows'][name]
        elif 'linux' in t:
            cmd = ["which",command]
            result = subprocess.check_output(cmd).strip()
            if len(result) == 0:
                return None
            else
                return result

    @classmethod
    def command_exists(cls, name):
        t = cls.ttype()
        if 'windows' in t:
            #only for windows
            cls.find_cygwin_executables()
            return name in cls.command['windows']
        elif 'linux' in t:
            r = which(name)
            return r

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

    @classmethod
    def mkdir(cls, newdir):
        """works the way a good mkdir should :)
        - already exists, silently complete
        - regular file in the way, raise an exception
        - parent directory(ies) does not exist, make them as well
        """
        """http://code.activestate.com/recipes/82465-a-friendly-mkdir/"""
        _newdir = path_expand(newdir)
        if os.path.isdir(_newdir):
            pass
        elif os.path.isfile(_newdir):
            raise OSError("a file with the same name as the desired "
                          "dir, '%s', already exists." % _newdir)
        else:
            head, tail = os.path.split(_newdir)
            if head and not os.path.isdir(head):
                os.mkdir(head)
            if tail:
                os.mkdir(_newdir)

    
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

