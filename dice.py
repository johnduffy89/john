import random

roll =  random.randint(1,6)

i = 0


test_text = input ("How many rolls? ")
test_number = int(test_text)

one = 0
two = 0


while(i< test_number):
    roll = random.randint(1,6)
    
    i+=1

    if roll == 1:
      
        one += 1
        quot = dice/ test_number
        print ("1. ",dice,"/" ,test_number, " = ",quot )
    elif roll == 2:
        two += 1
        quot = two/ test_number
        print("2. ",two,"/",test_number, " = ",quot)
    elif roll == 3:
        three= 0
        three += 1
        quot = three/ test_number
        print("3. ",three,"/" ,test_number, " = ",quot)
    elif roll == 4:
        four  = 0
        four += 1
        quot = four/ test_number
        print("4. ",four,"/" ,test_number, " = ",quot)
    elif roll == 5:
        five  = 0
        five += 1
        quot = five/ test_number
         print("5. ",five,"/" ,test_number, " = ",quot)
    else:
        six = 0
        six += 1
        quot = six/ test_number
        print("6. ",six,"/" ,test_number, " = ",quot)
                
# here


    
    
