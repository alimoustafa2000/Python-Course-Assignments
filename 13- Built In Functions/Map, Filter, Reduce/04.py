skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

reversed_skills = reversed(skills)

enumerated_skills = enumerate(reversed_skills, 50)

for counter, skill in enumerated_skills:

    if type(skill) == int :

        continue

    else:

        print(f"{counter} - {skill}")