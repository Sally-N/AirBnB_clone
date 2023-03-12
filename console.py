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
                    del storage.all()key[]
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg != "":
            args = arg.split('')
            if args[0] not in storage.classes:
                print("** class doesn't exist **")
            else:
                string_rep = [str(obj) for key, obj in storage.all().items()
                        if type(obj).obj_cls_name == args[0]]
                print(string_rep)
        else:
            new_s = [str(obj) for key, obj in storage.all().items]
            print(new_s)

    def do_update(self, arg):
        """Updates an instance based on classname and id"""
        if arg == "" or arg is None:
            print("** clase name is missing **")
            return

        regex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(regex, arg)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id is missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name mising **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()key], attriute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
