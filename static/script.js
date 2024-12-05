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