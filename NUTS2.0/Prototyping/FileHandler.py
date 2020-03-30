import yaml


class FileHandler:
    logger = 0
    path = 0
    fileType = 0

    def __init__(self, path):
        self.path = path

    def read_file(self):
        with open(self.path) as file:
            test_list = yaml.full_load(file)
            for device, dev in test_list.items():
                print(device, ":", dev)

    def write_file(self, dict_file):
        with open(self.path, 'w') as file:
            devices = yaml.dump(dict_file, file)

def main():
    fh = FileHandler(r"C:\Users\Janik\OneDrive\Studium\Studienarbeit\SA-Git\Network-Unit-Testing\NUTS2.0\Prototyping\Configurations\inventory\test.yaml")
    fh.read_file()
    dict_file = [{'switch01': ['255.255.255.0', '785435647839', 'ins']}]
    fh1 = FileHandler(r"C:\Users\Janik\OneDrive\Studium\Studienarbeit\SA-Git\Network-Unit-Testing\NUTS2.0\Prototyping\Configurations\inventory\testWriteFile.yaml")
    fh1.write_file(dict_file)


if __name__ == '__main__':
    main()