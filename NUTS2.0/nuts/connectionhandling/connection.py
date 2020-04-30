class Connection:
    """
    The Connection class specifies the type of connection which nornir uses

    ...

    Attributes
    ----------
    logger
        instance of the logger object
    connectionMapper
        maps the platform type to the right connection
    """
    connectionMapper = {
        "cisco_ios": "Netmiko"
    }

    def define_connection(self, test_definitions):
        """
            Maps the connection type to the test_definitions
        """
        for test_definition in test_definitions.values():
            if test_definition.get_test_devices().get_platform() in self.connectionMapper:
                test_definition.set_connection(self.connectionMapper[test_definition.get_test_devices().get_platform()])
            else:
                print("This Platform is not supported")
