class AbstractException(Exception):
    def __init__(self, *args, **kwargs):
        super(Exception, self).__init__(*args, **kwargs)
        self.message = kwargs.get('message', None)
        self.name = kwargs.get('name', None)

    def __str__(self):
        return "%s: %s" % (self.name, self.message)


class LoginUnsuccessfulError(AbstractException):
    def __init__(self, *args, **kwargs):
        super(LoginUnsuccessfulError, self).__init__(*args, **kwargs)
        self.message = "Login not successful, check your username or connection"
        self.name = "LoginUnsuccessfulError"


class LoginRequiredError(AbstractException):
    def __init__(self, *args, **kwargs):
        super(LoginRequiredError, self).__init__(*args, **kwargs)
        self.message = "Download not sucessful, login is required"
        self.name = "LoginRequiredError"


class DateRequiredError(AbstractException):
    def __init__(self, *args, **kwargs):
        super(DateRequiredError, self).__init__(*args, **kwargs)
        self.message = "The date maybe complete"
        self.name = "DateRequiredError"


class TimeRequiredError(AbstractException):
    def __init__(self, *args, **kwargs):
        super(TimeRequiredError, self).__init__(*args, **kwargs)
        self.message = "The hourn and minute maybe complete"
        self.name = "TimeRequiredError"


