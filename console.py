#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self,arg):
        """EOF to exit the program"""
        print("")
        return True

    def do_help(self, arg):
        """Provide help messages"""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Do nothing when empty linr is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
