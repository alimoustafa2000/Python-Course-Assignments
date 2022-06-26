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


get_people_scores("Ali", Math=90, Science=80, Language=70)

print('=' * 40)

get_people_scores("Ali", Logic=70, Problems=60)

print('=' * 40)

get_people_scores(Logic=70, Problems=60)

print('=' * 40)

get_people_scores("Ali")

