import sys
from kleidung.Kleidung import Kleidung
from ui.mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets
from lager.lagerverwaltung import Lagerverwaltung
from uebersicht.uebersicht import Uebersicht
from admin.login.login_admin import Login_Admin
from admin.fahrzeuge.fahrzeug_admin import Admin_Fahrzeug
from admin.lager.admin_lager import Admin_Lager
from fahrzeuge.fahrzeug import Fahrzeug_Mitarbeiter
from admin.benutzerverwaltung.benutzer_verwaltung import Benutzer_Verwaltung
from admin.einstellungen.ui_einstellungen import Ui_Einstellungen
from admin.pdf_bestellung.pdf_bestellung import Pdf_Bestellung
from admin.mpg.mpg_geraete import Mpg_Geraete
from mpg.mpg_user import Mpg_User
from admin.mitarbeiter.mitarbeiter import Mitarbeiter
from admin.mission.missions import Missions_Proof

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Rettungsdienst Verwaltung")
        self.kleidung = Kleidung(self.ui)
        self.Lager = Lagerverwaltung(self.ui)
        self.uebersicht = Uebersicht(self.ui)
        self.admin_login = Login_Admin(self.ui)
        self.admin_fahrzeug = Admin_Fahrzeug(self.ui)
        self.admin_lager = Admin_Lager(self.ui)
        self.fahrzeug = Fahrzeug_Mitarbeiter(self.ui)
        self.einstellungen = Ui_Einstellungen(self.ui, self)
        self.pdf = Pdf_Bestellung(self.ui)
        self.benutzer_verwaltung = Benutzer_Verwaltung(self.ui)
        self.mpg_geraete = Mpg_Geraete(self.ui)
        self.mpg_user = Mpg_User(self.ui)
        self.mitarbeiter = Mitarbeiter(self.ui)
        self.mission_proof = Missions_Proof(self.ui)

window = MainWindow()
window.show()
sys.exit(app.exec_())
