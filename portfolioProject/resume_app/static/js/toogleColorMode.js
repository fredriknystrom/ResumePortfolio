
document.getElementById('themeToggle').addEventListener('click', function() {
    const bodyElement = document.body;
    const themeIcon = document.getElementById('themeToggleIcon'); // Make sure this ID matches your icon element

    // Toggle the 'light-mode' class on the body
    bodyElement.classList.toggle('light-mode');

    // Update the icon to reflect the change
    if (bodyElement.classList.contains('light-mode')) {
        themeIcon.className = 'fa fa-tint'; // Change to your light mode icon class
    } else {
        themeIcon.className = 'fa fa-sun-o'; // Change to your default mode icon class
    }
    event.preventDefault();
});
