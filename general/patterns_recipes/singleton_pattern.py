# Singleton

# class OnlyOne working only on Python 2.7

########################################################
########################################################


class OnlyOne:
    # private
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)

# Testing OnlyOne


x = OnlyOne('sausage')
y = OnlyOne('eggs')
z = OnlyOne('spam')

print(z)
print(x)
print(y)

########################################################
########################################################


class SingletonObj(object):
    def __new__(cls):
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)

        return cls.instance

# Testing Singleton


obj1 = SingletonObj()
obj2 = SingletonObj()

print(type(obj1) == type(obj2))
print(id(obj1) == id(obj2))

########################################################
########################################################


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        # If you want to run __init__ every time the class is called, add
        else:
            cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]


class SingletonMeta(metaclass=Singleton):
    pass

# Testing SingletonMeta


obj1 = SingletonMeta()
obj2 = SingletonMeta()

print(type(obj1) == type(obj2))
print(id(obj1) == id(obj2))
