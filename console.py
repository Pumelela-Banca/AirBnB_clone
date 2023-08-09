#!/usr/bin/python3
'''console Program that contains the entry
   point of the command interpreter
'''
from models import base_model
from models import storage
import cmd
import os
import json


class HBNBCommand(cmd.Cmd):
    ''' defines each command'''
    prompt = '$: '

    def do_help(self, line):
        '''Get some help'''
        if line == 'quit':
            print('Quit command to exit the program')
        elif line == 'EOF':
            print('EOF command to exit the program')
        elif line == 'create':
            print("Creates a new instance of BaseModel")
        elif line == 'show':
            print("Prints the string representation "
                  "of an instance based on the class name")

        elif line == 'all':
            print("Prints all string representation of "
                  "all instances based or not on the class name")
        elif line == 'update':
            print("Updates an instance based on the class name "
                  "and id by adding or updating attribute "
                  "(save the change into the JSON file).")

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
            '''storage.reload()'''
            obj = storage.all()
            j = 0
            ky = 'BaseModel' + '.' + args[1]
            if obj.get(ky) is None:
                print('** no instance found **')
            else:
                print(f"[{args[0]}] ({args[1]}) {obj[ky]}")

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
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
            storage.reload()
            obj = storage.all()
            j = 0
            ky = 'BaseModel' + '.' + args[1]

            if obj.get(ky) is None:
                print('** no instance found **')
            else:
                del obj[ky]
                with open('file.json', 'w') as fh:
                    json.dump(obj, fh)

    def do_all(self, line):
        ''' Prints all string representation of all
            instances based or not on the class name
        '''
        if line == '' or line == 'BaseModel':
            storage.reload()
            obj = storage.all()
            lst = []
            for key in obj.keys():
                args = key.split('.')
                lst.append(f"[{args[0]}] ({args[1]}) {obj[key]}")
            print(lst)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        '''  Updates an instance based on the class name
             and id by adding or updating attribute
             (save the change into the JSON file).
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
            storage.reload()
            obj = storage.all()
            j = 0
            ky = 'BaseModel' + '.' + args[1]
            if obj.get(ky) is None:
                print('** no instance found **')
                return
            if len(args) == 2:
                print("** attribute name missing **")
                return
            if len(args) == 3:
                print("** value missing **")
                return
            if args[2] == "id" or args[2] == "created_at"\
                    or args[2] == "updated_at":
                return
            var = obj[ky]
            '''convert string value to dict to be able to use it as **kwargs'''
            var = eval(var)
            model1 = base_model.BaseModel(**var)
            '''set attribute'''
            attr = args[2]
            att_value = args[3][1:-1]
            setattr(model1, attr, att_value)
            model1.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
