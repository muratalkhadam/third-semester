class FileReader:
    def __init__(self, file_path: str):
        self.path = file_path
        self.file = open(file_path, "rb")
        self.curr = self.file.read(32)
        self.next_num = self.file.read(32)

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.curr
        self.curr = self.next_num
        self.next_num = self.file.read(32)
        return temp

    def read_32(self):
        self.file.read(32)

    def close(self):
        self.file.close()

    def is_eof(self):
        if self.file.read(1) == b'':
            return True
        return False
