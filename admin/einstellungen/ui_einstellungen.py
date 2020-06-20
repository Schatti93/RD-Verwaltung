from admin.einstellungen.ui_einstellungen_data import Ui_Einstellungen_Data
from PyQt5.QtWidgets import QFileDialog
from update.update import Updater


class Ui_Einstellungen():
    def __init__(self, ui, mainwindow):
        self.ui = ui
        self.mainwindow = mainwindow
        self.data = Ui_Einstellungen_Data()
        self.einstellungen_setzen()
        self.einstellungen_umsetzen()
        self.speicherort_anzeigen()
        self.show_barcode_location()
        self.show_barcode_minimum()
        self.update = Updater(self.ui)
        self.update.delete_update_path()
        self.ui.einstellungen_speichern.clicked.connect(self.einstellungen_speichern)
        self.ui.pdf_speicheror_btn.clicked.connect(self.save_pdf_location)
        self.ui.barcode_location_btn.clicked.connect(self.save_barcode_location)
        self.ui.barcode_number_btn.clicked.connect(self.save_barcode_minimum)
        self.ui.admin_update.clicked.connect(self.update.version_check)

    def einstellungen_setzen(self):
        parameter = self.data.einstellungen_abfragen()
        if len(parameter) == 0:
            self.ui.check_lager.setChecked(True)
            self.ui.check_uebersicht.setChecked(True)
            self.ui.check_fahrzeuge.setChecked(True)
            self.ui.check_dienstbekleidung.setChecked(True)
        else:
            for i in range(0, len(parameter)):
                if parameter[i][2] == "stock":
                    self.ui.check_lager.setChecked(int(parameter[i][1]))
                if parameter[i][2] == "overview":
                    self.ui.check_uebersicht.setChecked(int(parameter[i][1]))
                if parameter[i][2] == "cars":
                    self.ui.check_fahrzeuge.setChecked(int(parameter[i][1]))
                if parameter[i][2] == "dienstbekleidung":
                    self.ui.check_dienstbekleidung.setChecked(int(parameter[i][1]))

    def einstellungen_speichern(self):
        self.data.einstellungen_speichern(self.ui.check_dienstbekleidung.isChecked(), "dienstbekleidung")
        self.data.einstellungen_speichern(self.ui.check_fahrzeuge.isChecked(), "cars")
        self.data.einstellungen_speichern(self.ui.check_uebersicht.isChecked(), "overview")
        self.data.einstellungen_speichern(self.ui.check_lager.isChecked(), "stock")

    def einstellungen_umsetzen(self):
        liste = self.data.einstellungen_abfragen()
        for i in range(0, len(liste)):

            if int(liste[i][1]) == 0:
                if liste[i][2] == "dienstbekleidung":
                    self.ui.tabWidget.removeTab(3)
                if liste[i][2] == "cars":
                    self.ui.tabWidget.removeTab(2)
                if liste[i][2] == "stock":
                    self.ui.tabWidget.removeTab(1)
                if liste[i][2] == "overview":
                    self.ui.tabWidget.removeTab(0)

    def save_pdf_location(self):
        speicherort = QFileDialog.getExistingDirectory(self.mainwindow, "Datei Öffnen", "/")
        if len(speicherort) > 0:
            id = self.data.speicherort_abfragen()[0][0]

            self.data.pdf_speicherort(speicherort, id)
            self.ui.pdf_speicherort_label.setText(speicherort)
            self.ui.pdf_speicherort_label.setStyleSheet(
                "color:#ffffff; font-size:9pt; border: 1px solid green; border-radius: 5px")

    def speicherort_anzeigen(self):
        speicherort = self.data.speicherort_abfragen()[0][1]
        self.ui.pdf_speicherort_label.setText(speicherort)
        self.ui.pdf_speicherort_label.setStyleSheet(
            "color:#ffffff; font-size:9pt; border: 1px solid green; border-radius: 5px")

    def save_barcode_location(self):
        location = QFileDialog.getExistingDirectory(self.mainwindow, "Datei Öffnen", "/")
        if len(location) > 0:
            id = self.data.get_barcode_location()[0][0]

            self.data.save_barcode_location(location, id)
            self.ui.barcode_location_label.setText(location)
            self.ui.barcode_location_label.setStyleSheet(
                "color:#ffffff; font-size:9pt; border: 1px solid green; border-radius: 5px")

    def show_barcode_location(self):
        location = self.data.get_barcode_location()[0][1]
        self.ui.barcode_location_label.setText(location)
        self.ui.barcode_location_label.setStyleSheet(
            "color:#ffffff; font-size:9pt; border: 1px solid green; border-radius: 5px")

    def save_barcode_minimum(self):
        number = self.ui.barcode_number_text.text()
        id = self.data.get_barcode_location()[0][0]
        self.data.save_barcode_minimum(id, number)

    def show_barcode_minimum(self):
        number = self.data.get_barcode_location()[0][2]
        self.ui.barcode_number_text.setText(str(number))
