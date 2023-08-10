#!/usr/bin/python3
'''console Program that contains the entry
   point of the command interpreter
'''
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
import cmd
import os
import json


class HBNBCommand(cmd.Cmd):
    ''' defines each command'''
    prompt = '(hbnb) '

    dict_cls = {
            'BaseModel': BaseModel,
            'User': User, 'Place': Place,
            'State': State, 'City': City,
            'Amenity': Amenity, 'Review': Review
    }

    def default(self, line):
        cmnd_dict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
        }
        args = line.split('.')
        try:
            if len(args) != 2:
                print(f"*** Unknown syntax: {line}")
                return False
            if HBNBCommand.dict_cls.get(args[0]) is None:
                print(f"** class doesn't exist **")
                return False
            cmds = args[1].split('(')
            if len(cmds) != 2:
                print(f"*** Unknown syntax: {line}")
                return False
            arg_line = args[0]
            if len(cmds[1]) > 1:
                cmds[1] = '(' + cmds[1]
                cmds[1] = cmds[1][:-1]
                cmds[1] = cmds[1] + ',)'
                cmds_tuple = eval(cmds[1])
                if len(cmds_tuple) > 1 and type(cmds_tuple[1]) is dict:
                    arg_line += ' ' + cmds_tuple[0]
                    for ky, vl in cmds_tuple[1].items():
                        update_str = arg_line
                        update_str += ' ' + str(ky) + ' ' + str(vl)
                        for k, v in cmnd_dict.items():
                            if k == cmds[0]:
                                v(update_str)
                                break
                    return
                for i in cmds_tuple:
                    arg_line += ' ' + i
            flag = 0
            for k, v in cmnd_dict.items():
                if k == cmds[0]:
                    v(arg_line)
                    flag = 1
                    break
            if flag == 0:
                print(f"*** Unknown syntax: {line}")
                return False
        except Exception:
            print(f"*** Unknown syntax: {line}")
            return False

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
        elif line == 'count':
            print("count number of instance of specific class")
        else:
            print('\nDocumented commands (type help <topic>):')
            print('========================================')
            print('EOF  help  quit create show update count all\n')

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
            return

        else:
            for cl, val in HBNBCommand.dict_cls.items():
                if cl == line:
                    obj = val()
                    obj.save()
                    print(obj.id)
                    return
            print("** class doesn't exist **")

    def do_show(self, line):
        ''' Prints the string representation of
            an instance based on the class name
        '''
        if line == '':
            print('** class name missing **')
            return
        args = line.split()

        if HBNBCommand.dict_cls.get(args[0]) is None:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        else:
            '''storage.reload()'''
            obj = storage.all()
            j = 0
            ky = args[0] + '.' + args[1]
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
        if HBNBCommand.dict_cls.get(args[0]) is None:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        else:
            storage.reload()
            obj = storage.all()
            j = 0
            ky = args[0] + '.' + args[1]

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
        if line == '':
            storage.reload()
            obj = storage.all()
            lst = []
            for key in obj.keys():
                args = key.split('.')
                lst.append(f"[{args[0]}] ({args[1]}) {obj[key]}")
            print(lst)

        else:
            if HBNBCommand.dict_cls.get(line) is None:
                print("** class doesn't exist **")
                return
            storage.reload()
            obj = storage.all()
            lst = []
            for key in obj.keys():
                if line in key:
                    args = key.split('.')
                    lst.append(f"[{args[0]}] ({args[1]}) {obj[key]}")
            print(lst)

    def do_update(self, line):
        '''  Updates an instance based on the class name
             and id by adding or updating attribute
             (save the change into the JSON file).
        '''
        if line == '':
            print('** class name missing **')
            return
        args = line.split()
        if HBNBCommand.dict_cls.get(args[0]) is None:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        else:
            storage.reload()
            obj = storage.all()
            j = 0
            ky = args[0] + '.' + args[1]
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
            obj = HBNBCommand.dict_cls.get(args[0])(**var)
            '''set attribute'''
            attr = args[2]
            try:
                att_value = eval(args[3])
            except Exception:
                att_value = args[3]
            setattr(obj, attr, att_value)
            obj.save()

    def do_count(self, line):
        storage.reload()
        obj = storage.all()
        count = 0
        for key in obj.keys():
            if line in key:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
