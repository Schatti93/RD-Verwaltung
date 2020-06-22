from admin.benutzerverwaltung.benutzer_data import Benutzer_Data
import hashlib
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class Benutzer_Verwaltung():
    def __init__(self, ui):
        self.ui = ui
        self.data = Benutzer_Data()
        self.combo_admins_fuellen()
        self.tabelle_alle_admins_fuellen()
        self.ui.neuer_admin_speichern.clicked.connect(self.neuer_benutzer)
        self.ui.pw_aendern_speichern.clicked.connect(self.benuter_passwort_aendern)
        self.ui.admin_loeschen_speichern.clicked.connect(self.benutzer_loeschen)

    def benuter_passwort_aendern(self):
        benutzer = self.data.eingeloggter_benutzer_abfragen()[0][1]
        passwort = self.ui.pw_aendern_altes_pw.text()
        passwort_hash = hashlib.sha512(passwort.encode('utf-8')).hexdigest()
        benutzer_daten = self.data.benutzerdaten_abfragen(benutzer)
        neues_passwort = self.ui.pw_aendern_neues_pw.text()
        neues_passwort_vergleich = self.ui.pw_aendern_neues_pw_wied.text()

        if passwort_hash == benutzer_daten[0][2]:
            if neues_passwort == neues_passwort_vergleich:
                passwort_hash = hashlib.sha512(neues_passwort.encode('utf-8')).hexdigest()
                self.data.passwort_update(benutzer, passwort_hash)
                self.ui.pw_aendern_altes_pw.setText("")
                self.ui.pw_aendern_neues_pw.setText("")
                self.ui.pw_aendern_neues_pw_wied.setText("")
                self.ui.pw_aendern_label.setText("")
                self.ui.pw_aendern_label.setStyleSheet("")
                return True
            else:
                self.ui.pw_aendern_label.setText("Neue Passwörter stimmen nicht überein")
                self.ui.pw_aendern_label.setStyleSheet(
                    "color:#ffffff; font-size:9pt; border: 1px solid red; border-radius: 5px")
                return False
        else:
            self.ui.pw_aendern_label.setText("Altes Passwort nicht korrekt.")
            self.ui.pw_aendern_label.setStyleSheet(
                "color:#ffffff; font-size:9pt; border: 1px solid red; border-radius: 5px")
            return False

    def neuer_benutzer(self):
        benutzer = self.ui.neuer_admin_name.text()
        passwort = self.ui.neuer_admin_pw.text()
        passwort_vergleich = self.ui.neuer_admin_pw_wied.text()
        count = 0
        alle_benutzer = self.data.alle_benutzer_abfragen()
        gespeichert = False
        for i in range(0, len(alle_benutzer)):

            if alle_benutzer[i][1] == benutzer:
                count += 1

        if count == 0:
            if passwort == passwort_vergleich:
                passwort_hash = hashlib.sha512(passwort.encode('utf-8')).hexdigest()
                self.data.neuer_benutzer(benutzer, passwort_hash)
                gespeichert = True
            else:
                self.ui.neuer_admin_label.setText("Passwörter stimmen nicht überein")
                self.ui.neuer_admin_label.setStyleSheet(
                    "color:#ffffff; font-size:9pt; border: 1px solid red; border-radius: 5px")
                return False
        else:
            self.ui.neuer_admin_label.setText("Benutzer schon vorhanden")
            self.ui.neuer_admin_label.setStyleSheet(
                "color:#ffffff; font-size:9pt; border: 1px solid red; border-radius: 5px")
            return False
        if gespeichert:
            self.ui.neuer_admin_label.setStyleSheet("")
            self.ui.neuer_admin_label.setText("")
            self.tabelle_alle_admins_fuellen()
            self.combo_admins_fuellen()
            self.ui.neuer_admin_name.setText("")
            self.ui.neuer_admin_pw.setText("")
            self.ui.neuer_admin_pw_wied.setText("")
            return True

    def benutzer_loeschen(self):
        benutzer = self.ui.admin_loeschen_combo.currentText()
        eingeloggter_admin = self.data.eingeloggter_benutzer_abfragen()[0][1]
        passwort = self.ui.admin_loeschen_pw.text()
        passwort_hash = hashlib.sha512(passwort.encode('utf-8')).hexdigest()
        benutzer_daten = self.data.benutzerdaten_abfragen(eingeloggter_admin)
        gespeichert = False
        if passwort_hash == benutzer_daten[0][2]:
            self.data.benutzer_loeschen(benutzer)
            gespeichert = True
        else:
            self.ui.admin_loeschen_label.setText("passwort nicht korrekt")
            self.ui.admin_loeschen_label.setStyleSheet(
                "color:#ffffff; font-size:9pt; border: 1px solid red; border-radius: 5px")
            return False
        if gespeichert:
            self.ui.admin_loeschen_label.setText("")
            self.ui.admin_loeschen_label.setStyleSheet("")
            self.combo_admins_fuellen()
            self.tabelle_alle_admins_fuellen()
            self.ui.admin_loeschen_pw.setText("")
            return True

    def combo_admins_fuellen(self):
        self.ui.admin_loeschen_combo.clear()
        alle_admins = self.data.alle_benutzer_abfragen()
        liste_der_admins = ["---"]
        for i in range(0, len(alle_admins)):
            liste_der_admins.append(alle_admins[i][1])
        self.ui.admin_loeschen_combo.addItems(liste_der_admins)

    def tabelle_alle_admins_fuellen(self):
        self.ui.tabelle_alle_admins.setRowCount(0)
        alle_admins = self.data.alle_benutzer_abfragen()
        for i in range(0, len(alle_admins)):
            row = self.ui.tabelle_alle_admins.rowCount()
            self.ui.tabelle_alle_admins.insertRow(row)
            benutzer = QtWidgets.QTableWidgetItem(alle_admins[i][1])
            benutzer.setTextAlignment(Qt.AlignCenter)
            self.ui.tabelle_alle_admins.setItem(row, 0, QtWidgets.QTableWidgetItem(benutzer))
            self.ui.tabelle_alle_admins.resizeColumnsToContents()
            self.ui.tabelle_alle_admins.horizontalHeader().setSectionResizeMode(1)
