#Receiving value from user
money_hour = float(input("How much money do you receive for hour of work? \n"))
work_hours = int(input("How many hours do you work in a month? \n"))

#Calculating salary
salary = money_hour * work_hours
salary = float(salary)

#Printing result
print(f"Your total salary in a month is {salary}!")
