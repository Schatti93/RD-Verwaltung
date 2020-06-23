from clothes.ui_clothes import UI_Clothes
class UI_Manager():
    def __init__(self, ui):
        self.ui = ui
        self.ui_clothes = UI_Clothes(self.ui)
