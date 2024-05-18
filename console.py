#!/usr/bin/python3
"""

"""
import cmd


class HBNBCommand(cmd.Cmd):
    """

    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program"""
        return True

    def help_quit(self, arg):
        """"""
        print("Quit command to exit program")

    def emptyline(self):
        """Do nothing when empty linr is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
