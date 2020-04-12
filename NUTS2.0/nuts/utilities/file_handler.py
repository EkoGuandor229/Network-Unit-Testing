import yaml


class FileHandler:
    logger = 0
    devicePath = r"../resources/inventory/Devices/devices.yaml"
    deviceConnectionPath = r"../resources/inventory/DeviceConnections/deviceconnections.yaml"
    testDefinitionPath = r"../resources/inventory/TestDefinitions/testDefinitions.yaml"

    def read_device_file(self):
        try:
            with open(self.devicePath) as file:
                devices_yaml = []
                device_list = yaml.full_load(file)
                try:
                    for device, dev in device_list.items():
                        devices_yaml.append(dev)
                    return devices_yaml
                except ValueError:
                    print("Device Information are not entered correctly")
        except IOError:
            print("Inputfile not found")

    def read_device_connection_file(self):
        try:
            with open(self.deviceConnectionPath) as file:
                device_connection_yaml = []
                device_connection_list = yaml.full_load(file)
                try:
                    for device_connection, devcon in device_connection_list.items():
                        device_connection_yaml.append(devcon)
                    return device_connection_yaml
                except ValueError:
                    print("DeviceConnection Information are not in the right Format")
        except IOError:
            print("Inputfile not found")

    def read_test_definition_file(self):
        try:
            with open(self.testDefinitionPath) as file:
                test_definition_yaml = []
                test_definition_list = yaml.full_load(file)
                try:
                    for test_definition, tedef in test_definition_list.items():
                        test_definition_yaml.append(tedef)
                    return test_definition_yaml
                except ValueError:
                    print("TestDefinition Information are not in the right Format")
        except IOError:
            print("Inputfile not found")