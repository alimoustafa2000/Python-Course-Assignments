# import modules
import string
import random

# store characters in lists 
s1 = list(string.ascii_lowercase)
s2 = list(string.digits)

# shuffle lists
random.shuffle(s1)
random.shuffle(s2)


result = []

for x in range(7):

    result.append(s1[x])
    result.append(s2[x])

random.shuffle(result)

result.insert(4, "-")
result.insert(9, "-")

output = "".join(result)

print(output)
# p04d-8fj6-71yr3e
# 5qo6-r4s8-1xpc30