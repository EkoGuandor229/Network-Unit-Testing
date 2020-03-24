class FileHandler:
    logger = 0
    file = 0
    fileType = 0

    def read_file(self):
        self.text = str(self.file)

    def write_file(self):
        self.file = self.text
