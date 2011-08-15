class Obstacle():
    def __init__(self, name, category,  hindrance):
        self._category = category
        self._name = name
        self._hindrance = hindrance
    def getName(self):
        return self._name
    def getCategory(self):
        return self._category
    def getHindrance(self):
        return self._hindrance
    def setName(self, name):
        self._name = name
    def setCategory(self, category):
        self._category = category
    def setHindrance(self, hindrance):
        self._hindrance = hindrance

if __name__ == "__main__":
    o1 = Obstacle("natural", "tree", 2)
    print(o1)
