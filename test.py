#
# demo to start os command
#
# from subprocess import check_output

# cmd = r'C:\cygwin64\bin\ps.exe'
# output = check_output(cmd)
# print (output)


import subprocess


class Shell(object):

    command = {
        'windows': {
            'ps': r'C:\cygwin64\bin\ps.exe',
            'whoami': r'C:\cygwin64\bin\whoami.exe',
            'ls' : r'C:\cygwin64\bin\ls.exe'
        },
        'linux': {
            'ps' : 'ps'
        }
        }


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

            #subprocess.check_output(cmd, arguments???)
            you get it?
            you need to find out how to do that
            ok,
            but the parameters must go on check or execute? isnt the chelk an implicit execute?
            i dpnt know you will figure out.ut lets do this to github
            result =  subprocess.check_output(os_command).strip()
        else:
            result = subprocess.check_call(os_command????).strip()
        return result

look up hhow to pass arguments in documentation and implement


def main():
    shell = Shell()

    r = shell._execute('ps', "arg") # copy line replace
    print r

    r = shell._execute('whoami', "arg")
    print "-----{:}-----".format(r)

    r = shell._execute('ls', "-l -a")
    print "-----{:}-----".format(r)

if __name__ == "__main__":
    main()

