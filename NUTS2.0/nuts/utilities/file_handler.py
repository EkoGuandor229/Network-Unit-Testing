import datetime
import logging
import os
import nuts

import ruamel.yaml as yaml


class FileHandler:
    """
    The filehandler is responsible for writing and reading files to/from
    the file system.
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.results_file = os.path.join(nuts.basedir, "resources/inventory/Testresults/results.txt")
        self.path = "resources/inventory/TestResults/"
        self.file = "results.txt"

    def read_file(self, path):
        with open(path) as file:
            try:
                information_yaml = []
                information_list = yaml.safe_load(file)
                try:
                    for device, dev in information_list.items():
                        information_yaml.append(dev)
                    return information_yaml
                except ValueError as ex:
                    print("The Informations are not entered correctly or not in the right Format")
                    self.logger.exception(ex)
                print(yaml.safe_load(file))
            except yaml.YAMLError as exc:
                print(exc)
                self.logger.exception(ex)
            finally:
                file.close()
                self.logger.info('File at Path "{}" successfully read'.format(path))

    def write_new_run(self):
        time = datetime.datetime.now()
        with open(self.results_file, 'a') as fp:
            fp.write("New Test Run on " + str(time) + ":")
            fp.write("\n")

    def write_passed_results(self, results):
        with open(self.results_file, 'a') as fp:
            fp.write("  Passed Tests: \n")
            for result in results:
                fp.write("    Test: " + result.get_test_name() + " has PASSED")
                fp.write("\n")

    def write_failed_results(self, results):
        with open(self.results_file, 'a') as fp:
            fp.write("\n  Failed Tests: \n")
            for result in results:
                fp.write("    Test: " + result.get_test_name() + " has FAILED \n")
                fp.write("      Expected: " + str(result.get_expected_value()) + "\n")
                fp.write("      Actual:   " + str(result.get_result()) + "\n\n")
            fp.write("End of Test Run \n")
            fp.write("\n")

    def read_config(self, param):
        path = os.path.join(nuts.basedir, "config.yaml")
        with open(path) as file:
            config_map = yaml.load(file, Loader=yaml.ruamel.yaml.Loader)
        return config_map[param]
