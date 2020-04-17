import sys

MASTER_PASSWORD = "opensesame"

password = raw_input("Enter password: ")
attempt_count = 1

while password != MASTER_PASSWORD:

    if attempt_count > 3:
        sys.exit("Too many invalid attempts")
    password = raw_input("Invalid password:  ")
    attempt_count += 1

print ("Password correct")
