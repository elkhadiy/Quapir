# coding: utf-8

import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, QMenu, qApp, QApplication)
from PyQt5.QtGui import QIcon

#
# Current progress : Context menu of http://zetcode.com/gui/pyqt5/menustoolbars/
#

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create the status bar
        self.status_bar = self.statusBar()
        # show a message in the statusbar
        self.status_bar.showMessage('Ready')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File') # the '&' makes it possible to use
            # single character shortcut to access the menu items (underline
            # a letter of the items)

        # sub-menu
        impMenu = QMenu('&Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)
        fileMenu.addMenu(impMenu)

        # 'New' action in the menu
        newAct = QAction('New', self)
        fileMenu.addAction(newAct)

        # 'Exit' action in the 'File' menu
        exitAct = QAction(QIcon('exit-door.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application') # tip displayed in status bar
        exitAct.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAct)

        viewMenu = menubar.addMenu('&View')
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)
        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('StatusBar and Menu')
        self.show()

    def toggleMenu(self, state):
        if state:
            self.status_bar.show()
        else:
            self.status_bar.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())