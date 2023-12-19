$(document).ready(function() {
    $(".hover-card").hover(
        function() {
            // Mouse over - add the hover effect
            $(this).css("transform", "scale(1.02)");
        },
        function() {
            // Mouse out - remove the hover effect
            $(this).css("transform", "scale(1)");
        });

    // Attach a click event to the addToCartButton
    $(".addToCartButton").click(function() {
        // Get the URL from the 'data-url' attribute of the button
        var cartUrl = $(this).data('url');

        // Redirect to the cart page
        window.location.href = cartUrl;
    });

    // Attach a click event to the signup button
    $(".signupButton").click(function() {
        // Get the URL from the 'data-url' attribute of the button
        var registerUrl = $(this).data('url');

        // Redirect to the register section on the home page
        window.location.href = registerUrl + "#register";
    });
});
