def fibonacci(index):
    return index if index <= 1 else fibonacci(index - 1) + fibonacci(index - 2)
