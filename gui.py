import cv2
import sys
import numpy
from PIL import Image
from pixelsorter import pixelsort
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QLineEdit, QDialog, QGridLayout, QWidget
from PySide6 import QtCore

# Setup the QWigdet and other stuff
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pixelsorter GUI")
        
        # Image directory input
        self.imgdir = QLineEdit(self)
        imglabel = QLabel("img dir: ")
        
        # Difference input
        self.pxvalue = QLineEdit(self)
        pxlabel = QLabel("difference: ")
        
        # Preview button setup
        preview_button = QPushButton("Preview")
        preview_button.clicked.connect(self.preview_clicked)
        
        # Save button setup
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_clicked)
        
        # Create a grid layout with all the above 
        layout = QGridLayout(self)
        layout.addWidget(preview_button, 0, 0, 1, 1)
        layout.addWidget(save_button, 0, 1, 1, 1)
        layout.addWidget(pxlabel, 1, 0, 1, 1)
        layout.addWidget(self.pxvalue, 1, 1, 1, 1)
        layout.addWidget(imglabel, 2, 0, 1, 1)
        layout.addWidget(self.imgdir, 2, 1, 1, 1)

    @QtCore.Slot()
    
    # Preview button clicked functionality
    def preview_clicked(self):
        
        # Generate and display the pixelsort
        dir = self.imgdir.text()
        diff = self.pxvalue.text()
        cv2.destroyAllWindows()
        img = cv2.imread(str(dir))
        pxsorted = pixelsort(img, int(diff))
        cv2.imshow('CV2, check folder for sorted.png', pxsorted)
    
    # Save button clicked functionality
    def save_clicked(self):
        
        # Generate and save the pixelsort to 'sorted.png' REMEMBER TO SET USER SAVE LATER!!!
        dir = self.imgdir.text()
        diff = self.pxvalue.text()
        img = cv2.imread(str(dir))
        pxsorted = pixelsort(img, int(diff))
        cv2.imwrite('sorted.png', pxsorted)

# Launch the QWidget
app = QApplication(sys.argv)
mw = MainWindow()
mw.resize(280, 110)
mw.show()
sys.exit(app.exec())