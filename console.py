#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    # Class attribute that stores the custom prompt
    prompt = "(hbnb) "

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
    HBNBCommand().cmdloop()
