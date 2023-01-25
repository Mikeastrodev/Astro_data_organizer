import os
import shutil
from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog, QCheckBox)
from PyQt5.QtGui import QPixmap

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'ADO'
        self.left = 100
        self.top = 100
        self.width = 290
        self.height = 225
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create a background image
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 290, 225)
        self.label.setPixmap(QPixmap(sys._MEIPASS + '/bckg.jpg'))

        # Create a "Select Folder" button
        self.select_folder_button = QPushButton("Select Folder", self)
        self.select_folder_button.clicked.connect(self.select_folder)

        # Create a "Organize" button
        self.organize_button = QPushButton("Organize", self)
        self.organize_button.clicked.connect(self.organize)

        # Create checkboxes for organizing by filter, target, and exposure time
        self.by_filter_checkbox = QCheckBox("Filter", self)
        self.by_target_checkbox = QCheckBox("Target", self)
        self.by_exposure_time_checkbox = QCheckBox("Exposure Time", self)

        # Create a layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.select_folder_button)
        layout.addWidget(self.organize_button)
        layout.addWidget(self.by_filter_checkbox)
        layout.addWidget(self.by_target_checkbox)
        layout.addWidget(self.by_exposure_time_checkbox)

        self.setLayout(layout)

        self.show()

    def select_folder(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")

    def organize(self):
        by_filter = self.by_filter_checkbox.isChecked()
        by_target = self.by_target_checkbox.isChecked()
        by_exposure_time = self.by_exposure_time_checkbox.isChecked()

        # Get a list of all files in the folder
        files = os.listdir(self.folder_path)

        # Iterate over each file
        for file in files:
            # Check if the file is a .jpg
            if file.endswith('.jpg'):
                # If it is, delete the file permanently
                os.remove(os.path.join(self.folder_path, file))
            elif file.endswith('.fit'):
                # Split the file name by underscores
                file_parts = file.split('_')

                # Set the initial folder path as the selected folder
                subfolder_path = self.folder_path
                if by_target:
                    # Extract the target name from the file name
                    target_name = file_parts[1]
                    # Create a subfolder for the target if it doesn't already exist
                    subfolder_path = os.path.join(subfolder_path, target_name)
                    if not os.path.exists(subfolder_path):
                        os.mkdir(subfolder_path)
                if by_exposure_time:
                    # Extract the exposure time from the file name
                    exposure_time = file_parts[2]
                    # Create a subfolder for the exposure time if it doesn't already exist
                    subfolder_path = os.path.join(subfolder_path, exposure_time)
                    if not os.path.exists(subfolder_path):
                        os.mkdir(subfolder_path)
                if by_filter:
                    # Extract the filter name from the file name
                    filter_name = file_parts[5]
                    # Create a subfolder for the filter if it doesn't already exist
                    subfolder_path = os.path.join(subfolder_path, filter_name)
                    if not os.path.exists(subfolder_path):
                        os.mkdir(subfolder_path)
                # Move the .fit file to the final subfolder
                shutil.move(os.path.join(self.folder_path, file), os.path.join(subfolder_path, file))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())