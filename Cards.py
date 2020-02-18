deck = []

suits = ["♠", "♥", "♣", "♦"]
for i in range(4):
    for j in range(1,14):
        value = str(j)
        if(i == 0):
            suit = "spade"
        if(j==11):
            value = "J"
        elif(j == 12):
            value = "Q"
        elif(j == 13):
            value = "K"
        elif(j == 1):
            value = "A"
        deck.append(f"{value}{suits[i]}")


print(deck)
        
