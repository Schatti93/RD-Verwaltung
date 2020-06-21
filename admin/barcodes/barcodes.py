import barcode
from barcode.writer import ImageWriter
from admin.barcodes.barcode_data import Barcode_Data
from error_message_boxes import Error_Message_Boxes

class Generate_Barcodes():
    def __init__(self):
        self.data = Barcode_Data()
        self.error = Error_Message_Boxes()
        self.generate_barcode_image("test", "test")

    # TODO user button for barcode_generator_image. But at this time I dont now where.
    def generate_barcode(self):
        barcodes = self.data.get_barcodes()
        min = self.data.get_barcode_data()[0][2]
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
        else:
            barcode_string = str(new_barcode)

        return barcode_string

    def generate_barcode_image(self, new_barcode, product):
        EAN = barcode.get_barcode_class('code128')
        barcode_data = self.data.get_barcode_data()
        if len(barcode_data) > 0:
            place_to_save = barcode_data[0][1]
            hight = float(barcode_data[0][3])
            width = float(barcode_data[0][4])
            font_size = int(barcode_data[0][5])
            font_distance = int(barcode_data[0][6])
            ean = EAN(new_barcode, writer=ImageWriter())
            try:
                ean.save(place_to_save + "/" + product + ' barcode',
                         {"module_width": width, "module_height": hight, "font_size": font_size,
                          "text_distance": font_distance}, product)
            except FileNotFoundError:
                self.error.message_box_only_ok("Ups, da lief etwas schief. Überprüfe bitte den Speicherpfad in den "
                                               "Einstellungen", "Barcode konnte nicht erstellt werden.")
