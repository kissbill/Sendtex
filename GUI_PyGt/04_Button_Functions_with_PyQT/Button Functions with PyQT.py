import sys
import re
from PyQt4 import QtGui, QtCore
#Event is lehessen a gombra

key_01 = ''
key_02 = ''

class Window(QtGui.QMainWindow):
    

    def __init__(self):
        super(Window, self).__init__() ##superrel atadjuk a parent objektet -->QMainWindow -ot
        self.setGeometry(550, 550, 500, 300) #itt lehet hivatkozni a window-ra mint sajat maga -->self-->window
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pyLogo.png'))


        extractAcction = QtGui.QAction("&Kilepek",self)
        extractAcction.setShortcut("Ctrl+Q")
        extractAcction.setStatusTip("Leave the App")
        extractAcction.triggered.connect(self.close_application)
        self.statusBar()

        mainMenu = self.menuBar() #azert add neki valtozot mert ezt valtoztatni fogjuk nem ugy mint a statusbar
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAcction)


        self.home()

    def home(self):
        btn = QtGui.QPushButton("#Base+" ,self) #ez legyen a neve aztan kuldje el a Window-ot
        btn.clicked.connect(self.keyword_01) #Connect megmondja, mit csinaljon a gomb, ha raboknek
        btn.resize(btn.sizeHint())
        btn.resize(btn.minimumSizeHint())
        btn.move(0,25)
        btn = QtGui.QPushButton("#Base-" ,self)#ez legyen a neve aztan kuldje el a Window-ot
        btn.clicked.connect(self.keyword_02) #Connect megmondja, mit csinaljon a gomb, ha raboknek
        btn.resize(btn.sizeHint())
        btn.resize(btn.minimumSizeHint())
        btn.move(100,25)
        btn = QtGui.QPushButton("Kereses" ,self)#ez legyen a neve aztan kuldje el a Window-ot
        btn.clicked.connect(self.searching) #Connect megmondja, mit csinaljon a gomb, ha raboknek
        btn.resize(btn.sizeHint())
        btn.resize(btn.minimumSizeHint())
        btn.move(200,25)
        self.show()

        

    def keyword_01(self):
        key_01 = 'BasePlus'
        print(key_01)

    def keyword_02(self):
        key_02 = 'BaseMinus'
        print(key_02)

    # Back End
    def close_application(self):
        print('kileptel yoyo')
        sys.exit()

    def searching(self):
        # Init
        text = []
        sorban_end = []
        kulcs_szo_sora = []
        kulcsSzo = r"(?=.*)(?=.*#" + key_01 + ")(?=.*#" + key_02 + ")"
        ending = '\\+'
        pattern_keyword = re.compile( kulcsSzo )
        pattern_end = re.compile( ending )

        # Loop through text
        for i, line in enumerate(open('log_VW_FEB.txt')):
            text.append(line)
            #Kulcs szo
            for match in re.finditer(pattern_keyword, line):
                kulcs_szo_sora.append( i + 1 ) #talalt sor lementese
                break
            # Kereszt lezarasok keresese
            for match in re.finditer(pattern_end, line):
                sorban_end.append( i + 1 ) #talalt kereszt sor lementese

        # Lezaro kereszt elemek tombjenek hossza
        #hossz = len(sorban_end)
        for hits in kulcs_szo_sora:
            print('Eredeti doksiban ezen sor : %s ' % hits)
            print()
            for lezaro in sorban_end[0:len(sorban_end)]:
                if hits < lezaro:
                    #print(hits)
                    #print(lezaro)
                    break
            for megVagy in text[hits-1:lezaro-1]:
                print(megVagy, end='' )
                print()
                print('----------------------------------oo------------------------------------')







def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
