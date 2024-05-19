#!/usr/bin/python3
import cmd
'''Command Line Interpreter'''


class HBNBCommand(cmd.Cmd):
    '''Command Line Interpreter'''
    prompt = '(hbnb) '

    def do_EOF(self, line):
        print("")
        return True

    def do_quit(self, line):
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
