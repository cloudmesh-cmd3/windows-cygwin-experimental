#! /usr/bin/env python

from cmd import Cmd
from mixin import MixIn, makeWithMixins, makeWithMixinsFromString
from plugins import *
from plugins import get_plugins
import sys

class Shell(Cmd):

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
        print "Hello, %s" % name

    def do_EOF(self, args):
        """
        Usage:
            EOF

        Command to the shell to terminate reading a script.
        """
        return True

    def do_quit(self, args):
        """
        Usage:
            quit

        Action to be performed whne quit is typed
        """
        sys.exit()

    do_q = do_quit


def main():
    plugins = get_plugins()
    SuperShell = makeWithMixins(Shell, plugins)
    shell = SuperShell()
    shell.prompt = '> '
    shell.cmdloop('Welcome to the Cloudmesh Shell')

if __name__ == '__main__':
    main()
