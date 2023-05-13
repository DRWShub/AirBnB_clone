#!/usr/bin/python3
import cmd
import re
import models
import subprocess
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class_list = ['BaseModel', 'User', 'Place', 'State', 'City',
              'Amenity', 'Review']


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    last_output = ''

    class_list = ['BaseModel', 'User', 'Place', 'State', 'City',
                  'Amenity', 'Review']

    classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
               "Place": Place, "Review": Review, "State": State, "User": User}

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        print('\n'.join([
              'Quit command to exit the program\n',
              ]))

    def emptyline(self):
        """Doesn't execute anything"""
        pass

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def A_shell(self, line):
        """Run shell command"""
        sub_cmd = subprocess.Popen(line,
                                   shell=True,
                                   stdout=subprocess.PIPE)
        ouput = sub_cmd.communicate()[0].decode('utf-8')
        print(output)
        self.last_output = output

    def an_echo(self, line):
        """implements echo in non interactive mode"""
        print(line.replace('$out', self.last_output))

    def do_create(self, line):
        """creates a new instance of BaseModel, saves it

        to JSON file, and prints the id.
        """
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.class_list:
            print("** class does exist **")
        else:
            case = eval(line)()
            case.save()
            print(case.id)

    def do_show(self, arg):
        """Prints the string representation of all instance

        based or not on the class name and id.
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.

        Saves the changes to JSON file.
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")

        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """Prints the string representation of all instances based or

        not on the class name.Printed result is a list of strings.
        """

        instances = []
        if not line:
            for key, value in storage.all().items():
                cls_name = key.split('.')[0]
                instance = eval(cls_name)(**value.to_dict())
                instances.append(str(instance))
                print(instances)

        elif line in HBNBCommand.class_list:
            for key, value in storage.all().items():
                if line == key.split('.')[0]:
                    instance = eval(line)(**value.to_dict())
                    instances.append(str(instance))
            print(instances)

        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name by adding

        or updating attribute, and saves changes to JSON file
        """
        if not line:
            print("** class name missing **")
        else:
            same_line = line
            try:
                args = line.split(' ')
            except ValueError:
                print("** instance id missing **")
            try:
                if args[1]:
                    pass
            except IndexError:
                print("** instance id missing **")
                return
            try:
                if args[2]:
                    pass
            except IndexError:
                print("** attribute name missing **")
                return
            try:
                if args[3]:
                    attr_val = same_line.split('"')[1]
            except IndexError:
                print("** value is missing **")
                return

            key = "{}.{}".format(args[0], args[1])
            if args[0] not in HBNBCommand.class_list:
                print("** class doesn't exist **")

            elif key not in storage.all().keys():
                print("** no instance found **")

            else:
                setattr(storage.all()[key], args[2], attr_val)
                storage.all()[key].save()

    def precmd(self, args):
        """implements string format for some commands"""
        if len(args) >= 2:
            for arg in args:
                if "." in args:
                    args = args.replace(".", " ").replace("(",
                                                          "").replace(")", "")
                    args = args.split(" ")
                    args = f"{args[1]} {args[0]}"
                return cmd.Cmd.precmd(self, args)

        elif len(args) > 2:
            args = shlex.split(arg)
            for arg in args:
                if args:
                    args = re.match(r'^(\w+)\.(\w+)\(:?.*\)$', args)
                    args = f"{command} {class_list}"
        return (args)
        return cmd.Cmd.precmd(self, args)

    def get(self, cls, id):
        """gets the class list value"""
        if cls not in class_list.values():
            return None

        al_cls = models.storage.all(cls)
        for value in al_cls.values():
            if(value.id == id):
                return value
        return None

    def count(self, cls=None):
        """counts the number of instances for classes"""
        all_class = class_list.values()
        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())
        return count


if __name__ == '__main__':
    HBNBCommand().cmdloop()
