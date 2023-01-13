number = input('hours: ')
pay = input('rate: ')

if number and pay:
    number = int(number)
    pay = int(pay)
    cal = number * pay
    print(cal)