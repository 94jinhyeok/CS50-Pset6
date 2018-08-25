import sys

def main():

    while True:
        height = input("Height: ")

        if height and not height.isalpha():
            height = int(height)
            if (height >= 0 and height <= 23):
                break

    for i in range(height):

        for j in range(height - i - 1):
            sys.stdout.write(" ")

        for k in range(i + 1):
            sys.stdout.write("#")

        sys.stdout.write("  ")

        for l in range(i + 1):
            sys.stdout.write("#")

        sys.stdout.write("\n")


if __name__ == '__main__':
    main()