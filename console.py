#!/usr/bin/python3
"""
console module for the project
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand Class
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
        """Do nothing when empty linr is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
