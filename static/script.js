document.addEventListener('DOMContentLoaded', () => {
    const inputText = document.getElementById('input-text');
    const inputTextEn = document.getElementById('input-text-en');
    const outputText = document.getElementById('output-text');
    const clearButton = document.getElementById('clear-input');
    const copyButton = document.getElementById('copy-output');
    const toast = document.querySelector('.toast');
    const terminal = document.querySelector('.terminal');
    const terminalHeader = document.querySelector('.terminal-header');

    // Theme and Language Handling
    const themeToggle = document.querySelector('.theme-toggle');
    const langButtons = document.querySelectorAll('.lang-btn');
    const textRu = document.querySelectorAll('.text-ru');
    const textEn = document.querySelectorAll('.text-en');

    themeToggle.addEventListener('click', () => {
        const currentTheme = document.body.className === 'theme-default' ? 'light' : 'default';
        document.body.className = `theme-${currentTheme}`;
        localStorage.setItem('theme', currentTheme);
        document.cookie = `theme=${currentTheme}; path=/; max-age=31536000`;
    });

    langButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const lang = btn.dataset.lang;
            langButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            if (lang === 'en') {
                textRu.forEach(el => el.style.display = 'none');
                textEn.forEach(el => el.style.display = 'block');
                inputTextEn.value = inputText.value; // Sync text
            } else {
                textRu.forEach(el => el.style.display = 'block');
                textEn.forEach(el => el.style.display = 'none');
                inputText.value = inputTextEn.value; // Sync text
            }
            localStorage.setItem('lang', lang);
        });
    });

    // Load saved theme and language
    const savedTheme = localStorage.getItem('theme') || 'default';
    const savedLang = localStorage.getItem('lang') || 'ru';
    document.body.className = `theme-${savedTheme}`;
    document.querySelector(`[data-lang="${savedLang}"]`).click();

    // Latinizator Functionality
    function updateOutput(text) {
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
    }

    inputText.addEventListener('input', () => {
        inputTextEn.value = inputText.value; // Sync text
        updateOutput(inputText.value);
    });

    inputTextEn.addEventListener('input', () => {
        inputText.value = inputTextEn.value; // Sync text
        updateOutput(inputTextEn.value);
    });

    clearButton.addEventListener('click', () => {
        inputText.value = '';
        inputTextEn.value = '';
        outputText.textContent = '';
    });

    copyButton.addEventListener('click', () => {
        const textToCopy = outputText.textContent.trim();
        if (textToCopy) {
            navigator.clipboard.writeText(textToCopy)
                .then(() => showToast('Текст скопирован!', 'Text copied!'))
                .catch(err => showToast('Ошибка копирования: ' + err, 'Copy error: ' + err));
        } else {
            showToast('Нечего копировать!', 'Nothing to copy!');
        }
    });

    function showToast(ru, en) {
        const lang = localStorage.getItem('lang') || 'ru';
        toast.textContent = lang === 'en' ? en : ru;
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 3000);
    }

    // Drag Functionality
    let isDragging = false;
    let currentX, currentY, initialX, initialY, xOffset = 0, yOffset = 0;

    terminalHeader.addEventListener('mousedown', dragStart);
    document.addEventListener('mousemove', drag);
    document.addEventListener('mouseup', dragEnd);

    function dragStart(e) {
        initialX = e.clientX - xOffset;
        initialY = e.clientY - yOffset;
        if (e.target === terminalHeader) {
            isDragging = true;
        }
    }

    function drag(e) {
        if (!isDragging) return;
        e.preventDefault();
        currentX = e.clientX - initialX;
        currentY = e.clientY - initialY;
        xOffset = currentX;
        yOffset = currentY;
        terminal.style.transform = `translate(${currentX}px, ${currentY}px)`;
    }

    function dragEnd() {
        isDragging = false;
    }
});