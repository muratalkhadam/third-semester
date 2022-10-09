from FileReader import FileReader
from time import time, sleep


class StraightMerge:
    def __init__(self, file_a, file_b, file_c):
        self.start = time()

        self.file_a = file_a
        self.file_b = file_b
        self.file_c = file_c

    def __str__(self):
        print(f"Sorting finished in {time() - self.start}")

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
        return True

    def distribute(self, serie_len):
        counter = 0

        a = FileReader(self.file_a)
        b = open(self.file_b, "wb")
        c = open(self.file_c, "wb")

        while a.next_num:
            if counter % 2 == 0:
                for i in range(serie_len):
                    b.write(a.curr)
            else:
                for i in range(serie_len):
                    c.write(a.curr)

            next(a)
            counter += 1

        a.close()
        b.close()
        c.close()

    def merge(self, serie_len):
        b = FileReader(self.file_b)
        c = FileReader(self.file_c)

        with open(self.file_a, "wb") as binary_writer:
            # while is not EOF
            while not c.is_eof():
                counter_b = 0
                counter_c = 0

                # собираю в зависимости от длины
                while counter_b < serie_len and counter_c < serie_len:
                    if b.curr <= c.curr:
                        binary_writer.write(next(b))
                        counter_b += 1

                        while counter_c < serie_len:
                            binary_writer.write(next(c))
                            counter_c += 1
                    else:
                        binary_writer.write(next(c))
                        counter_c += 1

                        while counter_b < serie_len:
                            binary_writer.write(next(b))
                            counter_b += 1

            while b.next_num:
                binary_writer.write(next(b))

        binary_writer.close()
        b.close()
        c.close()

    def sort(self):
        serie_len = 1

        # for _ in range(1, int(log2(self.file_a_size / 32))):
        while not self.is_sorted():
            self.distribute(serie_len)
            print(f'Distrubion with the {serie_len} length successfully finish...')
            sleep(10)
            self.merge(serie_len)
            print(f'Merging with the {serie_len} length successfully finish...')

            serie_len *= 2
