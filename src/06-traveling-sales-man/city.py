class Gene:
    def __init__(self):
        return

class City(Gene):
    Name = ''
    Lat = 0.0
    Lon = 0.0
    Height = 0.0

    def __init__(self, name: str, lat: float, lon: float, height: float = 0.0):
        self.Name = name
        self.Lat = lat
        self.Lon = lon
        self.Height = height

    