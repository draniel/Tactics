import obstacle

class Terrain():
    def __init__(self, altitude, slip, slog, obstacle):
        self._slog = slog
        self._slip = slip
        self._altitude = altitude
        self._obstacle = obstacle
    def getSlog(self):
        return self._slog
    def getSlip(self):
        return self._slip
    def getAltitude(self):
        return self._altitude
    def getObstacle(self):
        return self._obstacle
    def getDescription(self):
        return "Slog: {0}, Slip: {1}, Obstacle: {2}({3}).".format(self.getSlog(), self.getSlip(), self.getObstacle().getName(), self.getObstacle().getHindrance())
    def setSlog(self, slog):
        self._slog = slog
    def setSlip(self, slip):
        self._slip = slip
    def setAltitude(self, altitude):
        self._altitude = altitude
    def setObstacle(self, obstacle):
        self._obstacle = obstacle


if __name__ == "__main__":
    o1 = obstacle.Obstacle("natural", "tree", 2)
    t1 = Terrain(1, 2, 3, o1)
    print(t1.getDescription())
