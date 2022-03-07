import random 

period = int(input("For how many throws? \n"))

optionNumber = 1
string = ""
for proposition in range(0, 3):
    sixesToss = 0

    for throw in range(1, period+1):
        diceToss = []

        for dice in range (0, (optionNumber * 6)):
            diceToss.append(random.randint(1, 6))

        if diceToss.count(6) >= optionNumber:
            sixesToss += 1

    string += "In " + str(period) + " throws, " + str(sixesToss) + " throws had, at least, " + str(optionNumber) + " sixes in them. The probability is " + str(sixesToss/period) + "\n"

    optionNumber += 1

openFile = open("Newton-Pepys Results File.txt", 'a')

openFile.write(string)

openFile.close()