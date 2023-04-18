

def add(*args):
    print(sum(args))

add(1, 2, 3, 4, 5)

class Car:
    def __init__(self, **kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        self.make = kw.get("make")
        self.make = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make = "Dodge", model = "Charger")

print(my_car.model)