let rotations = [
    { x: "-450deg", y: "360deg" }, // Top (-450,360)
    { x: "-720deg", y: "-180deg" },// Back (-720,-180)
    { x: "-360deg", y: "90deg" },  // Left (-360,90)
    { x: "90deg", y: "-360deg" },  // Bottom (90,-360)
    { x: "-360deg", y: "270deg" },  // Right (-360,270)
    { x: "0deg", y: "0deg" },      // Front (0,0)
];

let titles = [
    "Machine Learning",
    "Neural Networks",
    "NLP & LLMs",
    "Computer Vision",
    "Robotics",
    "Foundations of AI",
]

let currentIndex = 0;

function rotateCube() {
    const cube = document.querySelector(".cube");
    const title = document.querySelector(".my-header");

    title.textContent = ""; // Change the title's text

    let rotation = rotations[currentIndex];
    let new_title = titles[currentIndex];
    console.log(rotation.x, rotation.y)
    cube.style.transform = `rotateX(${rotation.x}) rotateY(${rotation.y})`;

    currentIndex++;
    if (currentIndex >= rotations.length) {
        currentIndex = 0; // Reset to the initial state after the last rotation
    }

    setTimeout(function() {
        title.textContent = new_title // Change the title's text
    }, 1500);
}

document.getElementById("rotateButton").addEventListener("click", rotateCube);

document.addEventListener("keydown", function(event) {
    if (event.key === " ") { // Spacebar
        rotateCube();
        event.preventDefault(); // Prevent the default spacebar behavior (e.g., scrolling)
    }
});
