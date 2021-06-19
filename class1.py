#comments
# list1= [1,2,'Jyotsana',True]
# print(list1)
# list1.append('Anna')
# print(list1)
# print(list1[-1::-1])
#
#
#
# con_capital= {"Nepal": "Kathmandu"}  # Dictionary
# print(con_capital["Nepal"])
#
# con_capital.update({'Japan':'Tokyo'})
# print(con_capital["Japan"])
# item = con_capital.popitem()
# print(item)
odd_list=[]
even_list=[]
for num in list_nums:
  if num%2==0:
   even_list.append(num)

  else:
    odd_list.append(num)
print(even_list)
print(odd_list)

import random

com_choice = random.randint(1,3)
user_choice = int(input('Enter \n 1 for Rock \n 2 for Paper \n 3 for Scissors '))
choice={1:"Rock",2:"Paper",3:"Scissor"}


for key in choice:
    if com_choice==key:
         if com_choice==1 and user_choice==2 or com_choice==2 and user_choice==3 or com_choice==3 and user_choice==1:
            print("Computer chose " + choice[key])
            print('User won!!')
         elif com_choice==2 and user_choice==1 or com_choice==3 and user_choice==2 or com_choice==1 and user_choice==3:
            print("Computer chose " + choice[key])
            print('Computer Won!! You lost!')
         elif com_choice==user_choice:
            print("Computer chose " + choice[key])
            print('Draw')
         else:
            print('Invalid choice')