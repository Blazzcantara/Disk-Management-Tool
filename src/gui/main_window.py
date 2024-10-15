# src/gui/main_window.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QComboBox
from src.disk_analyzer import analyze_disk, list_partitions

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Disk Management Tool")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.partition_combo = QComboBox()
        self.partition_combo.addItems(list_partitions())
        layout.addWidget(self.partition_combo)

        analyze_button = QPushButton("Analyze Disk")
        analyze_button.clicked.connect(self.analyze_disk)
        layout.addWidget(analyze_button)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def analyze_disk(self):
        selected_partition = self.partition_combo.currentText()
        analysis_result = analyze_disk(selected_partition)
        self.result_text.setText(analysis_result)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()