from StraightMerge import StraightMerge
from time import time


def main():
    file_name = input("Enter file to sort: ")
    start = time()

    sorter = StraightMerge(f"{file_name}.txt", r"file_b", r"files_c")
    sorter.sort()

    print(f"\nFinished sorting in {time() - start} seconds.")


if __name__ == "__main__":
    main()
