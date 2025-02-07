import re

def display_result(u,l,s,n):
    if(u>0 and l > 0 and s > 0 and n > 0):
        print("Your password is strong and you can use it for anything")

# defining variables
u = 0
l = 0
s = 0
n = 0 

# Taking password input 
password = str(input("Enter your password: "))

# Checking the length of the password
if(len(password) < 8):
    print("Your password must contain at least 8 characters")

# Checking for Uppercase characters 
if not (re.search(r"[A-Z]",password)):
    print("Your passowrd must contain at least one Uppercase charcter")
else:
    u = u + 1

# Checking for lowercase characters 
if not (re.search(r"[a-z]",password)):
    print("Your password must contain at least one lowercase character")
else:
    l = l + 1

# Checking for special characters 
if not re.search(r"[{!@#$%^&*-=_+,./<>?;':\"\\|}]", password):
    print("your password must contain at least one special character")
else:
    s = s + 1

# Checking for numbers 
if not re.search(r"\d", password):
    print("your password must contain at least one number")
else:
    n = n + 1

display_result(u,l,s,n)