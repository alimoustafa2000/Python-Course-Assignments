# ---------------(Task 1)---------------

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0])             # 1st method
print(friends.pop(0))        # 2nd method
print(friends[-1])          # 1st method
print(friends.pop(-1))     # 2nd method

print("="*40)

# ---------------(Task 2)---------------

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[ : :2])
print(friends[1: :2])

print("="*40)

# ---------------(Task 3)---------------

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[1:4])
print(friends[-2: ])

print("="*40)

# ---------------(Task 4)---------------

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

friends[3] = 'Elzero'
friends[4] = 'Elzero'

print(friends)

print("="*40)

# ---------------(Task 5)---------------

friends = ["Osama", "Ahmed", "Sayed"]

friends.insert(0, "Ali")

print(friends)

friends.append("Gamal")

print(friends)

print("="*40)

# ---------------(Task 6)---------------

friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends.remove("Nasser")
friends.remove("Osama")
print(friends)

friends.remove("Salem")
print(friends)

print("="*40)

# ---------------(Task 7)---------------

friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)

print(friends)

print("="*40)

# ---------------(Task 8)---------------

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends.sort()
print(friends)

friends.sort(reverse=True)
print(friends)

print("="*40)

# ---------------(Task 9)---------------

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

print(len(friends))

print("="*40)

# ---------------(Task 10)---------------

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0])
print(technologies[-1][-1])