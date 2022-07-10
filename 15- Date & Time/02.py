# printing the current date and time in different methods

import datetime

# ---------------(DATE)---------------

print(datetime.datetime.now().strftime("%Y-%m-%d"))
# 2022-07-01

print(datetime.datetime.now().strftime("%b %d, %Y"))
# Jul 01, 2022

print(datetime.datetime.now().strftime("%d-%b-%Y"))
# 01-Jul-2022

print(datetime.datetime.now().strftime("%d/%b/%y"))
# 01/Jul/22

print(datetime.datetime.now().strftime("%a, %d %B %Y"))
# Fri, 01 July 2022

print(datetime.datetime.now().strftime("%x"))
# 07/01/22


# ---------------(TIME)---------------

print(datetime.datetime.now().strftime("%-I:%-M:%-S %P"))
# 2:49:59 pm

print(datetime.datetime.now().strftime("%X"))
# 14:49:59


# ---------------(DATE & TIME)---------------

print(datetime.datetime.now().strftime("%c"))
# Fri Jul  1 14:49:59 2022


