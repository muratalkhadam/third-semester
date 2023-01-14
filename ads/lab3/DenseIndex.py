import fileinput


class DenseIndex:
    def __init__(self, data_file, index_file):
        self.data_file = data_file
        self.index_file = index_file

    def build_index(self):
        with open(self.index_file, 'w') as i_file:
            with open(self.data_file, 'r') as d_file:
                d_file.seek(0)
                i_file.seek(0)
                i_file.truncate()
                current_offset = 0
                for line in d_file:
                    # print("cur pointer at file data on", d_file.tell())
                    search_key, data = line.strip().split(',')
                    search_key = int(search_key)
                    index_entry = f"{search_key}, {current_offset}\n"
                    i_file.write(index_entry)
                    current_offset += len(line) + 1
                i_file.flush()

    def binary_search(self, search_key):
        with open(self.index_file, 'r') as i_file:
            i_file.seek(0)
            current_line = i_file.readline().strip()

            left = 0
            right = sum(1 for line in i_file) - 1

            while left <= right:
                mid = (left + right) // 2
                i_file.seek(mid)
                i_file.readline()
                current_line = i_file.readline().strip()
                key, offset = current_line.split(',')

                key = int(key)
                offset = int(offset)

                print(f"current pointer at", offset)
                print(f"our key is", key)

                if key == search_key:
                    return offset

                elif key > search_key:
                    right = mid - 1

                else:
                    left = mid + 1
            return None

    def search(self, search_key):
        offset = self.binary_search(search_key)

        with open(self.data_file, 'r') as d_file:
            if offset is not None:
                d_file.seek(offset)
                return d_file.readline()
            else:
                return None

    def insert(self, record):
        search_key, data = record.strip().split(',')
        search_key = int(search_key)
        offset = self.binary_search(search_key)

        if offset is None:
            with open(self.data_file, 'r') as d_file:
                d_file.seek(0, 2)
                offset = d_file.tell()

            with open(self.data_file, 'a') as d_file_w:
                with open(self.index_file, 'a') as i_file_w:
                    d_file_w.write('\n' + record)
                    i_file_w.seek(0, 2)

                    index_entry = f"{search_key},{offset}\n"
                    i_file_w.write(index_entry)
                    i_file_w.flush()

    def delete(self, search_key):
        offset = self.binary_search(search_key)
        if offset is not None:
            with open(self.data_file, 'w') as d_file:
                with open(self.index_file, 'r') as i_file:
                    d_file.seek(offset)
                    with open(self.data_file, 'r') as d_file_r:
                        d_file.write("*" * len(d_file_r.readline()))
                    i_file.seek(0)
                    index_data = i_file.readlines()
                    i_file.seek(0)
                    with open(self.index_file, 'w') as i_file_w:
                        i_file_w.truncate()
                    for line in index_data:
                        if not str(search_key) in line:
                            with open(self.index_file, 'w') as i_file_w:
                                i_file_w.write(line)
                    i_file.flush()

    def update(self, search_key, new_data):
        offset = self.binary_search(search_key)

        with open(self.data_file, 'r+') as d_file:
            if offset is not None:
                d_file.seek(offset)

                current_line = d_file.readline()
                key, data = current_line.strip().split(',')

                new_line = f"{key}, {new_data}\n"
                d_file.seek(offset)

                with open(self.data_file, 'r+') as d_file:
                    for line in fileinput.input(self.data_file):
                        d_file.write(line.replace(current_line, new_line))

                    # d_file.flush()
            else:
                print(f"Record with key {search_key} not found.")


if __name__ == '__main__':
    data_file = "files/data.txt"
    index_file = "files/index.txt"

    di = DenseIndex(data_file, index_file)
    di.build_index()

    result = di.search(111)
    print(result)  # Output: "3, record 3"
