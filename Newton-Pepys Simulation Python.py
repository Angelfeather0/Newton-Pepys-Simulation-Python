import random 

option = input("What proposition would you like to simulate (A, B, C)? \n")
period = int(input("For how many throws? \n"))

if option.upper() == 'A':
    optionNumber = 1
elif option.upper() == 'B':
    optionNumber = 2
elif option.upper() == 'C':
    optionNumber = 3

sixesToss = 0
for i in range(1, period+1):
    diceToss = []
    for j in range (0, (optionNumber * 6)):
        diceToss.append(random.randint(1, 6))

    if diceToss.count(6) >= optionNumber:
        sixesToss += 1

openFile = open("Newton-Pepys Results File.txt", 'a')

string = option.upper() + ": In " + str(period) + " throws, " + str(sixesToss) + " throws had, at least, " + str(optionNumber) + " sixes in them. The probability is " + str(sixesToss/period) + "\n"

openFile.write(string)

openFile.close()