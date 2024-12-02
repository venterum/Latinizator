# Latinizator

Latinizator — это приложение для транслитерации текста русского языка в латиницу. Оно поддерживает различные правила замены символов и учитывает особенности произношения, такие как мягкие гласные после твёрдого знака или в начале слова. Приложение позволяет вводить текст, автоматически преобразовывать его в латиницу, а также копировать результат в буфер обмена.

## Функциональность

- Автоматическая транслитерация текста с учётом особенностей произношения (например, "Я" заменяется на "Ja" в начале слова).
- Поддержка ввода и вывода текста с несколькими строками.
- Возможность копирования результата в буфер обмена.
- Мгновенное обновление результата при изменении текста.

## Установка

Для работы с приложением потребуется Python и несколько библиотек:

1. Установите Python (желательно последнюю версию 3.x) с [официального сайта](https://www.python.org/).
2. Скачайте или клонируйте проект:
   ```bash
   git clone https://github.com/venterum/Latinizator.git
   cd latinizator
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Запустите приложение:
   ```bash
   python app.py
   ```

## Зависимости

- PyQt6
- qdarktheme
- pywinstyles

Проект распространяется под лицензией MIT.
