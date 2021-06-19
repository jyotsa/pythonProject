user_choice=int(input('Enter a number'))
not_prime_flag=False
for num in range(2,user_choice):
  if user_choice%num==0:
     not_prime_flag=True
     print('not prime')
     break

  num+=1
else:
    print('number is prime')








