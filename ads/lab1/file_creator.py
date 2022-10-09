from random import randint


def main():

    file_name = r"D:\\asd1-files\\" + input("Enter the filename: ") + ".txt"
    number_amount = int(eval(input("Enter amount of number to generate: ")))

    lower_bound, upper_bound = 1, 1000000

    with open(file_name, "wb") as a:
        # multiply by 32 for file size
        for i in range(number_amount):
            a.write(randint(lower_bound, upper_bound).to_bytes(32, byteorder="big"))


if __name__ == "__main__":
    main()
