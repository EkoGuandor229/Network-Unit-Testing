import logging

import ruamel.yaml as yaml

class FileHandler:
    """
    The filehandler is responsible for writing and reading files to/from
    the file system.
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)

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
