from overview.uebersicht_fahrzeuge_anzeige import Fahrzeug_Anzeige
from fahrzeuge.fahrzeug_data import Data_Fahrzeug

class Fahrzeuge_Uebersicht():
    def __init__(self, ui):
        self.ui = ui
        self.data = Data_Fahrzeug()

    def anzeige(self):
        liste = self.data.fahrzeug_daten_holen()
        fahrzeug_objekte = {}
        counter = 0
        for i in range(0, len(liste)):
            kennung = liste[i][1]
            kennzeichen = liste[i][2]
            ort = liste[i][3]
            status = liste[i][4]
            bemerkung = liste[i][6]
            fahrzeug_objekte[kennzeichen] = Fahrzeug_Anzeige(self.ui).anzeige(kennung, kennzeichen, ort, status, bemerkung, counter)
            counter += 1
        return fahrzeug_objekte




