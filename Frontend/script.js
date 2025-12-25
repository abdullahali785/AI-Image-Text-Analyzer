const imageInput = document.getElementById("imageInput");
const analyzeBtn = document.getElementById("analyzeBtn");
const loading = document.getElementById("loading");
const result = document.getElementById("result");
const extractedText = document.getElementById("extractedText");
const explanation = document.getElementById("explanation");

analyzeBtn.addEventListener("click", async () => {
    if (!imageInput.files.length) return;

    result.classList.add("d-none");
    loading.classList.remove("d-none");

    const formData = new FormData();
    formData.append("file", imageInput.files[0]);

    try {
        const response = await fetch("http://127.0.0.1:8000/analyze", {
            method: "POST",
            body: formData,
        });

        const data = await response.json();

        extractedText.textContent = data.extracted_text;
        explanation.textContent = data.explanation;

        result.classList.remove("d-none");
    } catch (err) {
        alert("Failed to analyze image");
    }

    loading.classList.add("d-none");
});
