##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Acces denied
"""

access = False
count = 0
while access == False:
  count = count + 1
  username = (input("Enter username")).strip()
  password = (input("Enter password")).strip()
  if username == "admin" and password == "12345":
    print("Access granted")
  else:
    print("Access denied")
  if count == 3:
    print("Access denied")
    break
  
