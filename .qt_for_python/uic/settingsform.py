# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsform.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(650, 200)
        Form.setMaximumSize(QSize(900, 400))
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.listWidget)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.generateButton = QPushButton(Form)
        self.generateButton.setObjectName(u"generateButton")

        self.horizontalLayout_2.addWidget(self.generateButton)

        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_2.addWidget(self.saveButton)

        self.clearButton = QPushButton(Form)
        self.clearButton.setObjectName(u"clearButton")

        self.horizontalLayout_2.addWidget(self.clearButton)

        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_2.addWidget(self.checkBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addButton = QPushButton(Form)
        self.addButton.setObjectName(u"addButton")

        self.verticalLayout.addWidget(self.addButton)

        self.removeButton = QPushButton(Form)
        self.removeButton.setObjectName(u"removeButton")

        self.verticalLayout.addWidget(self.removeButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.changepassButton = QPushButton(Form)
        self.changepassButton.setObjectName(u"changepassButton")

        self.verticalLayout_3.addWidget(self.changepassButton)

        self.exitButton = QPushButton(Form)
        self.exitButton.setObjectName(u"exitButton")

        self.verticalLayout_3.addWidget(self.exitButton)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.listWidget.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Settings", None))
        self.generateButton.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save key", None))
        self.clearButton.setText(QCoreApplication.translate("Form", u"Clear key", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Show", None))
        self.addButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.removeButton.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.changepassButton.setText(QCoreApplication.translate("Form", u"Change login password", None))
        self.exitButton.setText(QCoreApplication.translate("Form", u"Exit", None))
    # retranslateUi

