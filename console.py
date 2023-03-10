#!/usr/bin/python3
"""Defines the entry point to the CLI"""
import cmd


class HBNBCommand(cmd.Cmd):
    """CLI commands class"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing if empty line is passed"""
        pass

    def do_quit(self, arg):
        """Quit dispatch method"""
        return True

    def do_EOF(self, arg):
        """End of file signal to exit the CLI"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
