import barcode
from barcode.writer import ImageWriter
from admin.barcodes.barcode_data import Barcode_Data

class Generate_Barcodes():
    def __init__(self):
        self.data = Barcode_Data()

    # TODO change barcode size
    def generate_barcode(self):
        barcodes = self.data.get_barcodes()
        min = self.data.get_barcode_location()[0][2]
        list = []
        for i in range(0, len(barcodes)):
            try:
                list.append(int(barcodes[i][0]))
            except ValueError:
                pass
        list = sorted(list)
        if len(list) > 0:
            new_barcode = list[-1] + 1
        else:
            new_barcode = min + 1
        if new_barcode <= min:
            new_barcode = min + 1
        if len(str(new_barcode)) < 4:
            einsetzen = 4 - len(str(new_barcode))
            barcode_string = einsetzen * "0" + str(new_barcode)
        return barcode_string

    def generate_barcode_image(self, new_barcode, product):
        EAN = barcode.get_barcode_class('code128')
        place_to_save = self.data.get_barcode_location()
        if len(place_to_save) > 0:
            place_to_save = place_to_save[0][1]
            ean = EAN(new_barcode, writer=ImageWriter())
            try:
                ean.save(place_to_save + product + ' barcode', None, product)
            except FileNotFoundError:
                pass
