class Device:
    deviceId = 0
    platform = 0
    username = 0
    password = 0
    hostname = 0
    deviceConnections = []

    def __init__(self, deviceid, platform, username, password, hostname, device_connections):
        self.deviceId = deviceid
        self.platform = platform
        self.username = username
        self.password = password
        self.hostname = hostname
        self.deviceConnections = device_connections

    def get_platform(self):
        return self.platform

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_hostname(self):
        return self.hostname

    def print_device(self):
        print(self.deviceId, self.platform, self.username, self.password, self.hostname, self.deviceConnections)
