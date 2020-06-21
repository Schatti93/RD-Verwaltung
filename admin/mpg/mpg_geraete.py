from admin.mpg.geraete import Geraete
from admin.mpg.standorte import Standorte
from admin.mpg.einweisungen import Einweisungen
from admin.mpg.verwertet import Verwertet
from PyQt5.QtGui import QIntValidator

class Mpg_Geraete():
    def __init__(self, ui):
        self.ui = ui
        #geraete initialisieren
        self.geraete = Geraete(self.ui)
        self.geraete.standort_combo_fuellen()
        #standorte initialisieren
        self.standorte = Standorte(self.ui)
        self.standorte.standorte_tabelle_fuellen()
        self.standorte.standort_loeschen_combo_fuellen()
        #einweisungen initialisieren
        self.einweisungen = Einweisungen(self.ui)
        self.einweisungen.einweisung_geraete_combos_fuellen()
        self.einweisungen.einweisung_tabelle_fuellen()
        self.einweisungen.combos_ma_fuellen()
        self.einweisungen.tabellen_filter_ma_combo_fuellen()
        self.einweisungen.fehlende_einweisung_fuellen()
        #verwertet initialisieren
        self.verwertet = Verwertet(self.ui)
        self.verwertet.verwertet_tabelle_fuellen()
        self.verwertet.geraete_inventarnummer_combos_fuellen()

        self.only_int_fields()

    def only_int_fields(self):
        validator = QIntValidator(0, 999999999)
        self.ui.geraete_verwalten_prueffrist.setValidator(validator)







