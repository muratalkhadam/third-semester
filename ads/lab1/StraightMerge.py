from FileReader import FileReader
from time import time
from itertools import count
import os


class StraightMerge:
    def __init__(self, file_a, file_b, file_c):
        self.start = time()

        self.file_a = file_a
        self.file_b = file_b
        self.file_c = file_c

        self.clear_file(file_b)
        self.clear_file(file_c)

    @staticmethod
    def clear_file(file):
        with open(file, "wb") as f:
            pass

    def is_sorted(self):
        file = FileReader(self.file_a)

        while file.next_num:
            if file.next_num < file.curr:
                file.close()
                return False
            next(file)
        file.close()
        return True

    def distribute(self, serie_len):
        counter = 0

        a = FileReader(self.file_a)
        b = open(self.file_b, "wb")
        c = open(self.file_c, "wb")

        while a.curr:
            if counter % 2 == 0:
                for i in range(serie_len):
                    b.write(next(a).to_bytes(32, byteorder="big"))
            else:
                for i in range(serie_len):
                    c.write(next(a).to_bytes(32, byteorder="big"))

            counter += 1

        a.close()
        b.close()
        c.close()

    def merge(self, serie_len):
        b = FileReader(self.file_b)
        c = FileReader(self.file_c)

        with open(self.file_a, "wb") as binary_writer:
            while b.curr and c.curr:
                counter_b = 0
                counter_c = 0
                # собираю в зависимости от длины
                while counter_b + counter_c != 2 * serie_len:
                    if (b.curr <= c.curr and counter_b < serie_len) or counter_c == serie_len:
                        binary_writer.write(b.curr.to_bytes(32, byteorder="big"))
                        counter_b += 1
                        next(b)
                    else:  # if b.curr > c.curr and counter_c < serie_len:
                        binary_writer.write(c.curr.to_bytes(32, byteorder="big"))
                        counter_c += 1
                        next(c)

            while b.curr:
                binary_writer.write(b.curr.to_bytes(32, byteorder="big"))
                next(b)

        binary_writer.close()
        b.close()
        c.close()

    def sort(self):
        serie_len = 1
        for i in count(1):
            if self.is_sorted():
                os.remove(self.file_b)
                os.remove(self.file_c)
                return

            self.distribute(serie_len)
            print(f"\nAfter distribution #{i}")
            print("a: " + self.read(self.file_a))
            print("b: " + self.read(self.file_b))
            print("c: " + self.read(self.file_c))

            self.merge(serie_len)
            print(f"\nAfter merging #{i}")
            print("b: " + self.read(self.file_b))
            print("c: " + self.read(self.file_c))
            print("a: " + self.read(self.file_a))

            serie_len *= 2

    @staticmethod
    def read(path: str) -> str:
        s = ""
        f = FileReader(path)

        for _ in range(50):
            if not f.curr:
                break
            s += str(f.curr) + " "
            next(f)

        f.close()
        return s
