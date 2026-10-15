#Written in Python IDLE 3.14.6
class mySet:
    def __init__(self):
        self.items = []

    def show(self):
        print("Items in set :", self.items)

    def add(self, item):
        if item not in self.items:
            self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)


class myBag:
    def __init__(self):
        self.items = []

    def show(self):
        print("Items in bag :", self.items)

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)


class myQueue:
    def __init__(self):
        self.items = []

    def show(self):
        print("Queue :", self.items)

    def add(self, item):
        self.items.append(item)

    def remove(self):
        if len(self.items) > 0:
            return self.items.pop(0)


# Test mySet
s = mySet()
s.add(10)
s.add(20)
s.add(10)
s.show()
s.remove(10)
s.show()

# Test myBag
b = myBag()
b.add(10)
b.add(10)
b.add(20)
b.show()
b.remove(10)
b.show()

# Test myQueue
q = myQueue()
q.add(10)
q.add(20)
q.add(30)
q.show()
q.remove()
q.show()
