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
                    current_offset += len(line)
                i_file.flush()

    # def build_index(self):
    #     with open(self.data_file, 'r') as d_file:
    #         with open(self.index_file, 'w') as i_file:
    #             # Iterate through each record in the data.txt file
    #             for i, record in enumerate(d_file):
    #                 search_key = int(record.split(',')[0])
    #                 # Add an index entry for the search key, pointing to the record's location
    #                 index_entry = f"{search_key},{i}\n"
    #                 i_file.write(index_entry)
    #             i_file.flush()

    # def binary_search(self, search_key):
    #     with open(self.index_file, "r") as i_file:
    #         i_file.seek(0)
    #         right = sum(1 for line in i_file) - 1
    #         left = 0
    #
    #         while left <= right:
    #             mid = (left + right) // 2
    #             i_file.seek(mid)
    #             i_file.readline()
    #             current_line = i_file.readline().strip()
    #             key, offset = current_line.split(',')
    #             print(key, "--->>", offset)
    #             print("we still searching for", search_key)
    #
    #             key = int(key)
    #             offset = int(offset)
    #             if key == search_key:
    #                 return offset
    #             elif key < search_key:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    #         return None

    def binary_search(self, search_key):
        with open(self.index_file, "r") as i_file:
            i_file.seek(0)
            left = 0
            right = sum(1 for line in i_file) - 1
            print("right is", right)
            while left <= right:
                mid = (left + right) // 2
                print("--"*10, mid)
                i_file.seek(mid)
                print("tell is", i_file.tell())
                i_file.readline()

                current_line = i_file.readline().strip()
                print("current line is", current_line)

                key, line_number = current_line.split(',')
                print("so key will be", key)

                key = int(key)
                line_number = int(line_number)
                print(f"key {key} to compare with {search_key}")
                if key == search_key:
                    with open(self.data_file, 'r') as d_file:
                        d_file.seek(0)
                        for i in range(line_number):
                            current_line = d_file.readline()
                            current_position = d_file.tell()
                            offset = current_position - len(current_line)
                            # print( "current line is", current_line , "with pos at", current_position, "offset will be", offset)
                        return offset
                elif key < search_key:
                    left = mid + 1
                else:
                    right = mid - 1
            return None

    def search(self, search_key):
        print("search key is", search_key)
        offset = self.binary_search(search_key)
        print(f"for {search_key} offset value is {offset}")
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
        else:
            print("Record already exists with the same search key.")

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

            print("Record with search key", search_key, "was deleted.")
        else:
            print("Record not found.")

    def update(self, record):
        search_key, data = record.strip().split(',')
        search_key = int(search_key)

        with open(self.data_file, 'r+') as d_file_r_w:
            for line in fileinput.input(self.data_file):
                if str(search_key) == line[:line.find(',')]:
                    d_file_r_w.write(line.replace(line[line.find(',')+1:], data))

        offset = self.binary_search(search_key)

        if offset is not None:
            with open(self.data_file, 'a') as d_file:
                with open(self.index_file, 'r') as i_file:
                    d_file.seek(offset)
                    d_file.write(record)
                    i_file.seek(0)
                    index_data = i_file.readlines()
                    i_file.seek(0)
                    with open(self.index_file, 'a') as i_file_w:
                        i_file_w.truncate()

                    for line in index_data:
                        with open(self.index_file, 'w') as i_file_w:
                            if not str(search_key) in line:
                                i_file_w.write(line)
                            else:
                                i_file_w.write(f"{search_key},{offset}\n")
                    i_file.flush()
        else:
            print("Record not found.")


if __name__ == '__main__':
    data_file = "data.txt"
    index_file = "index.txt"

    di = DenseIndex(data_file, index_file)
    di.build_index()

    result = di.search(111)
    print(result)  # Output: "3, record 3"
