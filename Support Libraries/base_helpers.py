
from traceback import print_stack
from configparser import ConfigParser
from SupportLibraries.ui_helpers import UIHelpers


class BaseHelpers(UIHelpers):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def load_properties_file(self):
        
        config = None
        try:
            # noinspection PyBroadException
            config = ConfigParser()
            config.read('test.ini')

        except Exception as ex:
            self.log.error("Failed to load ini/properties file.", ex)
            print_stack()

        return config
