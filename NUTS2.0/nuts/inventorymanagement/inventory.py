import logging

from nuts.inventorymanagement.device import Device
from nuts.inventorymanagement.device_connection import DeviceConnection
from nuts.utilities.file_handler import FileHandler
from pathlib import Path


class Inventory:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.devices = {}
        self.deviceConnections = []
        self.fileHandler = FileHandler()
        self.create_inventory()

    def create_device_object(self):
        file_path = Path("resources/inventory/Devices/devices.yaml")
        devices_yaml = self.fileHandler.read_file(file_path)
        for device in devices_yaml:
            try:
                device_connections = self.find_device_connection(device[0])
            except ValueError as ex:
                print(f"{device[0]}: A Problem occurred during this Class Instance")
                self.logger.exception(ex)
            except KeyError as ex:
                print(f"{device[0]}: There was a problem with the instantiation of this device")
                self.logger.exception(ex)
            else:
                self.devices[device[0]] = Device(device[0], device[1], device[2], device[3], device[4],
                                                 device_connections)
                self.logger.info('Device Object "{}" created'.format(device[0]))

    def create_device_connection_obejct(self):
        file_path = Path("resources/inventory/DeviceConnections/deviceconnections.yaml")
        device_connection_yaml = self.fileHandler.read_file(file_path)
        for device_connection in device_connection_yaml:
            try:
                self.deviceConnections.append(
                    DeviceConnection(device_connection[0], device_connection[1], device_connection[2]))
                self.logger.info('Device Connection Object for "{}" created'.format(device_connection[0]))
            except ValueError as ex:
                print("A Problem occurred during this Class Instance")
                self.logger.exception(ex)

    def find_device_connection(self, routerid):
        device_connections = []
        for devcon in self.deviceConnections:
            if devcon.get_device_a() == routerid:
                device_connections.append(devcon)
        return device_connections

    def create_inventory(self):
        self.create_device_connection_obejct()
        self.create_device_object()
