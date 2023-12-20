from decorator import decorator_func

@decorator_func
def say_hello(name):
    print ("Processing function")
    return f'name_: {name}'


print(say_hello("Shikh"))

# print(say_hello.__name__)
# help(say_hello)