import ruamel.yaml as yaml

class FileHandler:
    """
    The filehandler is responsible for writing and reading files to/from
    the file system.
    """

    def read_file(self, path):
        with open(path) as file:
            try:
                information_yaml = []
                information_list = yaml.safe_load(file)
                try:
                    for device, dev in information_list.items():
                        information_yaml.append(dev)
                    return information_yaml
                except ValueError:
                    print("The Informations are not entered correctly or not in the right Format")
                print(yaml.safe_load(file))
            except yaml.YAMLError as exc:
                print(exc)
            finally:
                file.close()
