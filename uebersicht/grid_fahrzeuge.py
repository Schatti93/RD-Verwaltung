from PyQt5 import QtWidgets
from PyQt5 import QtCore

class Grid_Fahrzeuge():
    def __init__(self, ui):
        self.ui = ui
        #self.grid_fahrzeug_anzeige()

    def grid_fahrzeug_anzeige(self):

        self.ui.verticalLayoutWidget = QtWidgets.QWidget(self.ui.tab_4)
        self.ui.verticalLayoutWidget.setGeometry(QtCore.QRect(680, 100, 570, 784))
        self.ui.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.ui.fahrzeug_grid = QtWidgets.QVBoxLayout(self.ui.verticalLayoutWidget)
        self.ui.fahrzeug_grid.setContentsMargins(0, 0, 0, 0)
        self.ui.fahrzeug_grid.setObjectName("fahrzeug_grid")

    def second_grid(self):
        self.ui.verticalLayoutWidget2 = QtWidgets.QWidget(self.ui.tab_4)
        self.ui.verticalLayoutWidget2.setGeometry(QtCore.QRect(1300, 100, 570, 784))
        self.ui.verticalLayoutWidget2.setObjectName("verticalLayoutWidget2")
        self.ui.fahrzeug_grid2 = QtWidgets.QVBoxLayout(self.ui.verticalLayoutWidget2)
        self.ui.fahrzeug_grid2.setContentsMargins(0, 0, 0, 0)
        self.ui.fahrzeug_grid2.setObjectName("fahrzeug_grid2")