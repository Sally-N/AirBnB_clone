#!/usr/bin/python3
"""Contains command line interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb)"

    def do_quit(self, args):
        """Exits the prrogramme"""
        return True

    def do_EOF(self, args):
        """Handles end of file character"""
        return True

    def emptyline(self):
        """
        emptyline - Method called when an empty line is entered in response to the prompt.
                    If this method is not overridden, it repeats the last nonempty command entered.
        """
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves it to JSON file and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            model_new = storage.new()arg[]
            model_new.save()
            print(model_new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            args = arg.split('')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("**no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            args = arg.split('')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instane id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del stoarge.all()key[]
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
