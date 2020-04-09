class Device:
    username = 0
    password = 0
    deviceId = 0
    adress = 0

    def __init__(self, username, password, deviceId, adress):
        self.username = username
        self.password = password
        self.deviceid = deviceId
        self.adress = adress

    def print_device(self):
        print(self.username, self.password, self.deviceid, self.adress)