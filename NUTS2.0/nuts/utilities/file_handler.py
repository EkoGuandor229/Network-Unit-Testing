import yaml


class FileHandler:
    """
    The filehandler is responsible for writing and reading files to/from
    the file system.
    """

    def read_file(self, path):
        try:
            with open(path) as file:
                information_yaml = []
                information_list = yaml.full_load(file)
                try:
                    for device, dev in information_list.items():
                        information_yaml.append(dev)
                    return information_yaml
                except ValueError:
                    print("The Informations are not entered correctly or not in the right Format")
        except IOError:
            print("File not found")
        finally:
            file.close()

