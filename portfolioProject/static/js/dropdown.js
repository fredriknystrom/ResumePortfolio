$(document).ready(function () {
    // Handle dropdown hover and click
    $('.nav-item.dropdown').hover(function () {
        $(this).find('.dropdown-menu').addClass('show');
    }, function () {
        $(this).find('.dropdown-menu').removeClass('show');
    });

    $('.nav-item.dropdown a.nav-link').click(function (e) {
        var href = $(this).data('href');
        if (href) {
            e.preventDefault();
            window.location.href = href;
        }
    });
});