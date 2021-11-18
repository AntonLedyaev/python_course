import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self,x):
        self.log(x)
        super().append(x)


x = LoggableList()

x.append('biba')
