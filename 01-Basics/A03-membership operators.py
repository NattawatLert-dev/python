# Membership operators = used to test whether a value or variables is found in a sequence
#                        (string, list, tuple, set, or collectionary)
#                        1. in
#                        2. not in

#Ex.1
word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

#EX.2
grade = {"Sandy": "A", "Squidward": "B", "Spongebob": "C", "Patrick": "D"}

student = input("Enter the name of a student:")

if student in grade:
    print(f"{student}'s grade is {grade[student]}")
else:
    print(f"{student} was not found")

#EX.3
email = "Tle@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")