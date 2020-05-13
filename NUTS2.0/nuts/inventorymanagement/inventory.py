import logging

from nuts.inventorymanagement.device import Device
from nuts.inventorymanagement.device_connection import DeviceConnection
from nuts.utilities.file_handler import FileHandler
from pathlib import Path

from nuts.utilities.progress_bar_handler import ProgressBarHandler


class Inventory:
    """
    The Inventory Class creates the Device and DeviceConnection Objects and
    links the Device Connections to the right Devices

    ...

    Attributes
    ----------
    logger
        Instance of the logger Class
    devices
        The created Devices in a Dictionary with the Device Id as Key
    device_connections
        The created device_connections in an Array to link with the Devices
    file_handler
        Instance of the Class file_handler
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.progress_bar = ProgressBarHandler()
        self.devices = {}
        self.device_connections = []
        self.file_handler = FileHandler()
        self.create_inventory()


    def create_device_object(self):
        """
        Creates the Device Objects and Links the DeviceConnection Objects to them
        """
        file_path = Path("resources/inventory/Devices/devices.yaml")
        devices_yaml = self.file_handler.read_file(file_path)
        self.progress_bar.initiate_progress_bar(len(devices_yaml), "Create Device Objects from YAML")
        for device in devices_yaml:
            self.progress_bar.update_progress_bar(1)
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
                                                 device_connections, device[5])
                self.logger.info('Device Object "{}" created'.format(device[0]))
        self.progress_bar.clear_progress_bar()

    def create_device_connection_object(self):
        """
         Creates the DeviceCOnnection Objects
        """
        file_path = Path("resources/inventory/DeviceConnections/deviceconnections.yaml")
        device_connection_yaml = self.file_handler.read_file(file_path)
        for device_connection in device_connection_yaml:
            try:
                self.device_connections.append(
                    DeviceConnection(device_connection[0], device_connection[1], device_connection[2]))
                self.logger.info('Device Connection Object for "{}" created'.format(device_connection[0]))
            except ValueError as ex:
                print("A Problem occurred during this Class Instance")
                self.logger.exception(ex)

    def find_device_connection(self, router_id):
        """
        Helper Method to map the right DeviceConnection to the Devices
        """
        device_connections = []
        for dev_con in self.device_connections:
            if dev_con.get_device_a() == router_id:
                device_connections.append(dev_con)
        return device_connections

    def create_inventory(self):
        """
        Runs all te Methods in the correct order
        """
        self.create_device_connection_object()
        self.create_device_object()
