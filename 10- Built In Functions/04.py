# -------------------------
# ----------(all)----------
# -------------------------

def my_all (items):

    for item in items:

        if bool(item) == False:

            return False

    else:

        return True


print(my_all([1, 2, 3]))
# True
print(my_all([1, 2, 3, []]))
# False


# -------------------------
# ----------(any)----------
# -------------------------

def my_any (items):

    for item in items:

        if bool(item) == True:

            return True

    else:

        return False


print(my_any([0, 1, [], False])) 
# True
print(my_any([(), 0, False])) 
# False


# -------------------------
# ----------(min)----------
# -------------------------

def my_min (items):
    
    a = list(items)

    a.sort()

    return a [0]


print(my_min([10, 100, -20, -100, 50])) 
# -100
print(my_min((10, 100, -20, -100, 50))) 
# -100


# -------------------------
# ----------(max)----------
# -------------------------

def my_max (items):

    a = list(items)

    a.sort()

    return a [-1]


print(my_max([10, 100, -20, -100, 50, 700])) 
# 700
print(my_max((10, 100, -20, -100, 50, 700))) 
# 700
