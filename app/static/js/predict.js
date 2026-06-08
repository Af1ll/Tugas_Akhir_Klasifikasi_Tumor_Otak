const predictForm = document.getElementById("predictForm");
const imageInput = document.getElementById("imageInput");
const imagePreview = document.getElementById("imagePreview");
const previewWrapper = document.getElementById("previewWrapper");

const loading = document.getElementById("loading");
const resultWrapper = document.getElementById("resultWrapper");
const errorWrapper = document.getElementById("errorWrapper");

const predictionResult = document.getElementById("predictionResult");
const confidenceResult = document.getElementById("confidenceResult");
const probabilityList = document.getElementById("probabilityList");
const predictButton = document.getElementById("predictButton");


imageInput.addEventListener("change", function () {
    const file = imageInput.files[0];

    if (file) {
        const imageUrl = URL.createObjectURL(file);
        imagePreview.src = imageUrl;
        previewWrapper.classList.remove("d-none");

        resultWrapper.classList.add("d-none");
        errorWrapper.classList.add("d-none");
    }
});


predictForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const file = imageInput.files[0];

    if (!file) {
        showError("Silakan pilih gambar terlebih dahulu.");
        return;
    }

    const formData = new FormData();
    formData.append("img", file);

    loading.classList.remove("d-none");
    resultWrapper.classList.add("d-none");
    errorWrapper.classList.add("d-none");
    predictButton.disabled = true;
    predictButton.innerText = "Memproses...";

    try {
        const response = await fetch("/api/predict", {
            method: "POST",
            body: formData
    });

        const result = await response.json();

    console.log("Response dari API:", result);

    if (!response.ok || result.status !== "berhasil") {
        throw new Error(result.message || "Terjadi kesalahan saat prediksi.");
    }

    showResult(result);

    } catch (error) {
        showError(error.message);
    } finally {
        loading.classList.add("d-none");
        predictButton.disabled = false;
        predictButton.innerText = "Prediksi Sekarang";
    }
});


function showResult(result) {
    const prediction = formatClassName(result.predicted);
    const confidence = (result.confidence * 100).toFixed(2);

    predictionResult.innerText = prediction;
    confidenceResult.innerText = confidence + "%";

    probabilityList.innerHTML = "";

    const probabilities = result.all_probabilities;

    for (const className in probabilities) {
        const percent = (probabilities[className] * 100).toFixed(2);

        const item = document.createElement("div");
        item.className = "mb-3";

        item.innerHTML = `
            <div class="d-flex justify-content-between mb-1">
                <span>${formatClassName(className)}</span>
                <span>${percent}%</span>
            </div>
            <div class="progress">
                <div class="progress-bar" role="progressbar" style="width: ${percent}%"></div>
            </div>
        `;

        probabilityList.appendChild(item);
    }

    resultWrapper.classList.remove("d-none");
}


function showError(message) {
    errorWrapper.innerText = message;
    errorWrapper.classList.remove("d-none");
}


function formatClassName(className) {
    const labels = {
        "glioma": "Glioma",
        "meningioma": "Meningioma",
        "no_tumor": "Normal",
        "pituitary": "Pituitary"
    };

    return labels[className] || className;
}