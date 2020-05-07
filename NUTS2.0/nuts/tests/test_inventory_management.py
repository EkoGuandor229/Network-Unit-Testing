from nuts.inventorymanagement.device import Device


class TestInventoryManagement:

    def test_device_id(self):
        test_device = Device("router01", "cisco_ios", "Cisco", "cisco", "10.20.0.31", "")
        assert test_device.get_device_id() == "router01"

    def test_device_platform(self):
        test_device = Device("router01", "cisco_ios", "Cisco", "cisco", "10.20.0.31", "")
        assert test_device.get_platform() == "cisco_ios"