# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


# окнонное приложение на базе QWidget
class Example(QWidget):

    def __init__(self):
        # инициализация QWidget
        super().__init__()

        # инициализация окна выносим в отдельный метод (ниже)
        self.initUI()

    def initUI(self):
        # устанавливаем размері и заголовок окна
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')

        # создаем кнопку для закрытия окна
        qButton = QPushButton('Quit', self)
        qButton.clicked.connect(self.close)

        # подгоняем размеры кнопки под надпись(sizeHint)
        qButton.resize(qButton.sizeHint())

        # перемещаем кнопку в новое положение
        qButton.move(50, 50)

        # показываем что наворотили
        self.show()


if __name__ == '__main__':

    # проверяем, нет ли в памяти объекта app
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    # создаем экземпляр оконного приложения
    ex = Example()
    # запускаем цикл ожидания событий
    app.exec_()
