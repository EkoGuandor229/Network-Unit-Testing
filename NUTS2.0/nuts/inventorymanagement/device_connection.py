class DeviceConnection:
    """
    The Device-Connection saves information about the connection between
    two devices in a network. This class is used when testing connective
    behavior.

    ...

    Attributes
    ----------
    device_a, device_b
        reference to two specific Device-classes which are the endpoints of
        the connection
    connection_speed
        the bandwidth-speed of a given connection between two devices is used
        for some specific tests
    """
    device_a = None
    device_b = None
    connection_speed = None

    def __init__(self, device_a, device_b, connection_speed):
        self.device_a = device_a
        self.device_b = device_b
        self.connection_speed = connection_speed

    def print_device_connection(self):
        print(self.device_a, self.device_b, self.connection_speed)

    def get_device_a(self):
        return self.device_a

    def get_device_b(self):
        return self.device_b

    def get_connection_speed(self):
        return self.connection_speed
