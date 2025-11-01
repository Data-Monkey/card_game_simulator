import random

global hand
global deck

# card is a 2 letter string, first letter is suit, second is rank
suits = ['H', 'D', 'C', 'S'] 
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

results = [0 for _ in range(53)]  # to track results from 0 to 52 cards left


def playgame():


    # initialise deck
    deck = [s + r for s in suits for r in ranks]
    #print (deck  )

    # randomise deck (and keep track of order)
    random.shuffle(deck)
    shuffled = deck.copy()

    # deal cards 
    # compamre last card to card 4 spots prior
    # if same suit, remove cards in between
    # if same rank, remove cards in between including borders
    # 

    def matches():
        # check for matches
        #print (hand)
        if len(hand) >= 4:
            last_card = hand[-1]
            fourth_last_card = hand[-4]
            if last_card[0] == fourth_last_card[0]:
                # same suit, remove cards in between
                del hand[-3:-1]
                matches()
            elif last_card[1] == fourth_last_card[1]:
                # same rank, remove cards in between including borders
                del hand[-4:]   
                matches()   

    hand = []
    while deck:
        hand.append(deck.pop(0))
        matches()
    

    # print final hand
    #print("Shuffled deck:", shuffled)
    #print("Final hand:", hand)
    #print("Cards in Hand:", len(hand) )
    results[len(hand)] += 1


for _ in range(1000000):
    playgame()

print("Results (cards left vs frequency):")
for i in range(53):
    print(f"{i}: {results[i]}") 









