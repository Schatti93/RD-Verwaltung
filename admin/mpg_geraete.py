from admin.mpg_data import Mpg_Data
class Mpg_Geraete():
    def __init__(self, ui):
        self.ui = ui
        self.data = Mpg_Data()

    def neues_geraet_anlegen(self):
        geraet = self.ui.neues_geraet_geraet.text()
        geraetenummer = self.ui.neues_geraet_geraetenummer.text()
        inventarnummer = self.ui.neues_geraet_inventarnummer.text
        ce = self.ui.neues_geraet_ce.text()
        bemerkung = self.ui.neues_geraet_bemerkung.text()
        pruefdatum = self.ui.neues_geraet_pruefdatum.text()
        prueffrist = self.ui.neues_geraet_prueffrist.text()
        standort = self.ui.neues_geraet_standort_combo.currentText()
        self.data.neues_geraet_speichern(geraet, geraetenummer, inventarnummer, ce,
                                         bemerkung, pruefdatum, prueffrist, standort)
        ##tabelle aktualisieren
