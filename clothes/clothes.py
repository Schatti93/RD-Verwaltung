from datetime import date
from clothes.clothes_data import Clothes_Data

class Clothes():
    def __init__(self, ui):
        self.ui = ui
        self.data = Clothes_Data()
        #self.ui.clothes_button.clicked.connect(self.go_through_table_entrys)



    def read_from_database(self, database):
        list = self.data.get_liste(database)
        mode = (1, 1)
        return_list = []
        for i in range(0, len(list)):
            return_list.append([list[i], mode])
        return return_list

    def in_out(self, content):
        datas = self.data.get_liste("Klamotten")
        return_bool = False
        for i in range(0, len(datas)):
            if content == datas[i][1]:
                return_bool = True
                self.data.add_barcode(content)
                break
            else:
                if i == len(datas):
                    self.data.switch_barcode(content)
        return return_bool