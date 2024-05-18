#!/usr/bin/python3
"""
console module for the project
"""

import cmd
import models
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Command Class
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

    def do_create(self, args):
        """
        Creates instance, saves and prints its id
        """
        arg_split = args.split()

        if not args:
            print("** class name missing ***")
        else:
            try:
                new_obj = eval(arg_split[0])()
            except NameError:
                print("** class doesn't exist**")
            else:
                new_obj.save()
                print(new_obj.id)

    def do_show(self, args):
        """
        Prints string rep of an instance
        """
        arg_split = args.split()

        if not args:
            print("** class name missing**")
        else:
            try:
                class_name = arg_split[0]
                instance_id = arg_split[1] if len(arg_split) > 1 else None
            except IndexError:
                print("** instance id missing**")
                return

            obj = models.storage.all().get(f"{class_name}.{instance_id}")

            if not class_name:
                print("** class name missing**")
            elif not obj:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, args):
        """
        Destroys instances based on class name and id
        """
        arg_split = args.split()

        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = arg_split[0]
                instance_id = arg_split[1] if len(arg_split) > 1 else None
            except IndexError:
                print("** instance id missing **")
                return

            obj = models.storage.all().get(f"{class_name}.{instance_id}")

            if not class_name:
                print("**class name missing **")
            elif not obj:
                print("**no instance found **")
            else:
                del models.storage.all()[f"{class_name}.{instance_id}"]
                models.storage.save()

    def do_all(self, args):
        """
        Prints all string rep of all instances
        """
        arg_split = args.split()
        all_objects = models.storage.all().values()
        objects_list = []
        for obj in all_objects:
            objects_list.append(str(obj))

        if args and args.split()[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            print(objects_list)

    def do_update(self, args):
        """
        Updates instances based on class name and id
        """
        arg_split = args.split()

        if not args:
            print("** class name missing **")
            return

        try:
            class_name = arg_split[0]
            instance_id = arg_split[1] if len(arg_split) > 1 else None
            attr_name = arg_split[2] if len(arg_split) > 2 else None
            attr_value = arg_split[3] if len(arg_split) > 3 else None
        except IndexError:
            if len(arg_split) == 1:
                print("** instance id missing**")
            elif len(arg_split) <= 2:
                print("** attribute name missing**")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
