import numpy as np
from math import log10


def main():
    # r"D:\\asd1-files\\file_a_4gb.txt
    file_name = input("Enter the filename: ") + ".txt"
    file_size = int(eval(input("Enter the size of file in bytes: ")))

    lower_bound, upper_bound = 0, 1e9
    with open(r"files\\" + file_name, "wb") as file:
        bytes_array = np.random.randint(lower_bound, upper_bound, int(file_size/4)).tobytes()
        file.write(bytes_array)


if __name__ == "__main__":
    main()
