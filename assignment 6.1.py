#Q2: Addressing Potential Pitfalls of Multiple Inheritance
# Pitfall: Ambiguous Method Resolution
class Base1:
    def method(self):
        print("Base1 method")

class Base2:
    def method(self):
        print("Base2 method")

class Derived(Base1, Base2):
    pass

# Example usage:
obj = Derived()
obj.method()  # Output: Base1 method (due to MRO)

# Pitfall: Inconsistent Attribute Names
class Parent1:
    common_attribute = "Parent1 attribute"

class Parent2:
    common_attribute = "Parent2 attribute"

class Child(Parent1, Parent2):
    pass

# Example usage:
obj = Child()
print(obj.common_attribute)  # Output: Parent1 attribute

# Pitfall: Increased Complexity
# Multiple inheritance can lead to complex code.
# It is crucial to document the class hierarchy and use it judiciously.
