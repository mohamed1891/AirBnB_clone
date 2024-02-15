#!/usr/bin/python3

# Command interpreter module
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


# HBNBCommand class
class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    def default(self, line):
        """Catch commands if nothing else matches then"""

        self.precmd(line)

    def precmd(self, line):
        """Intercepts commands to test for class.syntax()"""

        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def new_method(self):
        self.storage

    def do_create(self, line):
        args = line.split()
        if len(args) < 2:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[args[0]](*args[1:])
            storage.save(new_instance)
            print(new_instance.id)

    def do_show(self, arg):
        """Show a specific class"""
        words = arg.split()
        if len(words) != 2:
            print("** class name missing **")
            return
        if words[0] not in self.storage.classes():
            print("** class doesn't exist **")
            return
        cls = getattr(models, words[0])
        obj = self.storage.get(cls, words[1])
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        try:
            args = self.parse_args(arg)
            class_name = args[1]
            obj_id = args[2]
            storage.destroy(class_name, obj_id)
            print("{} with id {} was destroyed".format(class_name, obj_id))
        except (IndexError, KeyError, TypeError) as e:
            print("Error: {}".format(e))
        except Exception as e:
            print("Error: {}".format(e))

    def do_all(self, line):
        """Display all objects by type"""
        args = line.split()
        if len(args) == 1:
            print("** class name missing **")
            return

        class_name = args[1]
        if class_name not in classes:
            print("** class doesn't exist **")
            return 

        objects = storage.all().values()
        if not objects:
            print("** no instance found **")
            return

        instances = [obj for obj in objects if type(obj).__name__ == class_name]
        if not instances:
            print("** no instance found **")
            return

        for instance in instances:
            print(instance)

    def do_update(self, arg):
        """Update a BaseModel instance"""
        words = arg.split()
        if len(words) < 2:
            print("** class name missing **")
            return
        if words[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(words) < 3:
            print("** instance id missing **")
            return
        if not storage.exists(words[0], words[2]):
            print("** no instance found **")
            return
        attr_name = words[1]
        attr_value = " ".join(words[3:])
        storage.update(words[0], words[2], {attr_name: attr_value})
        print("** updated successfully **")

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

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""

        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
