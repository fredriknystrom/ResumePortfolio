$(document).ready(function() {
    $('#navbarNav .nav-link').on('click', function(e) {
        // Check if window width is less than or equal to 992px
        if($(window).width() <= 992) {
            // Prevent the default behavior of anchor links
            e.preventDefault();

            // Store the href attribute (the ID of the target section)
            var targetSection = $(this).attr('href');

            // Collapse the navbar
            $('#navbarNav').collapse('hide');

            // After navbar is collapsed, smoothly scroll to the target section
            $('#navbarNav').on('hidden.bs.collapse', function() {
                $('html, body').animate({
                    scrollTop: $(targetSection).offset().top
                }, 20); // 20 ms animation speed
            });
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const typeString = 'Hello, my name is Fredrik!';
    let i = 0;
    console.log(typeString)
    const typeWriter = () => {
        if (i < typeString.length) {
            document.querySelector('.hello-header').textContent += typeString.charAt(i);
            i++;
            setTimeout(typeWriter, 100);  // Adjust the typing speed by changing the timeout value.
        } else {
            // Remove the typing class to stop the cursor from blinking after typing is complete.
            document.querySelector('.hello-header').classList.remove('typing');
        }
    };

    // Start the typewriter effect
    typeWriter();
});
