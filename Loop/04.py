my_friends = []
number = 4

name = input("What's your friend name? ").strip()


while name != name.upper():
    number -= 1
    
    if name == name.capitalize():
        my_friends.append(name)
        print(f"Your friend: {name} Added")
        
    else:
        my_friends.append(name.capitalize())
        print(f"Your friend: {name.capitalize()} Added => 1st Letter Become Capital")
        
    print(f"Names Left in List Is {number}")
    print(my_friends)

    if number == 0:
        break
    else:
        name = input("What's your friend name? ").strip()
        

else: 
    print('Invalid name')
