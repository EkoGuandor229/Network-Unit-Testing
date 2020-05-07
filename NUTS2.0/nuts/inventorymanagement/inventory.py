from nuts.inventorymanagement.device import Device
from nuts.inventorymanagement.device_connection import DeviceConnection
from nuts.utilities.file_handler import FileHandler
from pathlib import Path


class Inventory:
    def __init__(self):
        self.devices = {}
        self.device_connections = []
        self.file_handler = FileHandler()
        self.create_inventory()

    def create_device_object(self):
        file_path = Path("resources/inventory/Devices/devices.yaml")
        devices_yaml = self.file_handler.read_file(file_path)
        for device in devices_yaml:
            try:
                device_connections = self.find_device_connection(device[0])
            except ValueError:
                print(f"{device[0]}: A Problem occurred during this Class Instance")
            except KeyError:
                print(f"{device[0]}: There was a problem with the instantiation of this device")
            else:
                self.devices[device[0]] = Device(device[0], device[1], device[2], device[3], device[4],
                                                 device_connections)

    def create_device_connection_obejct(self):
        file_path = Path("resources/inventory/DeviceConnections/deviceconnections.yaml")
        device_connection_yaml = self.file_handler.read_file(file_path)
        for device_connection in device_connection_yaml:
            try:
                self.device_connections.append(
                    DeviceConnection(device_connection[0], device_connection[1], device_connection[2]))
            except ValueError:
                print("A Problem occurred during this Class Instance")

    def find_device_connection(self, router_id):
        device_connections = []
        for dev_con in self.device_connections:
            if dev_con.get_device_a() == router_id:
                device_connections.append(dev_con)
        return device_connections

    def create_inventory(self):
        self.create_device_connection_obejct()
        self.create_device_object()
