class Jar:
    def __init__(self, capacity=12, cookies=0):
        self.capacity = capacity
        self.cookies = cookies

    def __str__(self):
        return f"{'🍪' * self.cookies}"


    def deposit(self, n):
        if (self.cookies + n) > self.capacity:
            raise ValueError
        self.cookies += n

    def withdraw(self, n):
        if (self.cookies - n) < 0:
            raise ValueError
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self.cookies
