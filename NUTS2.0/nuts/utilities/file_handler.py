import yaml


class FileHandler:
    logger = 0
    devicePath = r"../nuts/resources/inventory/Devices/devices.yaml"
    deviceConnectionPath = r"../nuts/resources/inventory/DeviceConnections/deviceconnections.yaml"
    testDefinitionPath = r"../nuts/resources/inventory/TestDefinitions/testDefinitions.yaml"
    fileType = 0

    def read_device_file(self):
        with open(self.devicePath) as file:
            devices_yaml = []
            device_list = yaml.full_load(file)
            for device, dev in device_list.items():
                devices_yaml.append(dev)
            return devices_yaml

    def read_device_connection_file(self):
        with open(self.deviceConnectionPath) as file:
            device_connection_yaml = []
            device_connection_list = yaml.full_load(file)
            for device_connection, devcon in device_connection_list.items():
                device_connection_yaml.append(devcon)
            return device_connection_yaml

    def read_test_definition_file(self):
        with open(self.testDefinitionPath) as file:
            test_definition_yaml = []
            test_definition_list = yaml.full_load(file)
            for test_definition, tedef in test_definition_list.items():
                test_definition_yaml.append(tedef)
            return test_definition_yaml

    def write_file(self, dict_file):
        with open(self.path, 'w') as file:
            devices = yaml.dump(dict_file, file)