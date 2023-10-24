let rotations = [ //-13 13
    { x: "0deg", y: "0deg" },  // Front (0,0) -> (-, 13)
    { x: "-450deg", y: "360deg" },  // Top (-90,0) -> (-450, 360)
    { x: "-720deg", y: "-180deg" },  // Back (0,180) -> (-720, -180)
    { x: "-360deg", y: "90deg" },  // Left  (0,90) -> (-360, 90)
    { x: "90deg", y: "-360deg" }, // Bottom  (90,0) -> (-90, -360)
    { x: "-360deg", y: "270deg" } // Right  (0,-90) -> (-360, 270)
    
];

let currentIndex = 0;

document.getElementById("rotateButton").addEventListener("click", function() {
    const cube = document.querySelector(".cube");

    currentIndex++;
    if (currentIndex >= rotations.length) {
        currentIndex = 0; // Reset to the initial state after the last rotation
    }

    let rotation = rotations[currentIndex];
    console.log(rotation.x, rotation.y)
    cube.style.transform = `rotateX(${rotation.x}) rotateY(${rotation.y})`;
});
