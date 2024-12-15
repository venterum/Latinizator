const toggleButton = document.getElementById('theme-toggle');
const body = document.body;

toggleButton.addEventListener('click', () => {
    const currentTheme = body.getAttribute('data-theme');
    body.setAttribute('data-theme', currentTheme === 'dark' ? 'light' : 'dark');
});

body.setAttribute('data-theme', 'light');

const inputText = document.getElementById('input-text');
const outputText = document.getElementById('output-text');
const clearButton = document.getElementById('clear-input');
const copyButton = document.getElementById('copy-output');

inputText.addEventListener('input', () => {
    const text = inputText.value;

    fetch('/translate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        outputText.textContent = data.translated;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

clearButton.addEventListener('click', () => {
    inputText.value = '';
    outputText.textContent = '';
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

function showToast(message) {
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;
    document.body.appendChild(toast);

    setTimeout(() => toast.classList.add('show'), 100);
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}
