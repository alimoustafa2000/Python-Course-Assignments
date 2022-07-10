# ----------------------
# in my_mod.py file:
# ----------------------

# say_welcome function

def say_welcome (name):

    print(f"Welcome {name}") 


# say_hello function

def say_hello (name):

    print(f"Hello {name}") 


# ==================================================

# ----------------------
# in  main.py file:
# ----------------------

import sys

sys.path.append(r"C:\Users\A L I\Desktop\Python")

# Calling the Whole module
import my_mod
my_mod.say_welcome("Ali")

my_mod.say_hello("Ola")

# Calling Function only
from my_mod import say_welcome
say_welcome("Ali")   

from my_mod import say_hello
say_hello("Ola")

# Using Alias
from my_mod import say_welcome as welcome
welcome("Ali")   

from my_mod import say_hello as hello
hello("Ola")