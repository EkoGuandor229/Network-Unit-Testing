from nornir.plugins.functions.text import print_result

from nuts.testcreation.network_test_strategy_factory import TestStrategyFactory


class TestContext:
    factory_instance = TestStrategyFactory()
    tests = []
    tests.append(factory_instance.factory_method("Netmiko", "cisco_ios", "10.20.0.31", "cisco", "cisco", "172.16.255.1"))
    tests.append(factory_instance.factory_method("Netmiko", "cisco_ios", "10.20.0.32", "cisco", "cisco", "172.16.255.1"))
    tests.append(factory_instance.factory_method("Netmiko", "cisco_ios", "10.20.0.33", "cisco", "cisco", "172.16.255.1"))
    tests.append(factory_instance.factory_method("Netmiko", "cisco_ios", "10.20.0.34", "cisco", "cisco", "172.16.255.1"))
    tests.append(factory_instance.factory_method("Netmiko", "cisco_ios", "10.20.0.35", "cisco", "cisco", "172.16.255.1"))

    def run_all_tests(self):
        for test in self.tests:
            result = test.run_test()
            evaluation = test.evaluate_result((result["host1"][0]))
            print(evaluation)
            print_result(result)


def main():
    context = TestContext()
    context.run_all_tests()


if __name__ == '__main__':
    main()
