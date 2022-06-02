students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

my_points = {
    "A": 100,
    "B": 80,
    "C": 40,
    "D" : 20
}

sum1 = 0
sum2 = 0
sum3 = 0

for student in students:
    print("-" * 30)
    print(f"Student Name => {student}")
    print("-" * 30)

    for subjects in students[student]:

        for points in my_points:

            if students[student][subjects] == points and student == "Ahmed":
                sum1 += my_points[points]
                print(f"- {subjects} => {my_points[points]} Points")
                
            elif students[student][subjects] == points and student == "Sayed":
                sum2 += my_points[points]
                print(f"- {subjects} => {my_points[points]} Points")

            elif students[student][subjects] == points and student == "Mahmoud":
                sum3 += my_points[points]

                print(f"- {subjects} => {my_points[points]} Points")

    print(f"= Total Points For {student} Is: {sum1 if student == 'Ahmed' else sum2 if student == 'Sayed' else sum3}")
