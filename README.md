# AirBnB Clone
## Description of the Project
This is a succesfully cloning a replica version of the [AirBnB]-(https://www.airbnb.com) using python3. The site handle rentals and reservations. It's entity framework and core classes is made up of Users, Place, State, City, Amenity and Review which inherits from a BaseModel. This was possible possible with the help of python cmd class method. Files were parsed and saved using the json class method, making the code interoperable. 
## Requirements
Allowed editors, vi, vim, emacs
Files are executable
Using pycodostyle (ver 2.8.*)
## Usage
### Interactive mode
To execute the program we run the console:
....$ ./console.py,
prompt appears:
(hbnb)
type command to get desired output. Ex.
(hbnb) help
##
Documented commands (type help <topic>):
=====================================
EOF   all   create   destroy   help   quit   show   update
(hbnb) create BaseModel
4659d995-2824-45cc-8c76-4c7e9e8a865d
EOF   all   create   destroy   help   quit   show   update
(hbnb) destroy 4659d995-2824-45cc-8c76-4c7e9e8a865d
EOF   all   create   destroy   help   quit   show   update
(hbnb) show 4659d995-2824-45cc-8c76-4c7e9e8a865d
** class doesn't exist **
### Unittest
The python unittest framework enables to test fixtures, test cases, test suite and test runner. It enable a testing automation. To create a unittest we need to first create a test modele.
In our current directory, new file test_anytestfile.py, import unittest method also unittest.TestCase class.
To run it
....& python -m unittest test_anytestfile.py
..........
........................................................................................................
          Ran 1 test
          Ok
          '''''''
To run directly from editor add
under if __name__=='__main__':
          unittest.main()
### Storage 
Instances of classes are saved in a json string representation to the __file.json__ file in the root directory. Chances such as addition, deletions, update made to the objects are saved automatically to the file. This serves as a local file database.
### Supported Commands

Name | Description | Use
-------- | ----------- |-------- |
help | This displays help informations as listed commands | help [command]
quit | Exits/quits the console | quit
EOF | Exits the program when files are passed into the program | N/A
create | Creates a new instance identity of the class | create [class_name]
show | Prints the instances | show [class_name] [id]
destroy | Deletes the instance | destroy [class_name] [id]
all | Prints the string representation of all instances of a class| all or all [class_name] [id]
update | Adds or modifies attributes of an instance | update [class_name] [id] [attribute] [value]
