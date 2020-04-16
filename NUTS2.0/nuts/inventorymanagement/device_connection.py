class DeviceConnection:
    device_a = 0
    device_b = 0
    connection_speed = 0

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
