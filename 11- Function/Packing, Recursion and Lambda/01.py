def get_score (**subjects):

    for subject in subjects: 

        print(f"- {subject} => {subjects[subject]}")



get_score(Math = 90, Science = 80, Language = 70)

print('=' * 40)

get_score(Logic=70, Problems=60)