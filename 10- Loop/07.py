my_ranks = {
    'Math': 'A',
    'Science': 'B',
    'Drawing': 'A',
    'Sports': 'C'
}

my_points = {
    "A": 100,
    "B": 80,
    "C": 40
}


sum = 0

for subject in my_ranks:

    for points in my_points:

        if my_ranks[subject] == points:

            sum += my_points[points]

            print(f"My Rank in {subject} Is '{my_ranks[subject]}' And This Equal {my_points[points]} Points.")

print(f"Total Points Is: {sum}")
