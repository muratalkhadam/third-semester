from random import randint


def main():
    file_name = "test.txt"
    max_n = 1_000
    n = int(input("Enter amount of numbers: "))

    with open(file_name, "wb") as a:
        for i in range(n):
            a.write(randint(1, max_n).to_bytes(32, byteorder="big"))


if __name__ == "__main__":
    main()
