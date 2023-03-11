#!/usr/bin/python3
"""Defines the entry point to the CLI"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """CLI commands class"""

    prompt = "(hbnb) "
    __cls_dict = {
        "BaseModel",
        "User",
        "Place",
        "Review",
        "City",
        "Amenity",
        "State",
    }
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
        elif arg not in HBNBCommand.__cls_dict:
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
        elif args[0] not in HBNBCommand.__cls_dict:
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
