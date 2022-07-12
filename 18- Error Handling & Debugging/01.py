user_NUM = input("Add Your Number => ")


if len(user_NUM) > 1:

    raise IndexError ("Only One Character Allowed")

elif len(user_NUM) == 1 and user_NUM == '0':

    raise ValueError ("Number Must Be Larger Than '0'")

elif ((user_NUM >= 'a' and user_NUM <= 'z') or (user_NUM >= 'A' and user_NUM <= 'Z')):

    raise Exception ("Only Numbers Allowed")

elif len(user_NUM) == 1 and user_NUM != '0' and user_NUM.isdigit():

    print("##################")
    print(f"The Number Is '{user_NUM}'")
    print("##################")
