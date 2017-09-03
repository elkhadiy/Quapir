# coding: utf-8

import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, QMenu, qApp, QApplication)
from PyQt5.QtGui import QIcon

#
# Current progress : starting http://zetcode.com/gui/pyqt5/layout/
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

        # An other menu, named "View", with a checkable entry
        viewMenu = menubar.addMenu('&View')
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggle_status_bar)
        viewMenu.addAction(viewStatAct)

        # Add the "Exit" action to a new toolbar
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('StatusBar and Menu')
        self.show()

    def toggle_status_bar(self, state):
        if state:
            self.status_bar.show()
        else:
            self.status_bar.hide()

    def contextMenuEvent(self, event):
        """
        Create a context menu that will show up on a right click anywhere in
        the window.
        """
        cmenu = QMenu(self)

        newAct = cmenu.addAction("&New")
        openAct = cmenu.addAction("&Open")
        quitAct = cmenu.addAction("&Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())