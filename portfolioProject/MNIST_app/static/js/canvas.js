const canvas = document.getElementById('drawingCanvas');
const context = canvas.getContext('2d');
let imageData = context.getImageData(0, 0, canvas.width, canvas.height);
let drawing = false;

canvas.addEventListener('mousedown', () => {
    drawing = true;
});

canvas.addEventListener('mouseup', () => {
    drawing = false;
    context.beginPath();
    imageData = context.getImageData(0, 0, canvas.width, canvas.height);
});

canvas.addEventListener('mousemove', (e) => {
    if (!drawing) return;
    draw(e.clientX - canvas.getBoundingClientRect().left, e.clientY - canvas.getBoundingClientRect().top);
});

function draw(x, y) {
    context.lineWidth = 30;
    context.lineCap = 'round';
    context.strokeStyle = 'black';
    context.lineTo(x, y);
    context.stroke();
    context.beginPath();
    context.moveTo(x, y);
}

function convertDataToMatrix(imageData) {
    const matrix = [];

    // Loop through the image data and create a 2D matrix
    for (let y = 0; y < imageData.height; y++) {
        const row = [];
        for (let x = 0; x < imageData.width; x++) {
            const index = (y * imageData.width + x) * 4;
            const pixelValue = imageData.data[index+3]; // this is used dont care about other
            const g = imageData.data[index + 1];
            const b = imageData.data[index + 2];

            // Apply sRGB gamma correction
            //const gammaCorrectedR = Math.pow(r / 255, 2.2);
            const gammaCorrectedG = Math.pow(g / 255, 2.2);
            const gammaCorrectedB = Math.pow(b / 255, 2.2);

            // Calculate grayscale value using gamma-corrected values
            //const grayscale = (gammaCorrectedR + gammaCorrectedG + gammaCorrectedB) / 3;

            row.push(pixelValue);
        }
        matrix.push(row);
    }

    return matrix;
}

function checkIfAllZeros(matrixData) {
    return matrixData.every(row => row.every(element => element === 0));
}

function sendToServer(matrixData) {
    // Get the CSRF token from the page's cookie
    if (!checkIfAllZeros(matrixData)) {
        const csrfToken = getCookie('csrftoken');

        // Convert the matrix data to JSON
        const jsonData = JSON.stringify({ pixel_data: matrixData });

        // Make a POST request to your Django server with the CSRF token included
        fetch('/mnist/', {
            method: 'POST',
            body: jsonData,
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken, // Include the CSRF token in the headers
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            const predictionResult = document.getElementById('predictionResult');
            predictionResult.innerHTML = `Predicted Number: ${data.prediction}`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    
    }
    else {
        console.log("Empty Canvas!")
    }

}

// Function to get the CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const guessButton = document.getElementById('guessButton');
guessButton.addEventListener('click', () => {
    data_matrix = convertDataToMatrix(imageData)

    console.log(data_matrix);

    // Send the data matrix to the server
    sendToServer(data_matrix);
});

const clearButton = document.getElementById('clearButton');
clearButton.addEventListener('click', () => {
    // Clear the canvas
    context.clearRect(0, 0, canvas.width, canvas.height);
    // Reset the image data to a blank image
    imageData = context.getImageData(0, 0, canvas.width, canvas.height);
});
