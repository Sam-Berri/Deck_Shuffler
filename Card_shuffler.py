import random



deck = [1, 1, 1, 1, 1 , 2, 2, 2, 2, 2, 3, 3, 4, 4]
shuffeld_deck = []

deck_size = len(deck)  



while deck_size > 0:
    
    deck_size = len(deck)  
    
    random_card = random.randint(0 , deck_size)
    
    removed_card = deck.pop(random_card - 1)

    shuffeld_deck.append(removed_card)

    deck_size = len(deck)  
    


print(shuffeld_deck)
