#!/usr/bin/python3

# Import the modules
import cmd
import re
import json

# Define the class HBNBCommand that inherits from cmd.Cmd
class HBNBCommand(cmd.Cmd):
    # Class attribute that stores the custom prompt
    prompt = "(hbnb) "

    # Method to handle commands that do not match any predefined ones
    def default(self, line):
        # Call the _precmd method to check for class syntax
        self._precmd(line)

    # Method to intercept commands to test for class syntax
    def _precmd(self, line):
        # Use regular expressions to match the pattern <class name>.<method name>(<arguments>)
        match = re.search(r"^(\w+)\.(\w+)\((.*)\)$", line)
        # If no match, return the line as it is
        if not match:
            return line
        # Extract the class name, method name, and arguments from the match
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        # Use regular expressions to match the pattern "<id>" or "<id>", <other arguments>
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
            # Otherwise, use regular expressions to match the pattern "<attribute>" or "<attribute>", <value>
            match_attr_and_value = re.search(
                r'^(?:"([^"]+)")?(?:, (.*))?$', attr_or_dict)
            # If match, extract the attribute and value
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        # Construct the command with the class name, method name, id, and attribute and value
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
        # If the line is empty, print an error message
        if line == "" or line is None:
            print("** class name missing **")
        # If the line is not a valid class name, print an error message
        elif line not in storage.classes():
            print("** class doesn't exist **")
        # Otherwise, create an instance of the class
        else:
            # Instantiate an object of the class
            b = storage.classes()
            # Save the object to the file
            b.save()
            # Print the id of the object
            print(b.id)

    # Method to show the string representation of an instance
    def do_show(self, line):
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
            # Otherwise, show the instance
            else:
                # Construct the key with the class name and id
                key = "{}.{}".format(words[0], words[1])
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
                else:
                    print(storage.all()[key])

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
        # If the line is empty, print all instances
        if line == "" or line is None:
            # Create an empty list to store the string representations
            list_str = []
            # Loop through the storage
            for key, value in storage.all().items():
                # Append the string representation of each instance to the list
                list_str.append(str(value))
            # Print the list
            print(list_str)
        # If the line is a valid class name, print all instances of that class
        elif line in storage.classes():
            # Create an empty list to store the string representations
            list_str = []
            # Loop through the storage
            for key, value in storage.all().items():
                # If the instance belongs to the class, append the string representation to the list
                if value.__class__.__name__ == line:
                    list_str.append(str(value))
            # Print the list
            print(list_str)
        # If the line is not a valid class name, print an error message
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    # Create an instance of the HBNBCommand class and start the command loop
    HBNBCommand().cmdloop()
