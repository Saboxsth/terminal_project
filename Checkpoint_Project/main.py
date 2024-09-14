import datetime, bday_message 

today= datetime.date.today()
next_birthday= datetime.date(2025,8,29)
days_away= next_birthday- today


if next_birthday== today:
  print(bday_message.random_message)

else:
  print(f'My next birthday is {days_away.days} days away!')

