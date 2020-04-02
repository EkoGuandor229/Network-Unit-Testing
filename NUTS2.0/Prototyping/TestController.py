from Prototyping.TestBuilder import TestBuilder


class TestController:
    reporter = 0
    testRunner = 0
    evaluator = 0
    testBuilder = TestBuilder()

    def logic(self):
        print("It just works " + str(self.reporter))


def main():
    controller = TestController()


if __name__ == '__main__':
    main()
