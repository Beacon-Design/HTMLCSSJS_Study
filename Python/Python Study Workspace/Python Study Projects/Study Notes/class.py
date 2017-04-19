print('''
------ self ----------------------------------------------
Class methods have only one specific difference from 
ordinary functions - they must have an extra first name 
that has to be added to the beginning of the parameter 
list, but you do not give a value for this parameter when 
you call the method, Python will provide it. This 
particular variable refers to the object itself, and by 
convention, it is given the name self


------ __init__ ------------------------------------------
The __init__ method is run as soon as an object of a class 
is instantiated.The method is useful to do any initialization 
you want to do with your object

we do not explicitly call the __init__ method but pass the 
arguments in the parentheses following the class name when 
creating a new instance of the class. This is the special 
significance of this method


*** Python does not automatically call the constructor of the 
base class, you have to explicitly call it yourself ***

\n''')
class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("Hi!",self.name)
p = Person("A")
p.say_hi()
Person("B").say_hi()



print('''
------The Class Namespace------------------------------------------------------
In the preceding code, a variable is defined in the class scope, which can be accessed by all
the members (instances), in this case to count the number of class members. Note the use of
init to initialize all the instances:



''')
class MemberCounter:
    members = 0
    def int(self):
        MemberCounter.members += 1
m1 = MemberCounter()
m1.int()
print(MemberCounter.members)
m2 = MemberCounter()
m2.int()
print(MemberCounter.members)
# This class scope variable is accessible from every instance as well, just as methods are:
print(m1.members)
print(m2.members)
# What happens when you rebind the members attribute in an instance?
m1.members = "TWO"
print(m1.members)
print(m2.members)
# The new members value has been written into an attribute in m1, 
# shadowing the class-wide variable.                










