from constants import ADMIN_USERNAME, UNKNOWN_COMMAND


def access_control(func):
    def wrapper(self, *args, **kwargs):
        if self.username == ADMIN_USERNAME:
            result = func(self, *args, **kwargs)
            return result
        else:
            print(UNKNOWN_COMMAND)
    return wrapper
