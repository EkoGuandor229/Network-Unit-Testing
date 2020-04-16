class Connection:
    logger = 0

    def define_connection(self, test_definitions):
        for test_definition in test_definitions:
            if test_definition.get_platform() == "cisco_ios":
                keyword = test_definition.get_command()
                command = "Netmiko" + keyword
                test_definition.set_command(command)
            else:
                print("This Platform is not supported")
