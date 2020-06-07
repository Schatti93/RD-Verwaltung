from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from uebersicht.uebersicht import Uebersicht
from lager.data_lagerverwaltung import Database_Lagerverwaltung
from admin.lager.fehlendes_material import Fehlendes_Material
from admin.lager.material_einpfl import Material_einpflegen
from admin.lager.bearbeiten import Bearbeiten
from admin.lager.neu_loeschen import Neu_Loeschen
from admin.lager.sets import Sets

class Admin_Lager():
    def __init__(self, ui):
        self.ui = ui
        self.lager = Database_Lagerverwaltung()

        ### aufruf bei start des programms
        self.eingabefelder_int()

        self.fehlendes_Material = Fehlendes_Material(self.ui)
        self.fehlendes_Material.fehlendes_material()

        self.einpflegen = Material_einpflegen(self.ui)
        self.einpflegen.combobox_bestellung_einpflegen()

        self.bearbeiten = Bearbeiten(self.ui)
        self.bearbeiten.alle_produkte_anzeigen_table()

        self.neu_loeschen = Neu_Loeschen(self.ui)

        self.sets = Sets(self.ui)
        self.sets.edit_set_combo_fill()

    def eingabefelder_int(self):
        validator = QIntValidator(0, 999999999)
        self.ui.admin_material_speichern_anzahl.setValidator(validator)
        self.ui.admin_new_prod_bes.setValidator(validator)
        self.ui.admin_new_prod_min.setValidator(validator)
        self.ui.admin_new_prod_max.setValidator(validator)
        self.ui.admin_new_prod_inhalt_menge.setValidator(validator)
