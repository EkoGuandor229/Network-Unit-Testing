from Prototyping.Device import Device
from Prototyping.FileHandler import FileHandler


class Inventory:
    devices = {}
    deviceConnections = 0
    fileHandler = FileHandler(r"C:\Users\Janik\OneDrive\Studium\Studienarbeit\SA-Git\Network-Unit-Testing\NUTS2.0\Prototyping\Configurations\inventory\test.yaml")

    def create_device_object(self):
        devices_yaml = self.fileHandler.read_file()
        for device in devices_yaml:
            self.devices[device[2]] = Device(device[0], device[1], device[2], device[3])


def main():
    inv = Inventory()
    inv.create_device_object()
    print(inv.devices["switch01"].print_device())


if __name__ == '__main__':
    main()