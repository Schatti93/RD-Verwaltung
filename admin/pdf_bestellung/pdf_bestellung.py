from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import datetime
from admin.pdf_bestellung.pdf_bestellung_data import Pdf_Bestellung_Data

class Pdf_Bestellung():
    def __init__(self, ui):
        self.ui = ui
        self.data = Pdf_Bestellung_Data()

    def unter_mindest_bestand(self):
        alle_daten = self.data.alle_produkte()
        liste_der_eintraege = []
        for i in range(0, len(alle_daten)):
            if int(alle_daten[i][2]) < int(alle_daten[i][3]):
                if alle_daten[i][8] == "Bestellt":
                    pass
                else:
                    liste_der_eintraege.append(alle_daten[i][1])
        return liste_der_eintraege

    def status_aendern(self, liste):
        for i in range(0, len(liste)):
            self.data.status_aendern(liste[i])

    def pdf_erstellen(self):

        material_liste = self.unter_mindest_bestand()
        if len(material_liste) == 0:
            pass
        else:
            today = datetime.date.today()
            today = today.strftime("%d.%m.%Y")
            speicherort = self.data.speicherort_abfragen()[0][1]

            try:
                pdf = canvas.Canvas(speicherort + "/benoetigtes material vom " + today + ".pdf", pagesize=A4, bottomup=0)
                pdf.setStrokeColorRGB(0.3, 0.5, 0.7)
                pdf.line(20, 30, 580, 30)

                pdf.setFillColorRGB(0.3, 0.5, 0.7)
                pdf.setFont("Helvetica-Bold", 16, leading=None)
                pdf.drawString(20, 46, "Benötigtes Material")

                pdf.setStrokeColorRGB(0.1, 0.1, 0.1)
                pdf.setFont("Helvetica", 10, leading=None)
                pdf.line(20, 80, 580, 80)
                pdf.drawString(25, 90, "Produkt")
                pdf.drawString(235, 90, "Vorhanden")
                pdf.drawString(295, 90, "Mindestbestand")
                pdf.drawString(380, 90, "Maximalbestand")
                pdf.drawString(460, 90, "differenz")
                pdf.drawString(510, 90, "Artikel Nummer")
                pdf.line(20, 95, 580, 95)

                y = 93
                x_print = 105
                x_waagerechte_linie = 93

                for i in range(0, len(material_liste)):
                    produkt_daten = self.data.produkt_abfragen(material_liste[i])

                    pdf.drawString(25, x_print, material_liste[i])
                    pdf.drawString(235, x_print, str(produkt_daten[0][2]))
                    pdf.drawString(295, x_print, str(produkt_daten[0][3]))
                    pdf.drawString(380, x_print, str(produkt_daten[0][4]))
                    differenz = int(produkt_daten[0][4]) - int(produkt_daten[0][2])
                    pdf.drawString(460, x_print, str(differenz))
                    pdf.drawString(510, x_print, str(produkt_daten[0][7]))
                    x_waagerechte_linie = x_waagerechte_linie + 20
                    pdf.line(20, x_waagerechte_linie, 580, x_waagerechte_linie)
                    x_print = x_print + 20
                    y = y + 20

                x = 80
                # senkrechten lininen
                pdf.line(20, y, 20, x)
                pdf.line(230, y, 230, x)
                pdf.line(290, y, 290, x)
                pdf.line(375, y, 375, x)
                pdf.line(455, y, 455, x)
                pdf.line(505, y, 505, x)
                pdf.line(580, y, 580, x)

                pdf.save()
                self.status_aendern(material_liste)
            except:
                pass

