from admin.ui_einstellungen_data import Ui_Einstellungen_Data
class Ui_Einstellungen():
    def __init__(self, ui):
        self.ui = ui
        self.data = Ui_Einstellungen_Data()
        self.einstellungen_setzen()
        self.ui.einstellungen_speichern.clicked.connect(self.einstellungen_speichern)
        self.einstellungen_umsetzen()

    def einstellungen_setzen(self):
        parameter = self.data.einstellungen_abfragen()
        if len(parameter) == 0:
            self.ui.check_lager.setChecked(True)
            self.ui.check_uebersicht.setChecked(True)
            self.ui.check_fahrzeuge.setChecked(True)
            self.ui.check_dienstbekleidung.setChecked(True)
        else:
            for i in range(0, len(parameter)):
                if parameter[i][2] == "lager":
                    self.ui.check_lager.setChecked(int(parameter[i][1]))
                if parameter[i][2] == "uebersicht":
                    self.ui.check_uebersicht.setChecked(int(parameter[i][1]))
                if parameter[i][2] == "fahrzeuge":
                    self.ui.check_fahrzeuge.setChecked(int(parameter[i][1]))
                if parameter[i][2] == "dienstbekleidung":
                    self.ui.check_dienstbekleidung.setChecked(int(parameter[i][1]))

    def einstellungen_speichern(self):
        self.data.einstellungen_speichern(self.ui.check_dienstbekleidung.isChecked(), "dienstbekleidung")
        self.data.einstellungen_speichern(self.ui.check_fahrzeuge.isChecked(), "fahrzeuge")
        self.data.einstellungen_speichern(self.ui.check_uebersicht.isChecked(), "uebersicht")
        self.data.einstellungen_speichern(self.ui.check_lager.isChecked(), "lager")

    def einstellungen_umsetzen(self):
        liste = self.data.einstellungen_abfragen()
        for i in range(0, len(liste)):
            print(liste[i][1])
            if int(liste[i][1]) == 0:
                if liste[i][2] == "dienstbekleidung":
                    self.ui.tabWidget.removeTab(3)
                if liste[i][2] == "fahrzeuge":
                    self.ui.tabWidget.removeTab(2)
                if liste[i][2] == "lager":
                    self.ui.tabWidget.removeTab(1)
                if liste[i][2] == "uebersicht":
                    self.ui.tabWidget.removeTab(0)










