#CAESAR CIPHER ENCRYPTION
inputString = input("Enter string to encrypt: ")
numberOfShifts = int(input("Enter number of shifts: "))
encryptedString = ""
upperLimit = 0
lowerLimit = 0
length = len(inputString)

#CORE Logic
for i in range(0, length):
    alphabet = inputString[i]
    alphabetASCII = ord(alphabet)
    calculatedASCII = 0
    if(alphabetASCII >= 97):
        #transform small letters
        lowerLimit = 97
        upperLimit = 122
        calculatedASCII = alphabetASCII + numberOfShifts
        if(calculatedASCII > upperLimit):
            calculatedASCII -=upperLimit
            calculatedASCII += lowerLimit - 1
            encryptedString += chr(calculatedASCII)
        else:
            encryptedString += chr(calculatedASCII)
    elif (alphabetASCII >= 65 and alphabetASCII <= 90):
        #transform CAPITAL letters
        lowerLimit = 65
        upperLimit = 90
        calculatedASCII = alphabetASCII + numberOfShifts
        if(calculatedASCII > upperLimit):
            calculatedASCII -=upperLimit

            # Minus one so that shift starts from 65 instead of 66

            calculatedASCII += lowerLimit - 1
            encryptedString += chr(calculatedASCII)
        else:
            encryptedString += chr(calculatedASCII)
    elif (alphabet == " "):
        encryptedString += " "

#printing result
print(encryptedString)