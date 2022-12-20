# find the value of 'v' that makes the Output '820'.

# my_range = list(range(v))

# print(sum(my_range, v) + pow(v, v, v)) => 820

# --------------------------------------------------

v = 1

while v < 1000:

    my_range = list(range(v))

    if (sum(my_range, v) + pow(v, v, v)) == 820:

        print(f"v = {v}")

        break

    v += 1


#  Output
# v = 40