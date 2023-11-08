name = input('What is your name? ')
bid = int(input('What is your bid? '))

bid_list = {}

def add_new_bid(name, bid):
    new_bid = {}
    new_bid['name'] = name
    new_bid['bid'] = bid
    bid_list.append(new_bid)

print(f'bids {bid_list}')
