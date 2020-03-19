import sys
from kleidung.Kleidung import Kleidung
from ui.mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets
from lager.lagerverwaltung import Lagerverwaltung
from uebersicht.uebersicht import Uebersicht
from admin.login_admin import Login_Admin
from admin.fahrzeug_admin import Admin_Fahrzeug
from fahrzeuge.fahrzeuge_uebersicht import Fahrzeuge_Uebersicht
from admin.admin_lager import Admin_Lager
from fahrzeuge.fahrzeug import Fahrzeug_Mitarbeiter
from uebersicht.grid_fahrzeuge import Grid_Fahrzeuge
from admin.ui_einstellungen_lager import Ui_Einstellungen_Lager
from admin.pdf_bestellung import Pdf_Bestellung

app = QtWidgets.QApplication(sys.argv)
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Rettungsdienst Verwaltung")
        self.grid_fahrzeug = Grid_Fahrzeuge(self.ui).grid_fahrzeug_anzeige() # erstellt das grid für die uebersicht anzeige der Fahrzeuge

        self.kleidung = Kleidung(self.ui)
        self.Lager = Lagerverwaltung(self.ui)
        self.uebersicht = Uebersicht(self.ui)
        self.admin_login = Login_Admin(self.ui)
        self.admin_fahrzeug = Admin_Fahrzeug(self.ui)
        self.fahrzeuge_uebersicht = Fahrzeuge_Uebersicht(self.ui)
        self.fahrzeuge_uebersicht.anzeige()
        self.admin_lager = Admin_Lager(self.ui)
        self.ui.fahrzeug = Fahrzeug_Mitarbeiter(self.ui)
        self.einstellungen = Ui_Einstellungen_Lager(self.ui)
        self.pdf = Pdf_Bestellung(self.ui)


window = MainWindow()

window.show()
sys.exit(app.exec_())
