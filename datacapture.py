#!/usr/bin/env python3

class CapureData:
  def __init__(self):
    self.data = []

  def add(self, num):
    self.data.append(num)

  def build_stat(self):
    return self.Stats(self.data)


  class Stats():
    def __init__(self, data):
        self.data = data
    def less(self, num):
        return sum(map(lambda i: i < num, self.data))

    def greater(self, num):
        return sum(map(lambda i: i > num, self.data))

    def between(self, ini, end):
        return sum(map(lambda i: i < end and i > ini, self.data))


d = CapureData()
d.add(1)
d.add(3)
d.add(6)
d.add(3)
d.add(2)
d.add(5)
d.add(3)

c = d.build_stat()
print(c.less(4))
print(c.greater(4))
print(c.between(2, 4))
