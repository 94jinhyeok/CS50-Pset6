import sys

def cardType(number):
    if (number == 4):
        return "Visa"
    elif (number == 5):
        return "Mastercard"
    elif (number == 3):
        return "Amex"
    else:
        return "Valid but not found"

def getLastNumber(number):
    return number % 10

def main():

    while True:
        cardNumber = int(input("What is your credit card number? (Totally not shady):  "))

        if (cardNumber > 0):
            break

    cardLength = cardNumber
    counter = 0
    evenSum = 0
    oddSum = 0

    while True:
        cardLength //= 10
        counter += 1

        if (cardLength == 0):
            break

    cardLength = counter

    if (cardLength < 13 or cardLength > 16):
        print("Invalid")

    else:
        cardArray = []

        for i in range(cardLength):

            if (cardNumber):
                cardArray.append(getLastNumber(cardNumber))
                cardNumber //= 10

        for i in range(cardLength):

            if (i % 2 != 0):

                if (cardArray.index(i) * 2 >= 10):
                    oddSum += getLastNumber(cardArray.index(i) * 2)
                    oddSum += 1

                else:
                    oddSum += cardArray.index(i) * 2

            else:
                evenSum += cardArray.index(i)

        total = evenSum + oddSum

        if (getLastNumber(total) == 0):
            print(cardType(cardArray[cardLength -1]))

        else:
            print("Invalid")


if __name__ == '__main__':
    main()