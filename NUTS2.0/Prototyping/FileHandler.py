import yaml


class FileHandler:
    logger = 0
    path = 0
    fileType = 0

    def __init__(self, path):
        self.path = path

    def read_file(self):
        with open(self.path) as file:
            devices_yaml = []
            test_list = yaml.full_load(file)
            for device, dev in test_list.items():
                devices_yaml.append(dev)
            return devices_yaml

    def write_file(self, dict_file):
        with open(self.path, 'w') as file:
            devices = yaml.dump(dict_file, file)