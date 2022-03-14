user_name='Joseph'

from_user = input('Please, enter your first name: ')

if  from_user.title() == user_name:
  print('Hello, ' + user_name + '! The password is: W@12')
else:
  print('Hello, ' + from_user.title() + '! See you later.')
