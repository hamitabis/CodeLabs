def is_leap(year):
  if (not (year % 400)): 
    return True
  elif (year % 100) and (not (year % 4)): 
    return True
  return False
