import yaml


class FileHandler:
    logger = 0
    path = 0
    fileType = 0

    def __init__(self, path):
        self.path = path

    def read_device_file(self):
        with open(self.path) as file:
            devices_yaml = []
            device_list = yaml.full_load(file)
            for device, dev in device_list.items():
                devices_yaml.append(dev)
            return devices_yaml

    def read_device_connection_file(self):
        with open(self.path) as file:
            device_connection_yaml = []
            device_connection_list = yaml.full_load(file)
            for device_connection, devcon in device_connection_list.items():
                device_connection_yaml.append(devcon)
            return device_connection_yaml

    def write_file(self, dict_file):
        with open(self.path, 'w') as file:
            devices = yaml.dump(dict_file, file)