student_score = {
    "Math" : "90%",
    "Science" : "80%",
    "Language" : "70%"
}


def get_people_scores (name = "", **subjects):

    if name == "" :
        pass

    elif name != "" and subjects != {}:
        print(f"Hello {name}, This Is Your Score Table:")

    if subjects == {} and name != "":
        print(f"Hello {name} You Have No Scores To Show.")

    else:
        for subject in subjects:
            print(f"- {subject} => {subjects[subject]}")


get_people_scores("Ali", **student_score)

print('=' * 40)

get_people_scores("Ali")

print('=' * 40)

get_people_scores(**student_score)

