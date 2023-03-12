#!/usr/bin/python3
"""Defines the entry point to the CLI"""
import cmd
from models import storage


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

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in storage.cls_dict:
            print("** class doesn't exist **")
        else:
            obj = storage.cls_dict[arg](arg)
            storage.new(obj)
            storage.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in storage.cls_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            if "{}.{}".format(args[0], args[1]) not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in storage.cls_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            if "{}.{}".format(args[0], args[1]) not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()["{}.{}".format(args[0], args[1])]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split(" ")
        if len(arg) > 0 and arg not in storage.cls_dict:
            print("** class doesn't exist **")
        else:
            output = []
            for obj in storage.all().values():
                if args[0] == obj.__class__.__name__:
                    output.append(obj.__str__())
                elif len(arg) == 0:
                    output.append(obj.__str__())
            print(output)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] not in storage.cls_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            if "{}.{}".format(args[0], args[1]) not in storage.all():
                print("** no instance found **")
                return False
            elif len(args) < 3:
                print("** attribute name missing **")
                return False
            elif len(args) < 4:
                print("** value missing **")
                return False
            else:
                instance = storage.all()["{}.{}".format(args[0], args[1])]
                attr = args[2]
                value = args[3]
                if attr in instance.__class__.__dict__.keys():
                    cast_type = type(instance.__class__.__dict__[attr])
                    instance.__dict__[attr] = cast_type(value)
                else:
                    instance.__dict__[attr] = value
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
