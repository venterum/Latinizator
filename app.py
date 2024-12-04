import pywinstyles
import qdarktheme

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QLabel, QWidget, QPushButton, QMessageBox
from PyQt6.QtCore import Qt


def latinizator(text):
    basic_map = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 
        'е': 'e', 'ё': 'o', 'ж': 'ž', 'з': 'z', 'и': 'i', 
        'й': 'j', 'к': 'k', 'л': 'ł', 'м': 'm', 'н': 'n', 
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 
        'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'č', 
        'ш': 'š', 'щ': 'šch', 'ы': 'y', 'э': 'é', 
        'ю': 'u', 'я': 'a',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 
        'Е': 'Je', 'Ё': 'Jo', 'Ж': 'Ž', 'З': 'Z', 'И': 'I', 
        'Й': 'J', 'К': 'K', 'Л': 'Ł', 'М': 'M', 'Н': 'N', 
        'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 
        'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Č', 
        'Ш': 'Š', 'Щ': 'Šch', 'Ы': 'Y', 'Э': 'É', 
        'Ю': 'Ju', 'Я': 'Ja'
    }
    soft_map = {
        'л': 'l', 'т': 't́', 'д': 'd́', 'н': 'ń', 'п': 'ṕ',
        'с': 'ś', 'р': 'ŕ', 'з': 'ź', 'м': 'ḿ',
        'Л': 'L', 'Т': 'T́', 'Д': 'D́', 'Н': 'Ń', 'П': 'Ṕ',
        'С': 'Ś', 'Р': 'Ŕ', 'З': 'Ź', 'М': 'Ḿ'
    }
    vowels = {'а', 'о', 'у', 'э', 'ы', 'я', 'е', 'ё', 'ю', 'и',
              'А', 'О', 'У', 'Э', 'Ы', 'Я', 'Е', 'Ё', 'Ю', 'И'}
    result = []
    
    for i, char in enumerate(text):
        if char in {'ь', 'ъ'}:
            continue
        
        prev_char = text[i - 1] if i > 0 else ''
        next_char = text[i + 1] if i + 1 < len(text) else ''
        
        if char in {'е', 'ё', 'ю', 'я', 'Е', 'Ё', 'Ю', 'Я', 'И', 'и'} and (i == 0 or prev_char in {'ь', 'ъ'} or prev_char in vowels):
            result.append('J' + basic_map[char.lower()] if char.isupper() else 'j' + basic_map[char])
        
        elif char in {'е', 'ё', 'ю', 'я', 'Е', 'Ё', 'Ю', 'Я', 'И', 'и'}:
            if i == 0 or next_char.lower() in vowels or next_char in {'ь', 'ъ'}:
                result.append('J' + basic_map[char.lower()] if char.isupper() else 'j' + basic_map[char])
            else:
                result.append(basic_map[char])
        
        elif char in soft_map and next_char.lower() in {'ь', 'Ь', 'ё', 'ю', 'я', 'Ё', 'Ю', 'Я'}:
            result.append(soft_map[char])
        
        else:
            result.append(basic_map.get(char, char))
    
    return ''.join(result)


class LatinizatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Łatinizator")
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