#
# demo to start os command
#
from subprocess import check_output

cmd = r'C:\cygwin64\bin\ps.exe'
output = check_output(cmd)
print (output)


import subprocess

class Shell (object)

    @classmethod
    def _execute(cls, cmd, arguments, capture=True):
    """Run a shell command
    :param cmd: the command to run as a list of arguments ????
    :param capture: capture the output
    """

    if capture:
      return subprocess.check_output(cmd)????
    else:
      return subprocess.check_call(cmd)????


