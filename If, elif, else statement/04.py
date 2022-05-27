country = input("What is Your Country? ").strip().lower()
countries = ["egypt", "palestine", "syria", "yemen", "ksa", "usa", "bahrain", "england"]
price = 100
discount = 30

if country in countries:
    print(f"Your Country Eligible For Discount And The Price After Discount Is ${price -discount }")
    
else:
    print(f"Your Country Not Eligible For Discount And The Price Is $ {price}")
