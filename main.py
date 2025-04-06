
# Password Validator Project
# Maria - Validation Logic | Franklin - User Interface

import re

#Password rules display to the user
rules = [
    "✨ Contains 8–16 characters",
    "🔒 Contains one of the special characters: %$#^&*!@()",
    "🔢 Contains at least one number 0–9",
    "🔠 Contains at least one capital letter",
    "🔤 Starts with a lowercase letter",
    "🚫 Does not contain the phrase 'pass'",
    "🚫 Does not contain the phrase 'qwerty'",
    "🚫 Does not contain the phrase '123'",  
]

#Show rules to the user
def show_rules():
    print("\nThe password must follow these rules: \n\t\t")
    for rule in rules:
        print(rule)

#This will be replaced by Logic Function
def validate_password(password):
    return []

#Start user interface
show_rules()

#Ask user for password
password = input("\nPlease enter a password that conforms to the above restrictions:\n\t\t")
    print(f"Your password is: {password}")


#chech if the password meets the rules

#Show Results 
violations = validate_password(password)

if violations:
    print("\nThis password does not meet the following requirements:")
    for rule in violations:
        print(f'-{rule}')
else:
    print("\n🎉Success! Your Password meets all the requirements.")