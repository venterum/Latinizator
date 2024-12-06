const toggleButton = document.getElementById('theme-toggle');
const body = document.body;

toggleButton.addEventListener('click', () => {
    const currentTheme = body.getAttribute('data-theme');
    if (currentTheme === 'dark') {
        body.setAttribute('data-theme', 'light');
    } else {
        body.setAttribute('data-theme', 'dark');
    }
});

body.setAttribute('data-theme', 'light');

const inputText = document.getElementById('input-text');
const outputText = document.getElementById('output-text');

inputText.addEventListener('input', () => {
    const text = inputText.value;

    fetch('/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
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