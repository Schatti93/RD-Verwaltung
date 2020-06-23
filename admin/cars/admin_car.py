from admin.cars.admin_car_data import Admin_Car_Data
from cars.uebersicht_fahrzeuge_anzeige import Fahrzeug_Anzeige

class Admin_cars():
    def __init__(self, ui):
        self.ui = ui
        self.data = Admin_Car_Data()
        self.ui.fahrzeug_admin_save_btn.clicked.connect(self.get_car_data_from_ui)

    def save_car(self, radio_identification, license_plate, town, tuev):
        self.data.save_car(radio_identification, license_plate, town, "Im Dienst", tuev, "")
        car_list = self.data.get_active_cars()
        Fahrzeug_Anzeige(self.ui).anzeige(radio_identification, license_plate,
                                          town, "Im Dienst", "", len(car_list))
        self.ui.admin_car_error_label.setText(
            "<html><head/><body><p><span style=\" color:#00FF00;\">Eingabe Gespeichert</span></p></body></html>")

    def get_car_data_from_ui(self):
        radio_identification = self.ui.admin_car_radio_identification.text()
        license_plate = self.ui.admin_car_license_plate.text()
        town = self.ui.admin_car_town.text()
        tuev = self.ui.admin_car_tuev.text()
        self.save_car(radio_identification, license_plate, town, tuev)

