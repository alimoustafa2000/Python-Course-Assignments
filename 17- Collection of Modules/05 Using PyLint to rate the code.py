"""A function that says hello to list members"""

my_friends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_peoples) -> list:

    """
    This is a function that Says Hello to list members
    parameter:
        some_peoples => list
    return:
        Return Hello Message To The Person
    """

    for someone in some_peoples:
        print(f"Hello {someone}")

say_hello(my_friends)
