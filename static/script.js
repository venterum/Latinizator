const inputText = document.getElementById('input-text');
const outputText = document.getElementById('output-text');
const clearButton = document.getElementById('clear-input');
const copyButton = document.getElementById('copy-output');
const lineNumbers = document.getElementById('line-numbers');

// Инициализация нумерации строк
function updateLineNumbers() {
    const input = document.getElementById('input-text');
    const lineNumbers = document.getElementById('line-numbers');
    const lines = input.value.split('\n');
    const count = lines.length;
    
    let html = '';
    for (let i = 1; i <= count; i++) {
        html += `<div>${i}</div>`;
    }
    
    lineNumbers.innerHTML = html;
}

// Обновление нумерации строк при скролле
updateLineNumbers();
inputText.addEventListener('scroll', () => {
    lineNumbers.scrollTop = inputText.scrollTop;
});

// Автоматическое изменение ширины блока нумерации строк
function updateLineNumbersWidth() {
    const lineCount = inputText.value.split('\n').length;
    const digits = lineCount.toString().length;
    lineNumbers.style.minWidth = `${digits * 12 + 20}px`;
}

// Получить активные режимы вывода
function getActiveOutputModes() {
    const activeButtons = document.querySelectorAll('.output-control-btn.active');
    return Array.from(activeButtons).map(button => button.dataset.outputType);
}

inputText.addEventListener('input', () => {
    const text = inputText.value;
    updateLineNumbers();
    updateLineNumbersWidth();

    fetch('/translate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            text: text,
            output_modes: getActiveOutputModes()
        })
    })
    .then(response => response.json())
    .then(data => {
        outputText.textContent = data.translated;
    })
    .catch(error => {
        console.error('Ошибка:', error);
    });
});

clearButton.addEventListener('click', () => {
    inputText.value = '';
    outputText.textContent = '';
    updateLineNumbers();
});

copyButton.addEventListener('click', () => {
    const textToCopy = outputText.textContent.trim();
    if (textToCopy) {
        const tempTextarea = document.createElement('textarea');
        tempTextarea.value = textToCopy;
        document.body.appendChild(tempTextarea);
        tempTextarea.select();
        try {
            const successful = document.execCommand('copy');
            showToast(successful ? 'Текст скопирован!' : 'Не удалось скопировать текст.');
        } catch (err) {
            showToast('Ошибка копирования: ' + err);
        }
        document.body.removeChild(tempTextarea);
    } else {
        showToast('Нечего копировать!');
    }
});

// Обработка кнопок управления выводом
document.addEventListener('DOMContentLoaded', () => {
    const outputControls = document.querySelectorAll('.output-control-btn');
    
    // Установка normal режима по умолчанию
    const normalButton = document.querySelector('.output-control-btn[data-output-type="normal"]');
    if (normalButton) {
        normalButton.classList.add('active');
    }
    
    outputControls.forEach(button => {
        button.addEventListener('click', () => {
            // Обрабатываем особый случай - кнопки регистра взаимоисключающие
            if (button.dataset.outputType === 'uppercase' || 
                button.dataset.outputType === 'lowercase' ||
                button.dataset.outputType === 'normal') {
                
                outputControls.forEach(btn => {
                    if (btn.dataset.outputType === 'uppercase' || 
                        btn.dataset.outputType === 'lowercase' ||
                        btn.dataset.outputType === 'normal') {
                        btn.classList.remove('active');
                    }
                });
            }
            
            // Переключаем состояние нажатой кнопки
            button.classList.toggle('active');
            
            // Получаем типы вывода и запускаем перевод
            if (inputText.value.trim()) {
                const inputEvent = new Event('input', { bubbles: true });
                inputText.dispatchEvent(inputEvent);
            }
        });
    });
});

// Полноэкранный режим
const fullscreenInputBtn = document.getElementById('fullscreen-input');
const fullscreenOutputBtn = document.getElementById('fullscreen-output');

if (fullscreenInputBtn) {
    fullscreenInputBtn.addEventListener('click', () => {
        const editorPanel = document.querySelector('.editor-panel');
        toggleFullscreen(editorPanel);
    });
}

if (fullscreenOutputBtn) {
    fullscreenOutputBtn.addEventListener('click', () => {
        const outputPanel = document.querySelector('.output-panel');
        toggleFullscreen(outputPanel);
    });
}

function toggleFullscreen(element) {
    if (!document.fullscreenElement) {
        element.requestFullscreen().catch(err => {
            showToast(`Ошибка при переходе в полноэкранный режим: ${err.message}`);
        });
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        }
    }
}

// Обработка клавиши Tab в текстовом поле
inputText.addEventListener('keydown', function(e) {
    if (e.key === 'Tab') {
        e.preventDefault();
        const start = this.selectionStart;
        const end = this.selectionEnd;
        
        this.value = this.value.substring(0, start) + '    ' + this.value.substring(end);
        this.selectionStart = this.selectionEnd = start + 4;
        
        // Запускаем событие input для обновления перевода
        const inputEvent = new Event('input', { bubbles: true });
        this.dispatchEvent(inputEvent);
    }
});

function showToast(message, duration = 3000) {
    const toastContainer = document.querySelector('.toast');
    
    if (!toastContainer) {
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;
    document.body.appendChild(toast);

        setTimeout(() => {
            toast.classList.add('show');
        }, 10);
        
    setTimeout(() => {
        toast.classList.remove('show');
            setTimeout(() => toast.remove(), 500);
        }, duration);
    } else {
        toastContainer.textContent = message;
        toastContainer.classList.add('show');
        
        setTimeout(() => {
            toastContainer.classList.remove('show');
        }, duration);
    }
}

// Автосохранение
const AUTOSAVE_KEY = 'latinizator_autosave';

// Загрузка сохраненного содержимого
function loadSavedContent() {
    const savedContent = localStorage.getItem(AUTOSAVE_KEY);
    if (savedContent) {
        inputText.value = savedContent;
        // Запускаем событие input для обновления перевода
        const inputEvent = new Event('input', { bubbles: true });
        inputText.dispatchEvent(inputEvent);
    }
}

// Настройка автосохранения
function setupAutosave() {
    // Сохранение каждые 5 секунд, если есть содержимое
    setInterval(() => {
        if (inputText.value.trim()) {
            localStorage.setItem(AUTOSAVE_KEY, inputText.value);
        }
    }, 5000);
    
    // Также сохраняем при изменении ввода (с задержкой)
    let saveTimeout;
    inputText.addEventListener('input', () => {
        clearTimeout(saveTimeout);
        saveTimeout = setTimeout(() => {
            localStorage.setItem(AUTOSAVE_KEY, inputText.value);
        }, 1000);
    });
}

// Инициализация
document.addEventListener('DOMContentLoaded', () => {
    loadSavedContent();
    setupAutosave();
    updateLineNumbersWidth();
});
