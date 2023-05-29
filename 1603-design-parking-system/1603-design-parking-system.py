class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slots = {'big': big, 'medium': medium, 'small': small}

    def addCar(self, carType: int) -> bool:
        car_sizes = {1: 'big', 2: 'medium', 3: 'small'}
        if self.slots[car_sizes[carType]] > 0:
            self.slots[car_sizes[carType]] -= 1
            return True
        else:
            return False
