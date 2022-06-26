def member_skills (name = "",*skills):

    if name == "":
        name = "Unknown"
        
    if skills == ():
        print(f'Hello {name} You Have No Skills To Show')

    else:
        print(f"Hello {name} Your skills are: ")

        for skill in skills: 

            print(f"- {skill}")

member_skills (input("What's Your Name? ").strip().capitalize(), *input("Enter Your skills? ").split())

member_skills ()