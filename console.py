#!/usr/bin/python3
"""
console module for the project
"""

import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User


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
            print("** class name missing **")
        else:
            try:
                new_obj = eval(arg_split[0])()
            except NameError:
                print("** class doesn't exist **")
            else:
                new_obj.save()
                print(new_obj.id)

    def do_show(self, args):
        """
        Prints string rep of an instance
        """
        arg_split = args.split()

        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = arg_split[0]
                instance_id = arg_split[1]
            except IndexError:
                print("** instance id missing **")
                return

            key = f"{class_name}.{instance_id}"
            obj = models.storage.all().get(key)

            if not obj:
                print("** class doesn't exist **")
                return
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
                print("** class name missing **")
            elif not obj:
                print("** instance id missing **")
            else:
                del models.storage.all()[f"{class_name}.{instance_id}"]
                models.storage.save()

    def do_all(self, args):
        """
        Prints all string rep of all instances
        """
        arg_split = args.split()
        objects = models.storage.all()
        if not arg_split:
            print([str(obj) for obj in objects.values()])
        elif arg_split[0] in ["BaseModel"]:
            print([str(obj) for obj in objects.values()])
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        Updates instances based on class name and id
        """
        arg_split = args.split()

        if not args:
            print("** class name missing **")
            return
        if len(arg_split) < 2:
            print("** instance id missing **")
            return
        if len(arg_split) < 3:
            print("** attribute name missing **")
            return
        if len(arg_split) < 4:
            print("** value missing **")
            return
        class_name, instance_id = arg_split[0], arg_split[1]
        attr_name, attr_value = arg_split[2], arg_split[3]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        obj = models.storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        setattr(obj, attr_name, attr_value)
        obj.save


if __name__ == '__main__':
    HBNBCommand().cmdloop()
