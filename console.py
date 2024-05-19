#!/usr/bin/python3
'''command line interpreter'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''Command Line Interpreter'''
    prompt = '(hbnb) '

    def do_EOF(self, line):
        print("")
        return True

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
