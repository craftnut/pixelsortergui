import cv2
import sys
import numpy
from PIL import Image
from pixelsorter import pixelsort
from ctypes import alignment
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QDialog, QGridLayout, QWidget
from PySide6 import QtCore


# img = cv2.imread('test.png')
diff:int = 0


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pixelsorter GUI")
        
        self.imgdir = QLineEdit(self)
        imglabel = QLabel("img dir: ")
        self.pxvalue = QLineEdit(self)
        pxlabel = QLabel("difference: ")
        
        go = QPushButton("go")
        go.clicked.connect(self.go_clicked)
        
        layout = QGridLayout(self)
        layout.addWidget(go, 0, 0, 1, 1)
        layout.addWidget(pxlabel, 1, 0, 1, 1)
        layout.addWidget(self.pxvalue, 1, 1, 1, 1)
        layout.addWidget(imglabel, 2, 0, 1, 1)
        layout.addWidget(self.imgdir, 2, 1, 1, 1)
        
    # class Image(QApplication):
    #     def __init__(self):
    #         super().__init__()
    #         label = QLabel(self)
    #         pixmap = QPixmap('sorted.png')
    #         label.setPixmap(pixmap)
    #         self.setWindowTitle("test show")
    #         self.setCentralWidget(label)
    #         self.resize(pixmap.width(), pixmap.height())
            
    @QtCore.Slot()
    
    def go_clicked(self):
        
        dir = self.imgdir.text()
        diff = self.pxvalue.text()
        
        cv2.destroyAllWindows()
        img = cv2.imread(str(dir))
        pxsorted = pixelsort(img, int(diff))
        cv2.imshow('CV2, check folder for sorted.png', pxsorted)
        cv2.imwrite('sorted.png', pxsorted)
        # show = MainWindow.Image()
        # show.exec()
        

app = QApplication(sys.argv)
mw = MainWindow()
mw.resize(280, 110)
mw.show()
sys.exit(app.exec())