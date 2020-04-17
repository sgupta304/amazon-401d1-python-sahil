# a .py file is a 'module'
# when a python file is executed directly then it is often called a 'script'
corona_status = "cured"


# print(corona_status)
# print(f"The Corona status is : {corona_status}!")
# print(f"""
# The
# Corona
# Status
# is
# {corona_status}
# """)
# value = input("How are you")
# print(value)


def say_hello():
    print("hi")
    print("Hello")


say_hello()

print(type(None))

condition = None
# Falsy: False, 0, '', None, []

if condition:
    print("Met")
else:
    print("Not Met")

print(f"Not Met {condition}")
print("Not Met {}".format(condition))
