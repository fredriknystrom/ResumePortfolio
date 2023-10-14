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
                    scrollTop: $(targetSection).offset().top - 105
                }, 20); // 20 ms animation speed
            });
        }
    });
});

