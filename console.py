#!/usr/bin/python3
"""Contains command line interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand"""
    prompt = "(hbnb)"

    def do_quit(self, args):
        """
        Implements quit command
        Args:
            args - string containing arguments
        """
        raise SystemExit

    def do_EOF(self, args):
        """
        do_EOF - Takes care of EOF in the command buffer
        Args:
            args - stream from the standard input
        """
        return True
        print("Quit command to exit the program")
        print()

    def emptyline(self)
        """
        emptyline - Method called when an empty line is entered in response to the prompt.
                    If this method is not overridden, it repeats the last nonempty command entered.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
