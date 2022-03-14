try:
  number = int(input('Please, enter a positive number: '))
  sum_num = 0
  for i in str(number):
    sum_num += int(i) ** len(str(number))
    sum_num
  if number == sum_num:
    print("{} is an Armstrong Number".format(number))
  else:
    print("{} is not an Armstrong Number".format(number))
except ValueError:
  print("It is an invalid entry. Don't use non-numeric, float, or negative values!") 
