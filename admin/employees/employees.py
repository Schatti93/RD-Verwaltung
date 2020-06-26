from admin.employees.employees_data import Employee_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from admin.mpg.update_mpg import Update_Mpg
from admin.mpg.einweisungen import Einweisungen
from admin.mpg.einweisungen import Einweisungen

class Employees():
    def __init__(self, ui):
        self.ui = ui
        self.data = Employee_Data()
        self.mitarbeiter_tabelle_laden()
        self.ma_loeschen_combo_fuellen()
        self.ui.ma_neu_speichern_btn.clicked.connect(self.neuer_mitarbeiter)
        self.ui.ma_loeschen_btn.clicked.connect(self.ma_loeschen)
        self.update_mpg = Update_Mpg(self.ui)

    def mitarbeiter_tabelle_laden(self):
        self.ui.ma_tabelle.setRowCount(0)
        liste_der_eintraege = self.data.alle_ma_abfragen()
        for element in range(0, len(liste_der_eintraege)):
            rows = self.ui.ma_tabelle.rowCount()
            self.ui.ma_tabelle.insertRow(rows)
            for eintrag in range(0, len(liste_der_eintraege[element])):
                einzusetzen = QtWidgets.QTableWidgetItem(str(liste_der_eintraege[element][eintrag]))
                einzusetzen.setTextAlignment(Qt.AlignCenter)
                self.ui.ma_tabelle.setItem(rows, eintrag, QtWidgets.QTableWidgetItem(
                    einzusetzen))

    def ma_loeschen_combo_fuellen(self):
        self.ui.ma_loeschen_combo.clear()
        liste_der_daten = self.data.alle_ma_abfragen()
        combo_eintraege = ["---"]
        for element in range(0, len(liste_der_daten)):
            eintrag = str(liste_der_daten[element][1]) + ", " + str(liste_der_daten[element][2]) \
            + " / " + str(liste_der_daten[element][0])
            combo_eintraege.append(eintrag)
        self.ui.ma_loeschen_combo.addItems(combo_eintraege)

    def neuer_mitarbeiter(self):
        vorname = self.ui.ma_neu_vorname_text.text()
        nachname = self.ui.ma_neu_nachname_text.text()
        status = self.ui.ma_neu_checkbox.isChecked()
        if status == True:
            status = "Mitarbeiter"
        else:
            status = "Extern"
        self.data.neuer_mitarbeiter_speichern(vorname, nachname, status)
        self.ui.ma_neu_vorname_text.setText("")
        self.ui.ma_neu_nachname_text.setText("")
        self.ui.ma_neu_checkbox.setChecked(1)
        self.mitarbeiter_tabelle_laden()
        self.ma_loeschen_combo_fuellen()
        Einweisungen(self.ui).combos_ma_fuellen()
        Einweisungen(self.ui).tabellen_filter_ma_combo_fuellen()

    def ma_loeschen(self):
        if self.ui.ma_loeschen_combo.currentText() == "---":
            pass
        else:
            ma_id = self.ui.ma_loeschen_combo.currentText().split(" / ")[1]
            self.data.ma_loeschen(ma_id)
            self.mitarbeiter_tabelle_laden()
            name = self.ui.ma_loeschen_combo.currentText().split(" / ")[0]
            name = name.split(", ")
            self.data.delete_employee_data(name[1] + ", " + name[0])
            self.ma_loeschen_combo_fuellen()
            Einweisungen(self.ui).combos_ma_fuellen()
            Einweisungen(self.ui).tabellen_filter_ma_combo_fuellen()
            self.update_mpg.update_tabellen_und_combos()
            Einweisungen(self.ui).fehlende_einweisung_fuellen()