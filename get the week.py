# print today's date
from datetime import datetime, timedelta
today=datetime.now()
print('Today is:' + str(today))
# print yesterday's date
some_day=timedelta(days=1)
last_day=today-some_day
print('yesterday was:'+ str(last_day))
# ask a user to enter a date
any_date=input("enter a date:(dd/mm/yy)")
any_day_date=datetime.strptime(any_date,'%d/%m/%Y')
# print the date one week from the date entered
some_week=timedelta(weeks=1)
last_week=any_day_date-some_week
print('last week was:'+ str(last_week))