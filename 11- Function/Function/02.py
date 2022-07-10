
def addition (*numbers):

    sum = 0

    for number in numbers:
        if number == 10:
            continue

        elif number == 5:
            sum-=5

        else:
            sum+=number


    print(sum)

addition(10, 20, 30, 10, 15)
# 65

addition(10, 20, 30, 10, 15, 5, 100)
# 160