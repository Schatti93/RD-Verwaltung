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

            for entry in range(0, len(material)):
                row = self.ui.missions_proof_table.rowCount()
                self.ui.missions_proof_table.insertRow(row)
                for data in range(0, len(material[entry])):
                    insert = QtWidgets.QTableWidgetItem(str(material[entry][data]))
                    insert.setTextAlignment(Qt.AlignCenter)
                    self.ui.missions_proof_table.setItem(row, data, insert)
        self.ui.missions_proof_table.horizontalHeader().setSectionResizeMode(1)