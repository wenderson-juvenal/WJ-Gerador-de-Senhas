import sys
from functions import *
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QCheckBox, QVBoxLayout, QMessageBox

with open("style.css") as file:
    style = file.read()

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()

window.setFixedSize(400, 500)
window.setWindowTitle("WJ-Gerador de senhas")
window.setStyleSheet(style)

# label que vai armazenar a senha gerada
label = QLabel("", window)
label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
label.setMaximumWidth(600)

# opções de caracteres
upperCase = QCheckBox("Letras maiúsculas", window)
upperCase.toggle()

lowerCase = QCheckBox("Letras minúsculas", window)
lowerCase.toggle()

num = QCheckBox("Números", window)
num.toggle()

specialChar = QCheckBox("Caracteres especiais", window)
specialChar.toggle()

# input do usuário com o tamanho da senha
passSize = QLineEdit()
passSize.setPlaceholderText("Tamanho da senha")
passSize.setMaxLength(2)

# botao gerar senha
btnGenerate = QPushButton("Gerar senha")
btnGenerate.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
btnGenerate.clicked.connect(lambda: generatePassword(window, QMessageBox, label, passSize.text(), upperCase.isChecked(), lowerCase.isChecked(), num.isChecked(), specialChar.isChecked()))

# botao copiar senha
btnCopy = QPushButton("copiar")
btnCopy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
btnCopy.clicked.connect(lambda: copyText(label))
btnCopy.setStyleSheet("padding:0; background-color: transparent; border:1px solid #1c233f; color:#1c233f; font-size:10px")
btnCopy.setFixedSize(70, 30)

layout.addWidget(label)
layout.addWidget(btnCopy, alignment=Qt.AlignmentFlag.AlignRight)
layout.addWidget(upperCase)
layout.addWidget(lowerCase)
layout.addWidget(num)
layout.addWidget(specialChar)
layout.addWidget(passSize)
layout.addWidget(btnGenerate)
layout.setSpacing(4)
window.setLayout(layout)

window.show()
app.exec()
