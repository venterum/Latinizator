import pywinstyles
import qdarktheme

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QLabel, QWidget, QPushButton, QMessageBox
from PyQt6.QtCore import Qt


def latinizator(text):
    table = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Jo',
        'Ж': 'Ž', 'З': 'Z', 'И': 'I', 'Й': 'J', 'К': 'K', 'Л': 'L', 'М': 'M',
        'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Č', 'Ш': 'Š', 'Щ': 'Šch', 'Ы': 'Y',
        'Э': 'É', 'Ю': 'Ju', 'Я': 'Ja', 'Ь': "", 'Ъ': '',
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'jo',
        'ж': 'ž', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'č', 'ш': 'š', 'щ': 'šch', 'ы': 'y',
        'э': 'é', 'ю': 'ju', 'я': 'ja', 'ь': "", 'ъ': ''
    }
    soft_vowel = {
        'е': 'je', 'ё': 'jo',
        'Е': 'Je', 'Ё': 'Jo'
    }
    vowels = "АЕЁИОУЫЭЮЯаеёиоуыэюя"

    result = []

    words = text.split()

    for word in words:
        word_result = []
        for i, char in enumerate(word):
            if i == 0 and char in soft_vowel:
                word_result.append(soft_vowel[char])
            elif char in ('Ъ', 'ъ') and i + 1 < len(word) and word[i + 1] in soft_vowel:
                word_result.append(soft_vowel[word[i + 1]])
                continue
            elif char in soft_vowel and i > 0 and word[i - 1] in vowels:
                word_result.append(soft_vowel[char])
            else:
                word_result.append(table.get(char, char))
        result.append(''.join(word_result))
    return ' '.join(result)


class LatinizatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Latinizator")
        self.setGeometry(100, 100, 400, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.input_field = QTextEdit()
        self.input_field.setPlaceholderText("Введите текст на русском...")
        self.input_field.textChanged.connect(self.update_output)

        self.output_label = QLabel("Текст на латинице появится здесь.")
        self.output_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.output_label.setWordWrap(True)
        self.output_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.copy_button = QPushButton("Скопировать")
        self.copy_button.clicked.connect(self.copy_to_clipboard)

        layout.addWidget(self.input_field)
        layout.addWidget(self.output_label)
        layout.addWidget(self.copy_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_output(self):
        text = self.input_field.toPlainText()
        translated = latinizator(text)
        self.output_label.setText(translated)

    def copy_to_clipboard(self):
        text = self.output_label.text()
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
    pywinstyles.apply_style(window, "dark")
    app.exec()