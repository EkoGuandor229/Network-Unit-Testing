class TestController:
    reporter = 0
    testRunner = 0
    evaluator = 0
    testBuilder = 0

    def logic(self):
        print("It just works " + str(self.reporter))


def main():
    controller = TestController()
    controller.logic()


if __name__ == '__main__':
    main()
