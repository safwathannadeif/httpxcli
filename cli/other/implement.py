from cli.other.abstract import Vehicle


class Car(Vehicle):
    def start_engine(self):
        print("Starting car engine...")

    def stop_engine(self):
        print("Stopping car engine...")

    def accelerate(self):
        print("Accelerating car...")

    def brake(self):
        print("Applying car brakes...")