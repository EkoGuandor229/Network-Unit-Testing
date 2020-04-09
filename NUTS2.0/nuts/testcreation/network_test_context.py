import nuts.testcreation.test_strategy_factory as factory


class TestContext:
    factory = factory
    tests = []
    tests.append(factory.NapalmPingTest("Ping", True))
    tests.append(factory.NetmikoPingTest("Ping", True))

    def run_all_tests(self):
        for test in self.tests:
            test.run_test()


def main():
    context = TestContext()
    context.run_all_tests()


if __name__ == '__main__':
    main()
