#!/usr/bin/python3

# Import the modules
import cmd
import re
import json
from models import storage
from models.engine.file_storage import FileStorage

# Define the class HBNBCommand that inherits from cmd.Cmd
class HBNBCommand(cmd.Cmd):
    # Class attribute that stores the custom prompt
    prompt = "(hbnb) "

    def __init__(self):
        super().__init__()
        self.storage = FileStorage()
        self.storage.reload()

    def default(self, line):
        # Call the _precmd method to check for class syntax
        self._precmd(line)

    def _precmd(self, line):
        match = re.search(r"^(\w+)\.(\w+)\((.*)\)$", line)
        if not match:
            return line

        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)

        match_uid_and_args = re.search(r'^"([^"]+)"(?:, (.*))?$', args)
        # If match, extract the id and the other arguments
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        # Otherwise, assume the argument is the id
        else:
            uid = args
            attr_or_dict = None

        attr_and_value = ""
        # If the method is update and there are other arguments
        if method == "update" and attr_or_dict:
            # Use regular expressions to match the pattern {<dictionary>}
            match_dict = re.search(r'^({.*})$', attr_or_dict)
            # If match, call the update_dict method with the dictionary
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(r'^(?:"([^"]+)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(1) or "") + " " + (match_attr_and_value.group(2) or "")

        command = method + " " + classname + " " + uid + " " + attr_and_value
        # Call the onecmd method with the command
        self.onecmd(command)
        # Return the command
        return command

    # Method to update an instance with a dictionary
    def update_dict(self, classname, uid, s_dict):
        # Replace single quotes with double quotes in the string
        s = s_dict.replace("'", '"')
        # Load the string as a JSON object and convert it to a dictionary
        d = json.loads(s)
        # If the class name is missing, print an error message
        if not classname:
            print("** class name missing **")
        # If the class name is not valid, print an error message
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        # If the id is missing, print an error message
        elif uid is None:
            print("** instance id missing **")
        # Otherwise, proceed with the update
        else:
            # Construct the key with the class name and id
            key = "{}.{}".format(classname, uid)
            # If the key is not in the storage, print an error message
            if key not in storage.all():
                print("** no instance found **")
            # Otherwise, update the instance attributes with the dictionary values
            else:
                # Get the valid attributes for the class name
                attributes = storage.attributes()[classname]
                # Loop through the dictionary items
                for attribute, value in d.items():
                    # If the attribute is valid, convert the value to the appropriate type
                    if attribute in attributes:
                        setattr(storage.all()[key], attribute, value)
                # Save the instance to the file
                storage.all()[key].save()


    # Method to handle the EOF (End Of File) character
    def do_EOF(self, line):
        # Print a new line
        print()
        # Return True to exit the program
        return True

    # Method to exit the program
    def do_quit(self, line):
        # Return True to exit the program
        return True

    # Method to do nothing on an empty line
    def emptyline(self):
        # Pass
        pass

    # Method to create an instance of a class
    def do_create(self, line):
        if not line:
            print("** class name missing **")
            return

        class_name = line.strip()
        if class_name not in self.storage.classes():
            print("** class doesn't exist **")
            return

        new_instance = self.storage.classes()[class_name]()
        new_instance.save()
        print(new_instance.id)

    # Method to show the string representation of an instance
    def do_show(self, line):
        if not line:
            print("** class name missing **")
            return

        words = line.split()
        if words[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(words) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(words[0], words[1])
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, line):
        # If the line is empty, print an error message
        if line == "" or line is None:
            print("** class name missing **")
        # Otherwise, split the line by spaces
        else:
            words = line.split(' ')
            # If the first word is not a valid class name, print an error message
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            # If the second word is missing, print an error message
            elif len(words) < 2:
                print("** instance id missing **")
            # Otherwise, delete the instance
            else:
                # Construct the key with the class name and id
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                # Otherwise, delete the instance from the storage
                else:
                    del storage.all()[key]
                    # Save the changes to the file
                    storage.save()

    # Method to print all string representation of all instances based or not on the class name
    def do_all(self, line):
        if not line:
            print('\n'.join(str(instance) for instance in storage.all().values()))
        elif line in storage.classes():
            class_name = line.strip()
            instances = [str(instance) for instance in storage.all().values() if instance.__class__.__name__ == class_name]
            print('\n'.join(instances))
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    # Create an instance of the HBNBCommand class and start the command loop
    HBNBCommand().cmdloop()
