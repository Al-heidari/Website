async function processAES(action) {
    const text = document.getElementById('inputText').value;
    const key = document.getElementById('key').value;
    const keySize = window.selectedKeySize || 128; // Default to 128-bit if none selected

    try {
        const response = await fetch('http://127.0.0.1:5000/aes', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text, key, keySize, action })
        });

        const result = await response.json();
        document.getElementById('outputText').value = result.output;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById('outputText').value = "An error occurred.";
    }
}
