#!/usr/bin/env python3

def validate(input):
    if (not isinstance(input, int)):
        raise TypeError('value type is not valid')
    elif (input > 1000):
        raise ValueError('value is more than threshold')
    elif (input < 0):
        raise ValueError('value is negative')
    return input

class CapureData:
  def __init__(self):
    self.data = []

  def add(self, num):
    val = validate(num);
    self.data.append(val)

  def build_stat(self):
    return self.Stats(self.data)

  def get(self):
    return self.data

  class Stats():
    def __init__(self, data):
        self.data = data

    def less(self, num):
        val = validate(num)
        res = sum(map(lambda i: i < val, self.data))

        if (res == 0):
            raise ValueError('no values found')
        return res

    def greater(self, num):
        val = validate(num)
        res = sum(map(lambda i: i > val, self.data))
        if (res == 0):
            raise ValueError('no values found')
        return res

    def between(self, ini, end):
        start = validate(ini)
        finish = validate(end)
        if (finish < start):
            raise ValueError('init value cant be more than finish')
        res = sum(map(lambda i: i < finish and i > start, self.data))
        if (res == 0):
            raise ValueError('no values found')
        return res



