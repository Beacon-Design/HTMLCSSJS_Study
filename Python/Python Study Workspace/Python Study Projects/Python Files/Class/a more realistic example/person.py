

# File person.py (final)
""" 
Record and process information about people. Run this file directly to test its classes. 
"""

from classtools import AttrDisplay                  # Use generic display tool

class Person(AttrDisplay):                          # Mix in a repr at this level
    """ 
    Create and process person records 
    """
    def __init__(self, name, job=None, pay=0):      # Constructor takes three arguments
        self.name = name                            # Fill out fields when created
        self.job = job                              # self is the new instance object
        self.pay = pay

    # Add methods to encapsulate operations for maintainability
    def lastName(self):                             # Behavior methods, Assumes last is last
        return self.name.split()[-1]                # self is implied subject

    def giveRaise(self, percent):                   # Percent must be 0..1
        self.pay = int(self.pay * (1 + percent))    # Must change here only

# Add customization of one behavior in a subclass
class Manager(Person):
    """
    A customized Person with special requirements
    """

    # Add customization of constructor in a subclass
    def __init__(self, name, pay):                   # Redefine constructor
        Person.__init__(self, name, 'mgr', pay)     # Run original with 'mgr'   Job name is implied

    def giveRaise(self, percent, bonus=.10):         # Redefine at this level
        Person.giveRaise(self, percent + bonus)     # Call Person's version


if __name__ == '__main__':                           # When run for testing only
    # self-test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jone', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())         # Extract object's last name
    sue.giveRaise(.10)                    # Give this object a raise
    print(sue)

    tom = Manager('Tom Jones', 5000)         # Job name not needed:
    tom.giveRaise(.10)                       # Implied/set by class
    print(tom.lastName())
    print(tom)