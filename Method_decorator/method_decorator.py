def method_decorator(decorator, name, *args, **kwargs):
    """
    This decorator is used to wrap the class method in the decorator

    Args:
        :param decorator:  decorator for method
        :param name: name of the class method
        :param args: args for decorator
        :param kwargs: kwargs for decorator

    Returns:
        :return class: returns the same class with the method in the decorator

    """

    def get_class(cls: object):
        bound = cls.__getattribute__(cls, name)
        dec = decorator(bound, *args, **kwargs)
        setattr(cls, name, dec)
        return cls

    return get_class


def magic(func, *dec_args, **dec_kwargs):
    def wrap(self, *args, **kwargs):
        print("start magic")
        func(self, *args, **kwargs)
        print("end magic")

    return wrap


@method_decorator(magic, 'hello', [1, 2, 3, 4], n=4)
class Test(object):
    def __init__(self):
        self.x = 10

    def hello(self):
        print("hello")

    def num(self, x):
        print(x)


t = Test()
t.hello()
t.hello()
t.num(4)
"""
start magic
hello
end magic
start magic
hello
end magic
4
"""
