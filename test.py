import PyQt5.QtWidgets as p
import sys,os
from PyQt5.QtGui import QPixmap,QFont,QPainter
from PyQt5 import QtCore,QtMultimedia


class Main(p.QWidget):
    def __init__(self, name1='Начать игру',
                       name2='Продолжить',
                       name3='Настройки',
                       name4='Выход',
                       fil = 'menu.jpg',
                       mus = 'mentheme.mp3'):
        super().__init__()

        box = p.QHBoxLayout(self)                                       # +++ self
#        pixmap = QPixmap('%s/data/images/%s' % (sys.path[0],fil))
        pixmap = QPixmap('ball.png')

        lbl = p.QLabel(self)
        lbl.setPixmap(pixmap)
        box.addWidget(lbl)
        self.but1 = p.QPushButton(name1,lbl)
        self.but2 = p.QPushButton(name2,lbl)
        self.but3 = p.QPushButton(name3,lbl)
        self.but4 = p.QPushButton(name4,lbl)

        self.but1.move(100, 650)
        self.but2.move(400, 650)
        self.but3.move(700, 650)
        self.but4.move(1000,650)

        self.but1.setStyleSheet('Background:red')
        self.but2.setStyleSheet('Background:red')
        self.but3.setStyleSheet('Background:red')
        self.but4.setStyleSheet('Background:red')

        self.but1.setFont(QFont('Arial',20))
        self.but2.setFont(QFont('Arial',20))
        self.but3.setFont(QFont('Arial',20))
        self.but4.setFont(QFont('Arial',20))

        self.but1.setFixedSize(250,70)
        self.but2.setFixedSize(250,70)
        self.but3.setFixedSize(250,70)
        self.but4.setFixedSize(250,70)

#        self.path = QtCore.QDir.current().absoluteFilePath('%s/data/music/%s' % (sys.path[0],mus))
        self.path = QtCore.QDir.current().absoluteFilePath('D:/_Qt/Mp3/zvuki_prirody-td.wav')

        self.media = QtCore.QUrl.fromLocalFile(self.path) 
        self.content = QtMultimedia.QMediaContent(self.media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(self.content)
        self.player.play()

        self.showFullScreen()
        self.but4.clicked.connect(quit)


# ?        sys.exit(app.exec_())


class Win(Main):
#    def __init__(self, name1, name2, name3, name4, fil,mus):
#        super().__init__(name1, name2, name3, name4, fil,mus)

# + vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

    def __init__(self):
        super().__init__()

        self.but1.clicked.connect(self.goGeme)

    def goGeme(self): 
        self.close(); 
        msg = p.QWidget(); 
        but = p.QPushButton('Hello',msg); 
        msg.show()
        sys.exit(app.exec_()) 

# + ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        

class Map:
    def __init__(self):
        pass


class Icons:
    pass


class Video:
    pass


def start_game():
    pass

def setting():
    pass

def quit():
    sys.exit()

def cont_game():
    pass


if __name__ == "__main__":                  # +++
    app = p.QApplication(sys.argv)
    r = Win()                               # - Main()
    r.show()                                # +++
    sys.exit(app.exec_())                   # +++