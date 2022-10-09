from StraightMerge import StraightMerge


def main():
    file_name = input("Enter file to sort: ")

    sorter = StraightMerge(f"D:/asd1-files/{file_name}.txt",
                           r"D:\\asd1-files\\b_file.bin",
                           r"D:\\asd1-files\\c_file.bin")

    sorter.sort()
    print(sorter)


if __name__ == "__main__":
    main()
