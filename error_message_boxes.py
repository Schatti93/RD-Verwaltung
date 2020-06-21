from PyQt5.QtWidgets import QMessageBox

class Error_Message_Boxes():

    def message_box_only_ok(self, text, window_title):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle(window_title)
        msgBox.setStandardButtons(QMessageBox.Ok)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass