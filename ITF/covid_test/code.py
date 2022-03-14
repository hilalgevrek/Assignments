age = False  # Are you a cigarette addict older than 75 years old? 
chronic = False # Do you have a severe chronic disease?
immune = True  # Is your immune system too weak? 

boolean_result = (age and chronic) or (chronic and immune) or (age and immune)  # If at least any two are 'True', the result risky. Otherwise there isn't any risk.

if boolean_result == True:
  print('You are in risky group')
else:
  print('You are not in risky group')
