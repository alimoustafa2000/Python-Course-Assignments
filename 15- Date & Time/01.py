# print number of days from a specific date to the current date.

import datetime

current_date = datetime.datetime.now()

specific_date = datetime.datetime(2021, 6, 25)

print(f"Number Of Days From '2021-06-25' To The Current date Is => {(current_date - specific_date).days} days")