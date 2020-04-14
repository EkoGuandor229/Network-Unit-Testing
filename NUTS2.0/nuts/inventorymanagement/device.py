class Device:
    deviceId = 0
    platform = 0
    username = 0
    password = 0
    hostname = 0
    deviceConnections = []

    def __init__(self, deviceid, platform, username, password, address, device_connections):
        self.deviceId = deviceid
        self.platform = platform
        self.username = username
        self.password = password
        self.hostname = address
        self.deviceConnections = device_connections

    def print_device(self):
        print(self.deviceId, self.platform, self.username, self.password, self.hostname, self.deviceConnections)
