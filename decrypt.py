#CAESAR CIPHER DECRYPTION
inputString = input("Enter string to decrypt: ")
numberOfShifts = int(input("Enter number of shifts: "))
decryptedString = ""
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
        calculatedASCII = alphabetASCII - numberOfShifts
        if(calculatedASCII < lowerLimit):
            calculatedASCII = lowerLimit - calculatedASCII
            calculatedASCII = (upperLimit + 1) - calculatedASCII
            decryptedString += chr(calculatedASCII)
        else:
            decryptedString += chr(calculatedASCII)
    elif (alphabetASCII >= 65 and alphabetASCII <= 90):
        #transform CAPITAL letters
        lowerLimit = 65
        upperLimit = 90
        calculatedASCII = alphabetASCII - numberOfShifts
        if(calculatedASCII < lowerLimit):
            calculatedASCII = lowerLimit - calculatedASCII

            

            calculatedASCII = (upperLimit + 1) - calculatedASCII
            decryptedString += chr(calculatedASCII)
        else:
            decryptedString += chr(calculatedASCII)
    elif (alphabet == " ") :
        decryptedString += " "
    

#printing result
print(decryptedString)