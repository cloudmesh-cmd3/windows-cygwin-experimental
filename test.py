#
# demo to start os command
#
# from subprocess import check_output

# cmd = r'C:\cygwin64\bin\ps.exe'
# output = check_output(cmd)
# print (output)


import subprocess, glob


class Shell(object):

    cygwin_path = r'C:\cygwin64\bin'


    command = {{}}
    """

    

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

        exe_paths = glob.glob(cls.cygwin_path + r'\*.exe')         # list all *.exe in  cygwin path, use glob
        for c in exe_paths:
            exe = c.split('\\')
            name = exe[3].split('.')[0]
            #command['windows'][name] = "{:}\{:}.exe".format(cygwin_path, c)
            cls.command['windows'][name] = c

    @classmethod
    def list(cls):
        # prins all available commands in cygwin bin
        #TODO
        pass

    @classmethod
    def operating_system(cls):
        return 'windows'  # just fixing fornow us sys to finw out


    @classmethod
    def _execute(cls, cmd, arguments, capture=True, verbose=False):
        """Run Shell command

        :param cmd: command to run
        :param arguments: we dont know yet
        :param capture: if true returns the output
        :return:
        """

        operating_system = 'windows' # just a fake thing
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
                    os_command = os_command + " " + arguments
            print os_command
            result = subprocess.check_output(os_command).strip()
        else:
            result = subprocess.check_call(os_command).strip()
        return result


def main():
    shell = Shell()

    r = shell._execute('ps', "arg") # copy line replace
    print r

    r = shell._execute('whoami', "arg")
    print "-----{:}-----".format(r)

    r = shell._execute('ls', ["-l", "-a"])
    print "-----{:}-----".format(r)

    r = shell._execute('ls', "-l -a")
    print "-----{:}-----".format(r)

if __name__ == "__main__":
    main()

