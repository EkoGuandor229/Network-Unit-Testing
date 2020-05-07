from nuts.inventorymanagement.device import Device
from nuts.inventorymanagement.device_connection import DeviceConnection


def test_device_parameterss():
    test_device = Device("router01", "cisco_ios", "Cisco", "cisco", "10.20.0.31", "")
    assert test_device.get_device_id() == "router01"
    assert test_device.get_platform() == "cisco_ios"
    assert test_device.get_username() == "Cisco"
    assert test_device.get_password() == "cisco"
    assert test_device.get_hostname() == "10.20.0.31"
    assert test_device.get_device_connections() == ""


def test_device_connection_parameters():
    test_device_connection = DeviceConnection("router01", "router02", "100Mbit")
    assert test_device_connection.get_device_a() == "router01"
    assert test_device_connection.get_device_b() == "router02"
    assert test_device_connection.get_connection_speed() == "100Mbit"


def test_device_and_device_connection_link():
    test_device_connection = DeviceConnection("router01", "router02", "100Mbit")
    test_device = Device("router01", "cisco_ios", "Cisco", "cisco", "10.20.0.31", test_device_connection)
    assert test_device.get_device_connections() == test_device_connection

