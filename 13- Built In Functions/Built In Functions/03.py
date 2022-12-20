# find the value of 'n' that makes the Output 'Good'.

# l = list(range(n))   

# if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):  

#     print("Good")

# -------------------------------------------------------

n = 1

while n < 1000:

    l = list(range(n))

    if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

        print (f"'n' may be => {n}")

    n+=1

#  Output
# 'n' may be => 20
# 'n' may be => 21
# 'n' may be => 22
