function generateFakeTerminal() {
    const output = document.getElementById('terminal-output');
    const userInput = prompt("🧠 اكتب سؤالك للذكاء الاصطناعي:");
    if (!userInput) return;

    output.textContent = "⏳ جارٍ المعالجة...";

    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: userInput })
    })
    .then(response => response.json())
    .then(data => {
        output.textContent = data.response || data.error || "❌ فشل في الحصول على رد.";
    })
    .catch(error => {
        output.textContent = "⚠️ خطأ في الاتصال بالخادم.";
        console.error(error);
    });
}