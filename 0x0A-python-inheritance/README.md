# :colombia: Python - Inheritance                                               
- What is a superclass, baseclass or parentclass                                
- What is a subclass                                                            
- How to list all attributes and methods of a class or instance                 
- When can an instance have new attributes                                      
- How to inherit class from another                                             
- How to define a class with multiple base classes                              
- What is the default class every class inherit from                            
- How to override a method or attribute inherited from the base class           
- Which attributes or methods are available by heritage to subclasses           
- What is the purpose of inheritance                                            
- What are, when and how to use isinstance, issubclass, type and super built-in functions
## Examples                                                                     
Create a class method for validate an integer into the class BaseGeometry        
```
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```
The output                                                                      
```
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
```
check the code in the file 7-base_geometry.py
## Prerequisites
8 lecture hours about  Inheritance                                              
## Installing

for have the code in your local machine you only need download the code files and put it into a directory                                                           

## Authors

---Olusegun Emmanuel
