class Device:
    """
    The Device class saves information about a device in the network, so the
    program can access this information for processing.

    ...

    Attributes
    ----------
    device_id
        The device id is used to uniquely identify a device across the
        network system.
    platform
        The platform refers to the device operating system, which determines,
        what kind of connections can be used to access the device over the
        internet.
    username
        The login name to connect to the device and execute commands on it.
    password
        The password used to authenticate the user to the device
    hostname
        The hostname is the ip-address, under which the device is accessible
        over the network.
    """

    def __init__(self, device_id, platform, username, password, hostname, device_connections):
        self.device_id = device_id
        self.platform = platform
        self.username = username
        self.password = password
        self.hostname = hostname
        self.deviceConnections = device_connections


    def get_device_id(self):

        return self.device_id

    def get_platform(self):
        return self.platform

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_hostname(self):
        return self.hostname

    def get_device_connections(self):
        return self.deviceConnections

    def print_device(self):
        print(self.device_id, self.platform, self.username, self.password, self.hostname, self.deviceConnections)
