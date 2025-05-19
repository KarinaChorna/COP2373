# Karina Chorna
# Chapter 1: Assignment 1
# the purpose of this code is to sell 20 tickets--no more than 4 tickets per buyer--and display the number of buyers

def sale(tickets_left):
    # request number of tickets from user
    tickets_ordered = int(input("How many tickets would you like to buy? 1-4: "))

    # make sure user enters a valid number of tickets, 1-4 and no more than what is remaining
    if 1 <= tickets_ordered <= 4:
        if tickets_ordered <= tickets_left:
            print("You have ordered", tickets_ordered, "tickets.")
            return tickets_ordered
        else:
            print("There are only ", tickets_left, " tickets left. Please try again.")
            return 0
    else:
        print("You must purchase at least 1 ticket and no more than 4 tickets.")
        return 0


def main():
    tickets = 20
    tickets_bought = 0
    buyers = 0

    # loop through the sale process until there are no more tickets left
    while tickets_bought < tickets:
        tickets_left = tickets - tickets_bought
        print(tickets_left, "tickets remaining.")

        # whenever a purchase of tickets is made, add another buyer
        bought = sale(tickets_left)
        if bought > 0:
            tickets_bought += bought
            buyers += 1

    # display the number of buyers that purchased the tickets
    print("All tickets have been purchased by", buyers, "buyers.")


main()
