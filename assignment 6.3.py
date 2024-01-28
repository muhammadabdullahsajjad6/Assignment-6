#Q4: Metaclass Mechanics in Python
class Meta(type):
    def __new__(cls, name, bases, dct):
        # Modify the class creation process
        dct['custom_attribute'] = 42
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

# Example usage:
obj = MyClass()
print(obj.custom_attribute)  # Output: 42
