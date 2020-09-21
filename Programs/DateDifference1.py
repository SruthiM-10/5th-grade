from datetime import date
Month=int(input("Enter a month"))
Day=int(input("Enter a day"))
Year=int(input("Enter a year"))
month=int(input("Enter a month"))
day=int(input("Enter a day"))
year=int(input("Enter a year"))


f_date = date(Year,Month,Day)
l_date = date(year,month,day)
delta = f_date - l_date
print(delta.microseconds,"days")