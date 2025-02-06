# Taking password input 
password = input("Enter your password: ")

# defining variables 
list_of_special_characters = '''"'!@#$%^&*()-=_+,./<>?;:'''
list_of_numbers = '''1234567890'''
u = 0 # for upper case 
l = 0 # for lower case 
s = 0 # for special characters
n = 0 # for number
# Checking the length of the password
if(len(password) > 8):
    print("Your password must contain at least 8 characters")

# Checking for Lower and upper characters
for i in range(1, len(password)):
    if(str(password[i]) == password.isupper()):
        u = u + 1
    if(str(password[i]) == password.islower()):
        l = l + 1

# Checking for special characters
for i in range(0, len(password)):
    if(str(password[i]) == list_of_special_characters[i]):
        s = s + 1 

# Checking for numbers 
for i in range(1, len(password)):
    if(str(password[i]) == list_of_numbers[i]):
        n = n + 1 
    
# defining function for displaying password
def display_password(u, l , s):
    if(u > 0 and l > 0 and s > 0):
        print("Your password is strong")
    else:
        print("Your password doesnot satisfy all the conditions")
