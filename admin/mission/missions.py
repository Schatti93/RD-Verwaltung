from admin.mission.missions_data import Missions_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class Missions_Proof():
    def __init__(self, ui):
        self.ui = ui
        self.data = Missions_Data()
        self.ui.missions_proof_get_btn.clicked.connect(self.get_mission_material)
        self.ui.missions_proof_mission_number.returnPressed.connect(self.get_mission_material)

    def get_mission_material(self):
        self.ui.missions_proof_table.setRowCount(0)
        mission_number = self.ui.missions_proof_mission_number.text()
        material = self.data.get_material(mission_number)
        if len(material) == 0:
            self.ui.missions_proof_error.setText("es wurden keine Daten zu dem Einsatz hinterlegt.")
            self.ui.missions_proof_error.setStyleSheet(
                "color:#ffffff; font-size:8pt; border: 1px solid red; border-radius: 5px")
        else:
            for entry in range(0, len(material)):
                row = self.ui.missions_proof_table.rowCount()
                check = self.check_table_entrys(material[entry][0], material[entry][1],
                                                material[entry][2])
                if check == 0:
                    self.ui.missions_proof_table.insertRow(row)
                    for data in range(0, len(material[entry])):
                        insert = QtWidgets.QTableWidgetItem(str(material[entry][data]))
                        insert.setTextAlignment(Qt.AlignCenter)
                        self.ui.missions_proof_table.setItem(row, data, insert)
                        self.ui.missions_proof_error.setText("")
                        self.ui.missions_proof_error.setStyleSheet("")
        self.ui.missions_proof_table.horizontalHeader().setSectionResizeMode(1)

    def check_table_entrys(self, product, number, date):
        rows = self.ui.missions_proof_table.rowCount()
        count = 0
        for i in range(0, rows):
            produkt_table = self.ui.missions_proof_table.item(i, 0).text()
            table_number = int(self.ui.missions_proof_table.item(i, 1).text())
            date_table = self.ui.missions_proof_table.item(i, 2).text()
            if produkt_table == product and date_table == date:
                table_number = table_number + number
                number = QtWidgets.QTableWidgetItem(str(table_number))
                number.setTextAlignment(Qt.AlignCenter)
                self.ui.missions_proof_table.setItem(i, 1, number)
                self.ui.missions_proof_table.resizeColumnsToContents()
                self.ui.missions_proof_table.horizontalHeader().setSectionResizeMode(1)
                count = 1
        return count
