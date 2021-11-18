class ExtendedStack(list):
    def sum(self):
        a, b = self.pop(), self.pop()
        self.append(a + b)

    def sub(self):
        a, b = self.pop(), self.pop()
        self.append(a - b)

    def mul(self):
        a, b = self.pop(), self.pop()
        self.append(a * b)

    def div(self):
        a, b = self.pop(), self.pop()
        self.append(a // b)




