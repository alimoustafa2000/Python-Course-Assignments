def Decorator(my_function):

    def Decorator_mess():

        print("Sugar Added From Decorators")

        my_function()

        print("#" * 50)

    return Decorator_mess

@Decorator

def make_tea():

    print("Tea Created")


@Decorator

def make_coffe():

    print("Coffe Created")


make_tea()
make_coffe()