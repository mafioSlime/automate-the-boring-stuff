class Planet:
    def __init__(self):
        self.name = "Hoth"
        self.radius = 2000000
        self.gravity = 5.5
        self.system = "Hoth System"

    def orbit(self):
        return f"{self.name} is orbiting in the {self.system}"


hoth = Planet()

print(f"This is the planet name: {hoth.name}")
print(f"This is the radius: {hoth.radius}")
print(f"this is the gravity: {hoth.gravity}")

print(hoth.orbit())
