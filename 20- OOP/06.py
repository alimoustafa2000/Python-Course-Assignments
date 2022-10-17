class A:

    def __init__(self, one):

        self.one = one

class B (A):

    def __init__(self, one, two):

        super().__init__ (one)

        self.two = two

class C (B):

    def __init__(self, one, two, three):

        super().__init__ (one, two)

        self.three = three

class Text (C):

        def __init__(self, one, two, three):

            super().__init__ (one, two, three)

        def show_name (self):

            return f"The Name Is {self.one}{self.two}{self.three}"


the_name = Text("El", "ze", "ro")

print(the_name.show_name())
# The Name Is Elzero
