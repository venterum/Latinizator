import qdarktheme

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6 import uic

from latinizator import latinizator


class LatinizatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.setWindowTitle("Latinizator")
        self.setGeometry(100, 100, 1219, 644)
        self.originalTextEdit.textChanged.connect(self.update_output)
        self.copyButton.clicked.connect(self.copy_to_clipboard)
        self.translitedText.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.originalTextEdit.setPlaceholderText("Введите текст на русском...")
        self.translitedText.setPlaceholderText("Текст на латинице появится здесь.")

    def update_output(self):
        text = self.originalTextEdit.toPlainText()
        translated = latinizator(text)
        self.translitedText.setText(translated)

    def copy_to_clipboard(self):
        text = self.translitedText.toPlainText()
        if text.strip():
            QApplication.clipboard().setText(text)
            QMessageBox.information(self, "Успех", "Текст скопирован в буфер обмена.")
        else:
            QMessageBox.warning(self, "Ошибка", "Нет текста для копирования.")


if __name__ == "__main__":
    app = QApplication([])
    window = LatinizatorApp()
    window.show()
    app.setStyleSheet(qdarktheme.load_stylesheet())
    app.exec()