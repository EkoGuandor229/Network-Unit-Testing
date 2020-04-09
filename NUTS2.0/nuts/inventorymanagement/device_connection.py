class DeviceConnection:
    deviceConnectionId = 0
    device_a = 0
    device_b = 0
    connection_speed = 0

    def __init__(self, device_connection_id, device_a, device_b, connection_speed):
        self.deviceConnectionId = device_connection_id
        self.device_a = device_a
        self.device_b = device_b
        self.connection_speed = connection_speed

    def print_device_connection(self):
        print(self.deviceConnectionId, self.device_a, self.device_b, self.connection_speed)
