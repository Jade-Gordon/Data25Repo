# lets create a location class
class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Location = (longitude={self.longitude}, latitude={self.latitude})"
    # def __str__(self):
    #     return f"({self.latitude}, {self.longitude})"

# Birmingham academy location
bham_academy = Location(52.488647, -1.887249)
print(bham_academy)


