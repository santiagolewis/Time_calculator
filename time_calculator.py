# This function takes two parameters, the first one is a start time in the 12-hour clock format(ending AM or PM), the second is a duration of time. The function adds the duration of time to the start time and returns the new hour. There is a third optional parameter that is a starting day of the week. 
# You can see what this function does in the link below.
# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator
def add_time(start, duration, day = False):
  # First we define the starting hour, minute and if it is AM or PM splitting the start parameter.
  start = start.split()
  AMPM = start[1]
  start = start[0].split(":")
  hour1 = start[0]
  min1 = start[1]
  # I used a dictionary to be able to link every day of the week with a number and a "daylis" list with every day on the week. Notice that the number of every day un the dictionary corresponds to the index of that day in "dayslis"
  daysDict = {"Monday" : 0, "Tuesday" : 1, "Wednesday" : 2, "Thursday" : 3, "Friday" : 4, "Saturday" : 5 ,"Sunday" : 6}
  dayslis = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  # Define a days_later variable.
  days_later = 0
  # Now we split the duration parameter in hours and minutes
  duration = duration.split()
  duration = duration[0].split(":")
  hour2 = duration[0]
  min2 = duration[1]
  # Next we define the new hour and new minutes by summing the starting to the duration hours and minutes.
  new_hour = int(hour1) + int(hour2)
  new_min = int(min1) + int(min2)
  #If the new minutes is greater than 59 then we sum one to new_hour and substract 60 to new_min
  if new_min > 59:
    new_min -= 60
    new_hour += 1
  #If new_min is only one digit long we must add a "0" on the left side so the new time is not 12:2 for example(in this case the new time would be 12:02)  
  if len(str(new_min)) == 1:
    new_min = "0" + str(new_min)
  Ahour = new_hour
  if AMPM == "PM":
    Ahour += 12
  # In this part we make sure that the day parameter is in lowercase and capitalized.
  if day:
    day = day.lower()
    day = day.capitalize()
  # Here we loop until Ahour is smaller or equal than 23, adding 1 to the days_later variable. 
  while Ahour > 23:
    Ahour -= 24
    # Now we define a dayINd variable that saves the index(of "dayslis") of the day that we currently are using the "daysDict" respective value and for every time the code runs this loop(which means a day have passed), we add one to that index and set the "day" variable to the day that has that index in the dayslis, unless the "dayINd" variable is 6, in which case we set the day varible to monday again(which is dayslis[0]).
    if day:
      dayINd = daysDict[day]
      if dayINd == 6:
        day = dayslis[0]
      else:
        day = dayslis[dayINd+1]
    days_later += 1
  # Now we change the "AMPM" variable to "AM" if it was set to "PM" and vice versa for every time the new_hour variable is greater or equal to 12 (substracting 12 every time the code runs this loop).
  while new_hour >= 12:
    if AMPM == "AM":
      AMPM = "PM"
    else:
      AMPM = "AM"
    # If "new_hour" variable is equal to 12 we break the loop otherwise this variable could be 00, and that is not 12-hour clock format.
    if new_hour == 12:
      break
    new_hour -= 12
  # Here we define the new_time variable that is the new_hour, new_min and AMPM variables in the format that the instructions indicate.
  new_time = str(new_hour) + ":" + str(new_min) + " " + AMPM
  # As required we add the day to the variable if the third parameter is given.
  if day:
    new_time += ", " + day
  # And finally we add "next day" or n° "days later" if "days_later" variable is equal to 1 or +1 respectively.
  if days_later == 1:
    new_time += " (next day)"
  elif days_later > 1:
    new_time += f" ({days_later} days later)"
  return new_time