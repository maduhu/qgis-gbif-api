# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qgis_occurrences_dialog_base.ui'
#
# Created: Wed Feb 11 14:50:20 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GBIFOccurrencesDialogBase(object):
    def setupUi(self, GBIFOccurrencesDialogBase):
        GBIFOccurrencesDialogBase.setObjectName(_fromUtf8("GBIFOccurrencesDialogBase"))
        GBIFOccurrencesDialogBase.resize(544, 574)
        self.progressBar = QtGui.QProgressBar(GBIFOccurrencesDialogBase)
        self.progressBar.setGeometry(QtCore.QRect(160, 520, 361, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.loadButton = QtGui.QPushButton(GBIFOccurrencesDialogBase)
        self.loadButton.setGeometry(QtCore.QRect(10, 510, 141, 40))
        self.loadButton.setCheckable(False)
        self.loadButton.setDefault(False)
        self.loadButton.setFlat(False)
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.loadingLabel = QtGui.QLabel(GBIFOccurrencesDialogBase)
        self.loadingLabel.setGeometry(QtCore.QRect(20, 490, 501, 20))
        self.loadingLabel.setText(_fromUtf8(""))
        self.loadingLabel.setObjectName(_fromUtf8("loadingLabel"))
        self.line = QtGui.QFrame(GBIFOccurrencesDialogBase)
        self.line.setGeometry(QtCore.QRect(10, 460, 511, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_4 = QtGui.QLabel(GBIFOccurrencesDialogBase)
        self.label_4.setGeometry(QtCore.QRect(40, 30, 62, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Grande"))
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.layoutWidget = QtGui.QWidget(GBIFOccurrencesDialogBase)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 60, 371, 273))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.institutionCodeField = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.institutionCodeField.sizePolicy().hasHeightForWidth())
        self.institutionCodeField.setSizePolicy(sizePolicy)
        self.institutionCodeField.setObjectName(_fromUtf8("institutionCodeField"))
        self.gridLayout.addWidget(self.institutionCodeField, 5, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.collectionCodeField = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collectionCodeField.sizePolicy().hasHeightForWidth())
        self.collectionCodeField.setSizePolicy(sizePolicy)
        self.collectionCodeField.setObjectName(_fromUtf8("collectionCodeField"))
        self.gridLayout.addWidget(self.collectionCodeField, 6, 1, 1, 1)
        self.publishingCountryComboBox = QtGui.QComboBox(self.layoutWidget)
        self.publishingCountryComboBox.setObjectName(_fromUtf8("publishingCountryComboBox"))
        self.gridLayout.addWidget(self.publishingCountryComboBox, 3, 1, 1, 1)
        self.basisComboBox = QtGui.QComboBox(self.layoutWidget)
        self.basisComboBox.setObjectName(_fromUtf8("basisComboBox"))
        self.gridLayout.addWidget(self.basisComboBox, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.catalogNumberField = QtGui.QLineEdit(self.layoutWidget)
        self.catalogNumberField.setObjectName(_fromUtf8("catalogNumberField"))
        self.gridLayout.addWidget(self.catalogNumberField, 4, 1, 1, 1)
        self.scientificNameField = QtGui.QLineEdit(self.layoutWidget)
        self.scientificNameField.setObjectName(_fromUtf8("scientificNameField"))
        self.gridLayout.addWidget(self.scientificNameField, 0, 1, 1, 1)
        self.countryComboBox = QtGui.QComboBox(self.layoutWidget)
        self.countryComboBox.setObjectName(_fromUtf8("countryComboBox"))
        self.gridLayout.addWidget(self.countryComboBox, 2, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.yearRangeBox = QtGui.QCheckBox(self.layoutWidget)
        self.yearRangeBox.setObjectName(_fromUtf8("yearRangeBox"))
        self.gridLayout_2.addWidget(self.yearRangeBox, 0, 0, 1, 1)
        self.minYearEdit = QtGui.QLineEdit(self.layoutWidget)
        self.minYearEdit.setObjectName(_fromUtf8("minYearEdit"))
        self.gridLayout_2.addWidget(self.minYearEdit, 1, 0, 1, 1)
        self.maxYearEdit = QtGui.QLineEdit(self.layoutWidget)
        self.maxYearEdit.setEnabled(False)
        self.maxYearEdit.setObjectName(_fromUtf8("maxYearEdit"))
        self.gridLayout_2.addWidget(self.maxYearEdit, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 7, 1, 1, 1)

        self.retranslateUi(GBIFOccurrencesDialogBase)
        QtCore.QMetaObject.connectSlotsByName(GBIFOccurrencesDialogBase)

    def retranslateUi(self, GBIFOccurrencesDialogBase):
        GBIFOccurrencesDialogBase.setWindowTitle(_translate("GBIFOccurrencesDialogBase", "GBIF Occurrences", None))
        self.loadButton.setText(_translate("GBIFOccurrencesDialogBase", "Load occurrences", None))
        self.loadButton.setShortcut(_translate("GBIFOccurrencesDialogBase", "Return", None))
        self.label_4.setText(_translate("GBIFOccurrencesDialogBase", "Filters:", None))
        self.label_8.setText(_translate("GBIFOccurrencesDialogBase", "Collection Code:", None))
        self.label_3.setText(_translate("GBIFOccurrencesDialogBase", "Country:", None))
        self.label_6.setText(_translate("GBIFOccurrencesDialogBase", "Publishing Country:", None))
        self.label_2.setText(_translate("GBIFOccurrencesDialogBase", "Basis of record:", None))
        self.label_5.setText(_translate("GBIFOccurrencesDialogBase", "Catalog Number:", None))
        self.label.setText(_translate("GBIFOccurrencesDialogBase", "Scientific name:", None))
        self.label_9.setText(_translate("GBIFOccurrencesDialogBase", "Year:", None))
        self.label_7.setText(_translate("GBIFOccurrencesDialogBase", "Institution Code:", None))
        self.yearRangeBox.setText(_translate("GBIFOccurrencesDialogBase", "Use a year range", None))

