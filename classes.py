class Planet:
    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f"{self.name} is orbiting in the {self.system}"


hoth = Planet("Hoth", 200000, 5.5, "Hoth System")

print(f"This is the planet name: {hoth.name}")
print(f"This is the radius: {hoth.radius}")
print(f"this is the gravity: {hoth.gravity}")

print(hoth.orbit())

jura = Planet("Jura", 150000, 9.0, "Jura System")

print(f"Planet Name: {jura.name}")
print(f"Radius: {jura.radius}")
print(f"Gravity: {jura.gravity}")
print(f"System: {jura.system}")
