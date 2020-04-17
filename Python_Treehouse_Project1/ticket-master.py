import sys

TICKET_PRICE = 10
ticket_remaining = 100
SERVICE_CHARGE = 2


def calculate_final_price(number_of_request_ticket, price, service_charge):
    return (number_of_request_ticket * price) + service_charge


while ticket_remaining >= 0:

    if ticket_remaining > 0:
        print "There're only {} tickets remaining!".format(ticket_remaining)
    else:
        print "Tickets are all out of stock! Come back next time"

    user_name = raw_input("Hi! What's your name?   ")

    number_of_ticket_being_sold = raw_input("Hi {}! How many tickets do you want?   ".format(user_name))

    try:
        number_of_ticket_being_sold = int(number_of_ticket_being_sold)
        if number_of_ticket_being_sold > ticket_remaining:
            raise ValueError("You're buying more tickets than we have!")
    except ValueError as err:
        print "Invalid number {}. Try again".format(err)
    else:

        user_pay = calculate_final_price(number_of_ticket_being_sold, TICKET_PRICE, SERVICE_CHARGE)

        print "You are purchasing {} tickets".format(number_of_ticket_being_sold), "for ${}".format(user_pay)

        proceed_to_pay = raw_input("Confirm purchase? [y/n]   ")
        if proceed_to_pay == "y":
            if number_of_ticket_being_sold <= ticket_remaining:
                print "Purchase confirm"
            else:
                print "Uh oh! Not enough tickets in stock for your order"
            ticket_remaining -= number_of_ticket_being_sold

        else:
            print "Thanks for your interest {}".format(user_name)

sold_out = "Sorry! Tickets are all sold out!"
print sold_out
