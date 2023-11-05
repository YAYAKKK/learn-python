## AGE CHEKING AND NEXT BIRTDAY PROGRAM

#FIRST STEP IMPORT LIBRARY DATETIME

import datetime as dt
print ('\nAGE CHEKING AND NEXT BIRTDAY PROGRAM')
print (9*'====')

#INPUT USER DATE BIRTHDAY
print ('\nINPUT YOUR DATE BIRTHDAY: \n')

date = int(input ("DATE \t\t :"))
month = int(input ("MONTH \t\t :"))
year = int(input ("YEAR \t\t :"))
masaDepan =int(input (f"FUTURE \t\t :"))

#TODAY DATE
now = dt.date.today ()   
print(f"TODAY IS : {now}")

#RESULT OF USER BIRTHDAY
dateBirth = dt.date(year, month, date)
print (f"YOUR BIRTH IN  {dateBirth}, IN {dateBirth: %A}")

#AGE IN DAY COUNT
ageday = now - dateBirth         #COUNT OF YEARS NOW AND DATE BIRTH FOR AGE BY DAY
print(f"\nYOUR AGE IN COUNT OF THE DAY : {ageday}")

#AGE IN YEAR COUNT              #COUNT OF AGE BY DAY WITH ALL OF DAY IN ONE YEAR FOR AGE BY YEAR
age = ageday.days // 365
ageMonth = (ageday.days % 365) // 30

print (f"NOW, YOUR AGE {age} YEARS, {ageMonth} MONTHS")

if age >20:
    print("\nYOU'RE ADULT")
elif age <20:
    print("\nYOU'RE A CHILD")
    print("\nGO READ YOUR BOOK")
else:
    print("\nARE YOU BABY")
    print("DONT CRY!!! AND GO TO YOUR MOM")

#NEXT BIRTHDAY IN FUTURE
nextBirthday = dt.date(year + age + masaDepan , month, date)
print (f"""\nIN SCALE TIME OF {masaDepan} YEARS FUTURE YOU WILL BIRTHDAY IN {age + masaDepan} YEARS IN {nextBirthday.strftime('%A')}""")

print("\nTHANKS FOR USING THIS PRROGRAM\n")