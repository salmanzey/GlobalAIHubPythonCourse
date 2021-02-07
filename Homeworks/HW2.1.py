username = "Yona"
password = "Hak"

username1 =input("Please enter your user name: ")

password1= input("Please enter your password: ")

if (username == username1 and password != password1):
  print("Wrong Password!")
elif (username != username1 and password == password1):
  print("Wrong Username!")
elif (username != username1 and password != password1):
  print("Wrong username and password!")
else:
  print("You are logged in...")    