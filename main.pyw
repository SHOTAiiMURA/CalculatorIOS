#####################################
# No need to Edit this main file.####
#####################################
# Edit Ui_Functions file to add functions or edit signal and slots.
# Setting Style sheet to widgets is also possible.

# APP Imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QTimer, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                         QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

##############################
# Import user interface file
##############################
# this is the UI file, just change this UI file name to the name of file that you just created
from UI_Main import Ui_MainWindow

# This is function file. You can make functions inside the UI file but it will be messy so its not recommended
# Check function file for more information
from Ui_Functions import Ui_Functions

# Global value for the windows status
WINDOW_SIZE = 0


# This will help us determine if the window is minimized or maximized

# Main class
class MainWindow(QMainWindow):

    def __init__(self, hide_title=False):
        QMainWindow.__init__(self)

        # Getting ui file and setting up the UI here
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)





        # Apply shadow effect (No need to remember)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(2)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        # Apply shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)


        # Minimize window
        # If Ui has a minimize Button then set up minimize action to the button
        if hasattr(self.ui, "minimizeButton"):
            # Connect button click event of minimize button with Minimize event
            # when it is clicked window will be minimized!!

            # it uses Lambda function so check it if you dont know, its really useful

            self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())



        # Close window
        # If Ui has a Close Button then set up close action to the button
        if hasattr(self.ui, "closeButton"):
            # Connect button click event of minimize button with Minimize event
            # when it is clicked window will be minimized!!
            self.ui.closeButton.clicked.connect(lambda: self.close())



        # Restore/Maximize window
        # If Ui has a Maximize Button then set up Maximize action to the button
        if hasattr(self.ui, "restoreButton"):
            # Connect button click event of maximize button with maximize event
            # when it is clicked window will be maximized!!
            # Scroll down to check the function itself
            self.ui.restoreButton.clicked.connect(lambda: self.restore_or_maximize_window())


        # Move window
        # originally we cannot move the window so we manually need to set this up

        # Define function for moving window
        def moveWindow(event):

            # Detect left button click event
            if event.buttons() == Qt.LeftButton:
                # move whole window to the cursor position
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # Check if ui has a title bar, if yes, then set up move action to the window, if not, you cannot move window
        if hasattr(self.ui, "title_bar") or hide_title:
            # Remove window default title bar
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

            # Set main background to transparent
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            if hasattr(self.ui, "title_bar"):
                # Override the mouseMoveEvent to move Window that we just made it
                self.ui.title_bar.mouseMoveEvent = moveWindow

        # Show window
        self.show()

    # Event override
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


    # Restore or maximize your window
    def restore_or_maximize_window(self):
        # Global windows state
        global WINDOW_SIZE  # The default value is zero to show that the size is not maximized
        win_status = WINDOW_SIZE

        if win_status == 0:
            # If the window is not maximized
            WINDOW_SIZE = 1  # Update value to show that the window has been maxmized
            self.showMaximized()
            # Update button icon (Lets not do this for now)
            # self.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-maximize.png"))  # Show maximized icon
        else:
            # If the window is on its default size
            WINDOW_SIZE = 0  # Update value to show that the window has been minimized/set to normal size (which is 800 by 400)
            self.showNormal()
            # Update button icon (Lets not do this for now)
            # self.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-restore.png"))  # Show minized icon

    def keyPressEvent(self, e):
        functions.key_event(e)


# Execute app
#
if __name__ == "__main__":
    import sys
    # I dont know why I need to make this app but I need to make it so I make it hahahahaha.
    app = QApplication(sys.argv)
    # make a instance of main window
    window = MainWindow(hide_title=True)
    # set up fucntions here
    functions = Ui_Functions(window)

    import sys
    sys.exit(app.exec_())
else:
    print(__name__, "hh")
# press ctrl+b in sublime to run
