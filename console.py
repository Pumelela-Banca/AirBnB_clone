#!/usr/bin/python3
from models import base_model
import cmd
import os
import json

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

    def do_create(self, line):
        ''' Creates a new instance of BaseModel '''
        if line == '':
            print('** class name missing **')
        elif line == 'BaseModel':
            model = base_model.BaseModel()
            model.save()
            print(model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        ''' Prints the string representation of
            an instance based on the class name
        '''
        if line == '':
            print('** class name missing **')
            return
        args = line.split()
        if args[0] != 'BaseModel':
            print("** class doesn't exist **")
            return 
        elif len(args) == 1:
            print('** instance id missing **')
            return
        else:
            if os.path.exists('file.json'):
                with open('file.json') as fh:
                    obj = json.load(fh)
                j = 0
                for key in obj.keys():
                    if args[1] in key:
                        print(f"[{args[0]}] ({args[1]}) {obj[key]}")
                        j = 1
                if  j == 0:
                    print('** no instance found **')
            else:
                print('** no instance found **')



if __name__ == '__main__':
    HBNBCommand().cmdloop()
