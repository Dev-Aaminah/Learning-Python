class Human:
    name = "Anonymous"  # class attribute
    place = "Earth"
    def __init__(self, name, height, weight):
        self.name = name    # object attribute
        # object attribute > class attribute [precedence]
        self.height = height
        self.weight = weight

pakistani = Human("Aaminah", "5'4", "unknown")
print(pakistani.name, pakistani.height, pakistani.place, pakistani.weight)