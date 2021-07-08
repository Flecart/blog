def do_twice(*args, **kwargs):
    def wrapper_do_twice(func):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice("name")
def greet(name):
    print(f"Hello")

greet("d")