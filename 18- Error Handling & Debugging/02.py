try:

    user_LETTER = input("Add Letter From A to Z => ")

    if len(user_LETTER) > 1:

        raise IndexError

    elif user_LETTER >= 'A' and user_LETTER <= 'Z' and len(user_LETTER) == 1:

        print(f"You Typed '{user_LETTER}'")

    else:

        raise ValueError

except IndexError:

    print("You Must Write One Character Only")

except ValueError:

    print("The Letter Not In A - Z")
