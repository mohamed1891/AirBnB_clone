#!/usr/bin/python3

# Command interpreter module
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models import storage
import shlex


# HBNBCommand class

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

# Creates a new instance of BaseModel
    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg not in ["BaseModel", "State", "City",
                         "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        # Prints the string representation of an instance
        args = shlex.split(arg)
        if not args or args[0] not in ["BaseModel", "State",
                                       "City", "Amenity", "Place", "Review"]:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        # Deletes an instance
        args = shlex.split(arg)
        if not args or args[0] not in ["BaseModel", "State",
                                       "City", "Amenity", "Place", "Review"]:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        # Prints all string representation of all instances
        args = shlex.split(arg)
        if not args or args[0] not in ["BaseModel", "State",
                                       "City", "Amenity", "Place", "Review"]:
            print(*map(str, storage.all().values()), sep='\n')
        else:
            class_name = args[0]
            instances = filter(lambda i: i.__class__.__name__ == class_name,
                               storage.all().values())
            instances = list(map(str, instances))
            print('\n'.join(instances))

    def do_update(self, arg):
        """Updates an instance"""
        args = shlex.split(arg)
        if not args or args[0] not in ["BaseModel", "State",
                                       "City", "Amenity", "Place", "Review"]:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                instance = storage.all()[key]
                setattr(instance, args[2], args[3])
                storage.save()

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command"""
        return True

    def do_EOF(self, arg):
        """EOF command"""
        return True

    def help_create(self):
        """Print help for create command"""
        print("Create a new instance of BaseModel, "
              "saves it, and prints the id")

    def help_show(self):
        """Print help for show command"""
        print("Prints the string representation "
              "of an instance based on the class name and id")

    def help_destroy(self):
        """Print help for destroy command"""
        print("Deletes an instance based on the class name and id")

    def help_all(self):
        """Print help for all command"""
        print("Prints all string represent in  "
              "all instances based or not on the class name")

    def help_update(self):
        """Print help for update command"""
        print("Updates an instance based on the class name and id")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
