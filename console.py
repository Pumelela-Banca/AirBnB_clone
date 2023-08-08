#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '$: '
    
    def do_help(self, line):
        '''Get some help'''
        if line == 'quit':
            print('Quit command to exit the program')
        elif line == 'EOF':
            print('EOF command to exit the program')
        else:
            print('Documented commands (type help <topic>):')
            print('========================================')
            print('EOF  help  quit\n')

    def do_quit(self, line):
        '''exit the program'''
        return True

    def do_EOF(self, line):
        '''exit the program'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
