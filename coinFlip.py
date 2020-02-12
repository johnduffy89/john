import random

numFlips = int(input("How many flips? "))

i = 0
ones = 0
twos = 0

flips = [0] * 2

while (i < numFlips):
    flip = random.randint(1,2)
    flips[flip-1] += 1
    i+=1

for i in range(len(flips)):
    print(f"{i+1}: {flips[i]}/{numFlips} = {flips[i]/numFlips*100}%")


   
