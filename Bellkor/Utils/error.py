class ModelValidationException(Exception):
    """Raised if the Model has not been initialised correctly"""

    def __init__(self, msg):
        """Initialise the Input Validation Exception

        :param msg: message

        """
        self.msg = msg
        super(ModelValidationException, self).__init__(msg)


class ModelIterationException(Exception):
    """Raised if the Model has not enough amount of Iterations"""

    def __init__(self, msg):
        """Initialise the Input Validation Exception

        :param msg: message

        """
        self.msg = msg
        super(ModelIterationException, self).__init__(msg)


class ModelRunException(Exception):
    """Raised if the Model has not enough amount of Iterations"""

    def __init__(self, msg):
        """Initialise the Input Validation Exception

        :param msg: message

        """
        self.msg = msg
        super(ModelRunException, self).__init__(msg)
