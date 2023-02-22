# This program will prompt the employee to enter their salary
# And the number of years they have been working for the company
# If they have been working for the company for more than 5 years, they will receive a bonus
# If they have been working for the company for less than 5 years
# a message will be printed on the screen notifying them that they do not qualify for a bonus

salary = int(input("Enter your salary: "))
year_of_service = int(input("Enter year of serivice: "))
bonus = 0.05
new_salary = salary * bonus

if (year_of_service > 5): 
    print("You qualify for a salary bonus of: " + str(new_salary))
else: 
    print("Sorry! You do not qualify for a bonus")