def main():

    while True:
        change = float(input("How much change do you need? "))

        if (change > 0):
            break

    change = (int(change * 100))

    quarters = change / 25

    remainder = change % 25

    dimes = remainder / 10

    remainder = remainder % 10

    nickels = remainder / 5

    remainder = remainder % 5

    print(int(quarters + dimes + nickels + remainder))

if __name__ == '__main__':
    main()