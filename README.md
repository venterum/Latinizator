# Latinizator

Latinizator — это инструмент для транслитерации текста на русском языке в латиницу. Поддерживается работа как через графический интерфейс (PyQt), так и через веб-интерфейс (Flask).

## Примеры

| Русский текст                                  | Латинизированный текст                                  |
|------------------------------------------------|-------------------------------------------------------|
| Съешь ещё этих мягких французских булок, да выпей чаю. | Sješ ješchо étih ḿagkih francuzskih bulok, da vypej čaju. |

---

## Таблица соответствия букв русского и латинского алфавита

| Латинские буквы | Русские буквы |
|-----------------|---------------|
| A a             | А а           |
| B b             | Б б           |
| C c             | Ц ц           |
| Č č             | Ч ч           |
| D d             | Д д           |
| E e             | Е е           |
| É é             | Э э           |
| F f             | Ф ф           |
| G g             | Г г           |
| H h             | Х х           |
| I i             | И и           |
| J j             | Й й           |
| Jo jo           | Ё ё           |
| Ju ju           | Ю ю           |
| Ja ja           | Я я           |
| K k             | К к           |
| L l             | Л л           |
| M m             | М м           |
| N n             | Н н           |
| O o             | О о           |
| P p             | П п           |
| R r             | Р р           |
| S s             | С с           |
| Š š             | Ш ш           |
| Šch šch         | Щ щ           |
| T t             | Т т           |
| U u             | У у           |
| V v             | В в           |
| Y y             | Ы ы           |
| Z z             | З з           |
| Ž ž             | Ж ж           |

*Примечание*: Мягкий знак (`ь`) и твёрдый знак (`ъ`) не транслитерируются, но влияют на смягчение согласных и йотирование гласных.

---

## Правила транслитерации

- **Обозначение мягкости согласных**  
   Перед смягчающими гласными (`е`, `ё`, `ю`, `я`) или мягким знаком (`ь`) согласные смягчаются во измбежание неверного прочтения, обозначается акутом (`´`):  
   - *Ĺudi* (люди)  
   - *Zeleń* (зелень)  

- **Йотирование гласных**  
   Гласные `е`, `ё`, `ю`, `я`, которые читаются как два звука в начале слова, после мягкого/твёрдого знаков или после других гласных, пишется с буквой `j`:  
   - *Jelena* (Елена)  
   - *Objektiv* (объектив)  

- **Мягкий и твёрдый знаки**  
   Эти буквы опускаются при переводе текста, но влияют на тем не менее также влияют на соседние буквы.  
   Примеры:  
   - *Vaĺjažnyj* (вальяжный)  
   - *Podjezd* (подъезд)

---

## Установка и запуск

### Локальное использование (PyQt)
1. Установите Python 3.x.
2. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/venterum/Latinizator.git
   cd latinizator
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Запустите приложение:
   ```bash
   python web.py
   ```

### Развёртывание веб-приложения (Flask)
1. Убедитесь, что зависимости установлены:
   ```bash
   pip install -r requirements.txt
   ```
2. Запустите веб-сервер:
   ```bash
   python app.py
   ```
3. Перейдите в браузер по адресу [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

## Зависимости

- **Flask** — веб-фреймворк.
- **PyQt6** — для настольного приложения.
- **qdarktheme** — тёмная тема для PyQt.
- **pywinstyles** — стилизация окон.

Установка:
```bash
pip install -r requirements.txt
```
