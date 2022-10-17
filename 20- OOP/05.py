# Main Class

class Members:

    def __init__(self, n, p):

        self.name = n

        self.permission = p

    def show_info(self):

        return f"Your Name Is {self.name} And You Are {self.permission}"

# Admin Class

class Admins (Members):

    def __init__(self, n, p):

        Members.__init__ (self, n, p)


# Moderators Class

class Moderators (Members):

    def __init__(self, n, p):

        super().__init__ (n, p)


member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")


print(member_one.show_info())
# Your Name Is Osama And You Are Admin

print(member_two.show_info())
# Your Name Is Ahmed And You Are Moderator
