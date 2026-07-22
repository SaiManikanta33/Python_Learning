        # Composition
    #Composition means one object owns another object

class engine:
    def start(self):
        print("Engine Started")
class car:
    def __init__(self):
        self.engine = engine()
    def drive(self):
        self.engine.start()
        print("Car is moving")
Car = car()
Car.drive()

        # Here The car owns an engine