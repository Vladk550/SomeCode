class Logger(object):

    reserved_names = ['call_method_message', 'send_arguments_message', 'returned_result_message', 'log_decor',
                      'set_arguments_message', 'set_method_message', 'set_result_message']

    def __init__(self):
        self.log = []
        self.call_method_message = 'Method {} was called '
        self.sent_arguments_message = 'with arguments {} '
        self.returned_result_message = '{} as a result was returned'

    def set_method_message(self, message):
        self.call_method_message = message

    def set_arguments_message(self, message):
        self.sent_arguments_message = message

    def set_result_message(self, message):
        self.returned_result_message = message

    def log_decor(self, func):
        def wrapper(*args, **kwargs):
            res = None
            try:
                res = func(*args, **kwargs)
                return res
            except Exception as ex:
                res = repr(ex)
                raise
            finally:
                self.log.append(self.call_method_message.format(func.__name__) + self.sent_arguments_message.format(args) +
                                self.returned_result_message.format(res))
        return wrapper

    def __getattribute__(self, attr):
        obj = object.__getattribute__(self, attr)
        if attr not in Logger.reserved_names and callable(obj):
            return self.log_decor(obj)
        else:
            return obj

    def __str__(self):
        return '\n'.join(self.log)


class SomeClass(Logger):

    def __init__(self):
        super(SomeClass, self).__init__()
        self.set_arguments_message("with  arguments {} ")

    def speak(self, st):
        return "I'm speaking. {}".format(st)

    def scream(self, st):
        return "I'm screaming. {}".format(st)

    def voice_volume(self, volume):
        return volume


if __name__ == "__main__":
    bl = SomeClass()
    print bl.speak("I'm Anon")
    print bl.scream("Kyyyyyy")
    print bl.log
