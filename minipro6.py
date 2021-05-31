# Author - Kishan Sindhi
# date - 31-5-2021
# discription - This is a simple function of email slicing 
# here you can enter your email id and this function will return you your "username" & "domain"


email = input("Enter your email id\n")
username = email[:email.index("@")]
domain  = email[email.index("@")+1:]
print(f"Your username is '{username}' and your domain is '{domain}'")
