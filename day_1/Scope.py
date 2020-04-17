# What is the scope here?

spam = 'some word'

print(f"outside some_func {spam}")


def some_func():
    global spam  # In order to change the value of the global value
    print(f"inside some_func spam {spam}")
    eggs = "eggs string"
    spam = "new spam value"
    print(f"inside some_func eggs {eggs}")
    return eggs


egg_val = some_func()

print(egg_val)
