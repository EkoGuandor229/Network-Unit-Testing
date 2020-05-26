class Connection:
    """
    The Connection class specifies the type of connection which nornir uses

    ...

    Attributes
    ----------
    connectionMapper
        dictionary that maps the platform type to the right connection
    """
    connectionMapper = {
        "cisco_ios": ["Napalm", "Netmiko"],
        "EOS": ["Napalm", "Netmiko"],
        "IOSXR": ["Napalm", "Netmiko"],
        "JUNOS": [["Napalm", "Netmiko"]],
        "NXOS": ["Napalm", "Netmiko"],
        "NXOS_SSH": ["Napalm", "Netmiko"]
    }

    def define_connection(self, test_definitions):
        """
            Maps the connection type to the test_definitions with the connecionMapper
        """
        for test_definition in test_definitions.values():
            device_os = test_definition.get_test_devices().get_platform()
            if device_os in self.connectionMapper:
                test_definition.set_connection(self.connectionMapper[device_os])
            else:
                print("This Platform is not supported")
