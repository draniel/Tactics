import terrain, obstacle

class Space():
    def __init__(self, terrain):
        self._terrain = terrain
    def getTerrain(self):
        return self._terrain
    def setTerrain(self, terrain):
        self._terrain = terrain

if __name__ == "__main__":
    tree = obstacle.Obstacle("tree", "natural", 2)
    ter1 = terrain.Terrain(25, 2, 3, tree)
    testSpace = Space(ter1)
    testSpaceTerrain = testSpace.getTerrain()
    print(testSpaceTerrain.getDescription())
