from overview.uebersicht_fahrzeuge_anzeige import Fahrzeug_Anzeige
from cars.cars_data import Cars_Data

class Car_Overview():
    def __init__(self, ui):
        self.ui = ui
        self.data = Cars_Data()

    def show_car(self):
        cars = self.data.get_cars()
        car_object = {}
        counter = 0
        for i in range(0, len(cars)):
            radio_identification = cars[i][1]
            license_plate = cars[i][2]
            place = cars[i][3]
            status = cars[i][4]
            comment = cars[i][6]
            car_object[license_plate] = Fahrzeug_Anzeige(self.ui).anzeige(radio_identification
                                      , license_plate, place, status, comment, counter)
            counter += 1
        return car_object




