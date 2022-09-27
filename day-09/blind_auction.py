print("Welcome to Blind Auction House")

auction_on_going = True
bidders = []

while auction_on_going:

    name = input("Please enter your name: ")
    bid = int(input("Please enter your bid price: "))

    bidders.append({
        "name": name,
        "bid": bid
    })

    prompt = input("Are there other bidders? 'yes' or 'no' ")
    
    if prompt == 'no':
        highest_bid = 0
        highest_bidder = {}
        for bidder in bidders:
            if bidder["bid"] > highest_bid:
                highest_bid = bidder["bid"]
                highest_bidder = bidder
        
        print(f"The highest bidder is {highest_bidder['name']} with a bid amount of {highest_bidder['bid']}")
        auction_on_going = False


        