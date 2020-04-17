import sys

attempt_count = 1
user_name = raw_input("What is your name?:   ")
ask_if_understand = raw_input("Hello there {}! Do you understand Python loop? Answer with [Yes or No]   ".format(user_name))

while ask_if_understand != "Yes":

    if attempt_count > 3:
        sys.exit("Too many attempt in one setting. Exiting application")
    ask_if_understand = raw_input("Oh no that's too bad. Type in [Yes] when you understand it!:   ")
    attempt_count += 1

print ("Yes!!! Way to go!")
