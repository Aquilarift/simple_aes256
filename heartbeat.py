# This Python file uses the following encoding: utf-8
import os
import sys
import pyperclip
import hashlib
import json

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad
from Cryptodome.Util.Padding import unpad
from base64 import b64encode
from base64 import b64decode

from PyQt6 import QtCore, QtWidgets

import mainwindow
import signdialog
import settingsform
import passchangedialog
import vignere


class HeartBeat(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.login = Login()
        self.settings = Settings()
        self.login.show()

        self.comboBox.addItems([str(x) for x in self.settings.d])

        self.copyButton.clicked.connect(self.copyClick)
        self.pasteButton.clicked.connect(self.pasteClick)
        self.clearButton.clicked.connect(self.clearClick)
        self.settingsButton.clicked.connect(self.openSettings)
        self.encButton.clicked.connect(self.encrypt)
        self.decButton.clicked.connect(self.decrypt)

    def decrypt(self):
        key = b64decode(vignere.decrypt(
            self.settings.d[self.comboBox.currentText()], pas))
        try:
            crtext = b64decode(self.textEdit.toPlainText())
            iv = crtext[:16]

            cipher = AES.new(key, AES.MODE_CBC, iv)
            text = unpad(cipher.decrypt(crtext[16:]), AES.block_size)
            self.textEdit.setText(text.decode())
        except:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Incorrect text')

    def encrypt(self):
        key = b64decode(vignere.decrypt(
            self.settings.d[self.comboBox.currentText()], pas))
        text = self.textEdit.toPlainText().encode()

        cipher = AES.new(key, AES.MODE_CBC)
        crtext = cipher.encrypt(pad(text, AES.block_size))
        self.textEdit.setText(b64encode(cipher.iv + crtext).decode())

    def openSettings(self):
        self.settings.show()

    def copyClick(self):
        pyperclip.copy(self.textEdit.toPlainText())

    def pasteClick(self):
        self.textEdit.setPlainText(pyperclip.paste())

    def clearClick(self):
        self.textEdit.clear()


class Settings(QtWidgets.QWidget, settingsform.Ui_Form):
    item = ...
    d = {}

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        with open('data.json', 'r') as f:
            self.d = json.load(f)
            f.close()
        self.laodList()

        self.checkBox.stateChanged.connect(self.showPassword)
        self.exitButton.clicked.connect(self.saveAndExit)
        self.changepassButton.clicked.connect(self.changePass)
        self.addButton.clicked.connect(self.addNick)
        self.removeButton.clicked.connect(self.removeNick)
        self.listWidget.itemClicked.connect(self.setItem)
        self.generateButton.clicked.connect(self.generateKey)
        self.saveButton.clicked.connect(self.saveK)
        self.clearButton.clicked.connect(self.clearKey)

    def closeEvent(self, event):
        window.comboBox.clear()
        window.comboBox.addItems([str(x) for x in self.d])
        event.accept()

    def clearKey(self):
        self.d[self.item.text()] = ''
        self.lineEdit.setText('')
        self.saveKeys()

    def laodList(self):
        for nick in self.d:
            self.listWidget.addItem(nick)

    def saveK(self):
        self.d[self.item.text()] = vignere.encrypt(self.lineEdit.text(), pas)
        self.saveKeys()

    def generateKey(self):
        key = get_random_bytes(32)
        self.lineEdit.setText(b64encode(key).decode())

        self.d[self.item.text()] = vignere.encrypt(
            b64encode(key).decode(), pas)

    def setItem(self, item):
        self.item = item
        self.lineEdit.setText(vignere.decrypt(self.d[item.text()], pas))

    def removeNick(self):
        with open('data.dat', 'r') as f:
            t, ok = QtWidgets.QInputDialog.getText(self, 'Login', 'Password:')
            if (
                (ok)
                and (hashlib.md5(t.encode()).hexdigest() == f.readline())
                and (self.listWidget.count() != 0)
            ):
                self.listWidget.takeItem(
                    self.listWidget.indexFromItem(self.item).row())
                try:
                    del self.d[self.item.text()]
                except:
                    QtWidgets.QMessageBox.warning(
                        self, 'Error', 'Choose nickname')

                self.saveKeys()
                self.lineEdit.setText("")
            f.close()

    def addNick(self):
        t, ok = QtWidgets.QInputDialog.getText(self, 'Add', 'Nickname:')
        if (ok):
            self.listWidget.addItem(t)

            self.d.update([(t, '')])
            self.saveKeys()

    def changePass(self):
        self.passdialog = ChangePass()
        self.passdialog.show()

    def saveAndExit(self):
        # Добавить сохранение

        self.close()

    def showPassword(self, state):
        if (state == 2):
            self.lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def saveKeys(self):
        # VIGNERE NICKNAMES
        with open('data.json', 'w') as f:
            json.dump(self.d, f, ensure_ascii=False, indent=4)
            f.close()


class ChangePass(QtWidgets.QDialog, passchangedialog.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.buttonBox.accepted.disconnect()
        self.buttonBox.accepted.connect(self.baccept)

    def baccept(self):
        # VIGNERE NICK
        with open('data.dat', 'r+') as f:
            if (hashlib.md5(self.lineEdit.text().encode()).hexdigest() == f.readline()):
                global pas
                old_pas = pas
                pas = self.lineEdit_2.text()
                f.seek(0)
                f.write(hashlib.md5(pas.encode()).hexdigest())
                f.close()

                with open('data.json', 'r') as jf:
                    d = json.load(jf)
                    jf.close()
                with open('data.json', 'w') as jf:
                    for nick in d:
                        d[nick] = vignere.encrypt(
                            vignere.decrypt(d[nick], old_pas), pas)
                    json.dump(d, jf, ensure_ascii=False, indent=4)
                    jf.close()
                self.accept()


class Login(QtWidgets.QDialog, signdialog.Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setModal(True)
        self.setWindowTitle(u'Login')
        self.setWindowFlags(self.windowFlags() &
                            ~QtCore.Qt.WindowType.WindowCloseButtonHint &
                            ~QtCore.Qt.WindowType.WindowMinMaxButtonsHint)

        self.buttonBox.accepted.disconnect()
        self.buttonBox.accepted.connect(self.login)
        self.rejected.connect(self.exit)

    def login(self):
        with open('data.dat', 'r') as f:
            key = f.readline()
            if (hashlib.md5(self.lineEdit.text().encode()).hexdigest() == key):
                global pas
                pas = self.lineEdit.text()
                self.accept()
            f.close()

    def exit(self):
        sys.exit(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = HeartBeat()
    window.show()
    sys.exit(app.exec())
