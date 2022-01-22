from ast import Return
from PyQt5 import  uic,QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QMessageBox, QPushButton, QTableWidget, QVBoxLayout, QWidget, QSizePolicy
from PyQt5.QtGui import QIcon
from numpy import mean


soma = 0 

def calculando():   
    primos = []
    campo_1 = int(calcular.spinBox.text())
    campo_2 = int(calcular.spinBox_2.text())

    # Verificar se o campo_2 é menos que o campo_1
    if campo_2 < campo_1:   
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Informação:")
        msgBox.setIcon(msgBox.Information)
        msgBox.setText('O Segundo campo precisa ser maior que o primeiro')
        msgBox.exec()
        return

    # Lógica aplicada para calcular os intervalos dos numeros primos
    for i in range(campo_1, campo_2+1):
        qtd_divisores = 0
        for j in range(1, i+1):
            if i % j == 0:
                qtd_divisores +=1
        if qtd_divisores == 2:
            primos.append(i)

    # Soma, contagem e média dos números primos
    soma_dos_primos = sum(primos)
    contagem_dos_primos = len(primos)
    avg = mean(primos)
    
    # Impressão na tela dos resultados da consulta
    calcular.label_4.setText("Os Números Primos no Intervalo de: "  +str(campo_1) +  ' e '   +str(campo_2) +
                '  São :\n' + str(primos).replace('[','').replace(']',''))
                
    calcular.label_6.setText("A quantidade de números primos entre: "  +str(campo_1) +  ' e '   +str(campo_2) +
                '  São :\n' +str(contagem_dos_primos))

    calcular.label_7.setText("A soma de todos os números primos entre: "  +str(campo_1) +  ' e '   +str(campo_2) +
                '  São :\n' +str(soma_dos_primos))

    calcular.label_8.setText("A média aritmética dos números primos entre: "  +str(campo_1) +  ' e '   +str(campo_2) +
                '  São :\n' +str(avg).replace('nan','0'))

    # Fim da impressão

app=QtWidgets.QApplication([])
calcular=uic.loadUi("calculadora.ui")
calcular.setWindowIcon(QIcon("calc_icon.png"))
calcular.pushButton.clicked.connect(calculando)
calcular.setStyleSheet('QPushButton {color: white}')


calcular.show()
app.exec()