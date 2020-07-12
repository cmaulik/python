#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()
  

  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print(now.strftime("The current Year is %d/%m/%Y"))

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(now.strftime("Local date and time is: %c"))
  print(now.strftime("Local date is: %x"))
  print(now.strftime("Local  time is: %X"))

  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM



if __name__ == "__main__":
  main();
