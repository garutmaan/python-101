import datetime

print("Welcome to PYTHON Class")
today_date = datetime.datetime.now()
# Tuesday, 21st February at 04:59 PM
print(f"Held on:{today_date.strftime('%A, %dth %B at %I:%M %p')}")