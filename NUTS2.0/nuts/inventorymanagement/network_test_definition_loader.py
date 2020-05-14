import logging
import os
import nuts

from nuts.utilities.file_handler import FileHandler
from nuts.inventorymanagement.network_test_definition import TestDefinition
from pathlib import Path

from nuts.utilities.progress_bar_handler import ProgressBarHandler


class TestDefinitionLoader:
    """
    The TestDefinitionLoader is a helper-class, that loads the definitions of
    the tests to be executed from a test-definition file in the .yaml format

    ...

    Attributes
    ----------
    logger
        Instance of the logger class
    test_definitions: dictionary
        The test definitions specify the tests that should be executed against
        a network system. They are loaded from one or multiple .yaml files
    file_handler
        Reference to the FileHandler-class that is responsible for reading and
        writing in the directory
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.progress_bar = ProgressBarHandler()
        self.test_definitions = {}
        self.file_handler = FileHandler()

    def create_test_definition_object(self):
        """
        Loads test definitions from the file system specified in the
        definition_location and instantiates NetworkTestDefinition classes
        """
        definition_location = (self.file_handler.read_config("test-definitions"))
        definition_files = os.path.join(nuts.basedir, definition_location)
        for filename in os.listdir(definition_files):
            test_definition_yaml = self.file_handler.read_file(
                definition_files + filename
            )
            self.progress_bar.initiate_progress_bar(
                len(test_definition_yaml), "Create test definition objects from " + filename
            )
            try:
                for test_definition in test_definition_yaml:
                    self.test_definitions[test_definition[0]] = TestDefinition(
                        test_definition[0],
                        test_definition[1],
                        test_definition[2],
                        test_definition[3],
                        test_definition[4],
                        test_definition[5]
                    )
                    self.logger.info('Testdefinitio Object "{}" created'.format(test_definition[0]))
                    self.progress_bar.update_progress_bar(1)
            except ValueError as ex:
                print("There are Values missing or in the wrong Format")
                self.logger.exception(ex)
            else:
                self.progress_bar.clear_progress_bar()
        return self.test_definitions

