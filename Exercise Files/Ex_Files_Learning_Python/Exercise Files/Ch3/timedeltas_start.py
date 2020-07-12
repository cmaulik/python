#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print(timedelta(days= 365, hours = 5, minutes= 30))

# print today's date
now = datetime.now()
print("Today's date is:", now)

# print today's date one year from now
print("Date after one year will be:" + str(now + timedelta(days=365,hours=2)))

# create a timedelta that uses more than one argument
print("After 2 days and 3 weeks " + str(now + timedelta(days=2, weeks=3)))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
print(t.strftime("The date and time before one week was %A, %d %B %Y"))


### How many days until April Fools' Day?
today = date.today()
afp = date(today.year,4,1)

if afp < today:
    afp = afp.replace(year=today.year+1)
# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# Now calculate the amount of time until April Fool's Day  
qwe = afp-today
print("It's just",qwe)