print('''
------ class variables -------------------------------------
Class variables are shared - they can be accessed by all instances 
of that class. There is only one copy of the class variable and 
when any one object makes a change to a class variable, that change 
will be seen by all the other instances.

------ object variables ------------------------------------
Object variables are owned by each individual object/instance of the 
class. In this case, each object has its own copy of the field i.e. 
they are not shared and are not related in any way to the field by 
the same name in a different instance.

note that an object variable with the same name as a class variable 
will hide the class variable

\n''')
class Robot:
    """population belongs to the *Robot class* is a **class variable**
       we refer to the population as Robot.population"""
    population = 0
    """The name variable belongs to the object (it is assigned using self) 
       and hence is an **object variable**
       refer to the object variable name using (self.name) notation in the 
       methods of that object"""
    
    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print ("(Initializing {})".format(self.name))
        """Robot.poopulation / self.__class__.population"""
        """every object refers to it's class via the self.__class__ attribute"""
        Robot.population += 1
    
    def die(self):
        print ("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print ("{} was the last one.".format(self.name))
        else:
            print ("There are {:d} robots ".format(Robot.population))
    
    def say_hi(self):
        print ("call me {}.".format(self.name))
    
    @classmethod
    def how_many(cls):
        """The how_many is actually a method that belongs to the class and 
           not to the object.so applying the @classmethod decorator is same
           as calling: how_many = classmethod(how_many)"""
        print ("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()
print(Robot.population)
print()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()
print()

droid1.die()
droid2.die()

Robot.how_many()
print()
print(Robot.__doc__,"\n\n")


print('''------Privacy Revisited------------------------------------------------
All class members are public. One exception: If you use data members with 
names using the double underscore prefix such as __privatevar, Python uses 
name-mangling to effectively make it a private variable

To make a method or attribute private (inaccessible from the outside), 
simply start its name with two underscores:

''')

class Secretive:
    def __inaccessible(self):
        print("---BET YOU CAN NOT SEE ME---")
    def accessible(self): 
        print("---THE SECRET MESSAGE IS :---")
        self.__inaccessible()
# Now __inaccessible is inaccessible to the outside world, while it can still 
# be used inside the class (for example, from accessible):
s = Secretive()
s.accessible()        
# s.__inaccessible()    ---AttributeError---

print('''
Inside a class definition, all names beginning with a double underscore are 
"translated" by adding a single underscore and the class name to the beginning:
>>> Secretive._Secretive__inaccessible
<unbound method Secretive.__inaccessible>

If you don't want the name-mangling effect, but you still want to send a signal for other
objects to stay away, you can use a single initial underscore. This is mostly just a convention,
but has some practical effects. For example, names with an initial underscore aren't imported
with starred imports (from module import *)

''')
s._Secretive__inaccessible()







print('''\n\n
------inheritance------------------------------------------------------
Inheritance can be best imagined as implementing a type and subtype 
relationship between classes


''')

class SchoolMember:
    """The SchoolMember class in this situation is known as the base class 
       or the superclass. The Teacher and Student classes are called the 
       derived classes or subclasses."""
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("initialized {}".format(self.name))
    def tell(self):
        print("{} is {}".format(self.name,self.age))
class Teacher(SchoolMember):
    def __init__(self,name,age,slary):
        SchoolMember.__init__(self,name,age)
        self.slary = slary
        print("initialized teacher {}".format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print("slary is {}".format(self.slary))
class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print("initialized student {} ".format(self.name))
    def tell(self):
        SchoolMember.tell(self) 
        print("marks is {}".format(self.marks))
    

t = Teacher("Tom",25,3000)
s = Student("A",12,5)

members = [t,s]
for member in members:
    member.tell()
print(SchoolMember.__doc__)

print('''
------Investigating Inheritance---------------------------------------
------issubclass /__bases__ /isinstance ---------------------------------------
''')      
print(issubclass(Student, SchoolMember))
print(issubclass(SchoolMember,Student))

print(Student.__bases__)    
print(SchoolMember.__bases__)

print(isinstance(s, Student))
print(isinstance(s, SchoolMember))

print(s.__class__)
print(type(s))


print('''------Multiple Superclasses-----------------------------------------------------------------
if a method is implemented differently by two or more of the superclasses (that 
is, you have two different methods with the same name), you must be careful 
about the order of these superclasses (in the class statement). The methods in 
the earlier classes override the methods in the later ones. So if the Calculator
class in the preceding example had a method called talk, it would override (and 
make inaccessible) the talk method of the Talker. Reversing their order,
like this:


class TalkingCalculator(Talker, Calculator): pass


would make the talk method of the Talker accessible. If the superclasses share 
a common superclass, the order in which the superclasses are visited while 
looking for a given attribute or method is called the method resolution order (MRO), 
and follows a rather complicated algorithm.


''')

class Calculator:
    def calculator(self, expression):
        self.value = eval(expression)
class Talker:
    def talk(self):
        print("VALUE IS:",self.value)
class TalkingCalculator(Calculator, Talker):
    pass
# The subclass (TalkingCalculator) does nothing by itself; it inherits all its behavior from its
# superclasses. The point is that it inherits both calculate from Calculator and talk from Talker,
# making it a talking calculator:
tc = TalkingCalculator()
tc.calculator("1+1+1")
tc.talk()


print('''------Interfaces and Introspection-------------------------------------
The "interface" concept is related to polymorphism. When you handle a polymorphic object, you
only care about its interface (or "protocol")the methods and attributes known to the world.

------hasattr(x, "__call__")----------------------------------------------------
------getattr(x, "__call__", value)---------------------------------------------
------setattr(x, "__call__", value)---------------------------------------------
The inverse of getattr is setattr, which can be used to set the attributes of an object.

------ __dict__ ----------------------------------------------------------------
see all the values stored in an objec,examine the __dict__ attribute.

''')
print(hasattr(tc, "talk"))
print(getattr(tc, "talk", None))
setattr(tc, "name", "MR.B")
print(tc.name)
print(tc.__dict__)




































