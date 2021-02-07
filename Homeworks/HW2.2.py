
my_dictionary = {"Yona":"Hak" }

username1 =input("Please enter your user name: ")

password1= input("Please enter your password: ")

if username1 in my_dictionary.keys():
 if my_dictionary[username1] == password1:
   print("You are logged in...")
 else:
   print("Wrong password!") 
   
elif password1 in my_dictionary.values():
  print("Wrong username!")

else:
  print("Wrong username and password!!!")  
