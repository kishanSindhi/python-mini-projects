email = input("Enter your email id\n")
username = email[:email.index("@")]
domain  = email[email.index("@")+1:]
print(f"Your username is '{username}' and your domain is '{domain}'")