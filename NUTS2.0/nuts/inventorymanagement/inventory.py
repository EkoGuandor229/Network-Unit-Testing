from nuts.inventorymanagement.device import Device
from nuts.inventorymanagement.device_connection import DeviceConnection
from nuts.utilities.file_handler import FileHandler


class Inventory:
    devices = {}
    deviceConnections = []
    fileHandler = FileHandler()

    def __init__(self):
        self.create_inventory()

    def create_device_object(self):
        devices_yaml = self.fileHandler.read_file(r"../resources/inventory/Devices/devices.yaml")
        for device in devices_yaml:
            try:
                device_connections = self.find_device_connection(device[0])
                self.devices[device[0]] = Device(device[0], device[1], device[2], device[3], device[4], device_connections)
            except ValueError:
                print(device[0] + "A Problem occurred during this Class Instance")

    def create_device_connection_obejct(self):
        device_connection_yaml = self.fileHandler.read_file(r"../resources/inventory/DeviceConnections/deviceconnections.yaml")
        for device_connection in device_connection_yaml:
            try:
                self.deviceConnections.append(DeviceConnection(device_connection[0], device_connection[1], device_connection[2]))
            except ValueError:
                print("A Problem occurred during this Class Instance")

    def find_device_connection(self, routerid):
        device_connections = []
        for devcon in self.deviceConnections:
            if devcon.get_device_a() == routerid:
                device_connections.append(devcon)
        return device_connections

    def create_inventory(self):
        self.create_device_connection_obejct()
        self.create_device_object()


def main():
    inv = Inventory()
    inv.devices["router01"].print_device()


if __name__ == '__main__':
    main()