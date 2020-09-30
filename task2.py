#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""
denied = True

while denied:
  name = (input("Enter name")).strip()
  password = (input("Enter PW")).strip()
  if name == "admin" and password =="12345":
    print("Access granted")
    denied = False
  else:
    print("Access denied")
