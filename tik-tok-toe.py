import random
print ("tik-tok-toe game")
a11 = ""
a12 = ""
a13 = ""
a21 = ""
a22 = ""
a23 = ""
a31 = ""
a32 = ""
a33 = ""
compuer_choice = ''
user_choice = str(input('enter your choice(x or o):'1))
if user_choice == "x":
     print("your choice is x")
     computer_choice = "o"
elif usre_choice == "o":
     print("your choice is o")
     computer_choice = "x"
else :
     print("error")
     exit()
computerlist =["a11","a12","a13","a21","a22","a23","a31","a32","a33"]
user_input = str(input("enter your choice:"))

a = f'''\n
        {a11}    |   {a12}    |   {a13} \n
      ------------------------\n
        {a21}    |   {a22}    |   {a23} \n
      ------------------------\n
        {a31}    |   {a32}    |   {a33} \n
'''

print (a)
