from Prototyping.Device import Device
from Prototyping.DeviceConnection import DeviceConnection
from Prototyping.FileHandler import FileHandler


class Inventory:
    devices = {}
    deviceConnections = {}
    deviceFileHandler = FileHandler(r"C:\Users\Janik\OneDrive\Studium\Studienarbeit\SA-Git\Network-Unit-Testing\NUTS2.0\Prototyping\Configurations\inventory\\Devices\devices.yaml")
    deviceConnectionFileHandler = FileHandler(r"C:\Users\Janik\OneDrive\Studium\Studienarbeit\SA-Git\Network-Unit-Testing\NUTS2.0\Prototyping\Configurations\inventory\DeviceConnections\deviceconnections.yaml")

    def create_device_object(self):
        devices_yaml = self.deviceFileHandler.read_device_file()
        for device in devices_yaml:
            self.devices[device[2]] = Device(device[0], device[1], device[2], device[3])

    def create_device_connection_obejct(self):
        device_connection_yaml = self.deviceConnectionFileHandler.read_device_connection_file()
        for device_connection in device_connection_yaml:
            self.deviceConnections[device_connection[0]] = DeviceConnection(device_connection[0], device_connection[1], device_connection[2], device_connection[3])

    def create_inventory(self):
        self.create_device_object()
        self.create_device_connection_obejct()


def main():
    inv = Inventory()
    inv.create_device_object()
    print(inv.devices["switch01"].print_device())
    inv.create_device_connection_obejct()
    print(inv.deviceConnections["switch01toswitch02"].print_device_connection())


if __name__ == '__main__':
    main()