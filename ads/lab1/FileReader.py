class FileReader:
    def __init__(self, file_path: str):
        self.path = file_path
        self.file = open(file_path, "rb")
        self.curr = int.from_bytes(self.file.read(32), byteorder='big')
        self.next_num = int.from_bytes(self.file.read(32), byteorder='big')

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.curr
        self.curr = self.next_num
        self.next_num = int.from_bytes(self.file.read(32), byteorder='big')
        return temp

    def read_32(self):
        self.file.read(32)

    def close(self):
        self.file.close()
