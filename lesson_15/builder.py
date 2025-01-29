class Car:
    def __init__(self, model="", tires="", engine="", color=""):
        self.model = model
        self.tires = tires
        self.engine = engine
        self.color = color

    def __str__(self):
        # "Red Sports Car with V8 engine and Performance tires"
        return f"{self.color} {self.model} with {self.engine} engine and {self.tires} tires"


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_model(self, model) -> "CarBuilder":
        self.car.model = model
        return self

    def set_tires(self, tires) -> "CarBuilder":
        self.car.tires = tires
        return self

    def set_engine(self, engine) -> "CarBuilder":
        self.car.engine = engine
        return self

    def set_color(self, color) -> "CarBuilder":
        self.car.color = color
        return self

    def get_car(self) -> Car:
        car = self.car
        self.car = Car()
        return car


class Director:

    def construct_sports_car(self, builder: CarBuilder) -> Car:
        return (
            builder.set_model("Sports Car")
            .set_tires("Performance")
            .set_engine("V8")
            .set_color("Red")
            .get_car()
        )
    
    def construct_sedan(self, builder: CarBuilder) -> Car:
        return (
            builder.set_model("Sedan")
            .set_tires("Regular")
            .set_engine("V6")
            .set_color("Blue")
            .get_car()
        )


director = Director()
car_builder = CarBuilder()
sports_car = director.construct_sports_car(car_builder)
print(sports_car)

sedan = director.construct_sedan(car_builder)
print(sedan)