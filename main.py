import sys
from clothes.clothes import Clothes
from ui.mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets
from stock.stock_management import Stock_Management
from overview.overview import Overview
from admin.login.admin_login import Login_Admin
from admin.cars.admin_car import Admin_cars
from admin.stock.admin_stock import Admin_Stock
from cars.cars import Cars_Employee
from admin.benutzerverwaltung.benutzer_verwaltung import Benutzer_Verwaltung
from admin.einstellungen.ui_einstellungen import Ui_Einstellungen
from admin.pdf_bestellung.pdf_bestellung import Pdf_Bestellung
from admin.mpg.mpg_geraete import Mpg_Geraete
from mpg.mpg_user import Mpg_User
from admin.employees.employees import Employees
from admin.mission.missions import Missions_Proof
from fill_table import Fill_Table

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Rettungsdienst Verwaltung")
        self.fill_table = Fill_Table(self.ui)
        self.clothes = Clothes(self.ui, self.fill_table)
        self.stock = Stock_Management(self.ui, self.fill_table)
        self.overview = Overview(self.ui)
        self.admin_login = Login_Admin(self.ui)
        self.admin_cars = Admin_cars(self.ui)
        self.admin_stock = Admin_Stock(self.ui)
        self.cars = Cars_Employee(self.ui)
        self.einstellungen = Ui_Einstellungen(self.ui, self)
        self.pdf = Pdf_Bestellung(self.ui)
        self.benutzer_verwaltung = Benutzer_Verwaltung(self.ui)
        self.mpg_geraete = Mpg_Geraete(self.ui)
        self.mpg_user = Mpg_User(self.ui)
        self.mitarbeiter = Employees(self.ui)
        self.mission_proof = Missions_Proof(self.ui)

window = MainWindow()
window.show()
sys.exit(app.exec_())
