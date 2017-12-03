class Driver(object):
    """ служебный класс, для инициализируется драйвера.
	    Этот класс наследуется классами, использующими драйвер
	"""
    def __init__(self, driver):
        self.driver = driver
