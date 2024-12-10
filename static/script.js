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
    outputText.textContent = 'Текст на латинице появится здесь.';
});

copyButton.addEventListener('click', () => {
    navigator.clipboard.writeText(outputText.textContent)
        .then(() => alert('Текст скопирован!'))
        .catch(err => alert('Ошибка копирования: ' + err));
});