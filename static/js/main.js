// Ensure the script runs once the entire page (DOM) is loaded
$(document).ready(function() {
    
    // Attach an event handler to the form's submit event
    $('#registrationForm').on('submit', function(e) {
        
        let isValid = true; // Flag to track overall form validity
        
        // --- 1. Empty Field Validation (e.g., Username) ---
        const username = $('#username').val().trim();
        if (username === '') {
            $('#username').addClass('is-invalid'); // Add Bootstrap's error class
            isValid = false;
        } else {
            $('#username').removeClass('is-invalid');
        }

        // --- 2. Password Strength Validation (Example) ---
        const password = $('#password').val();
        if (password.length < 8) {
            $('#password').addClass('is-invalid');
            // Small UI effect: Flash a message
            $('#passwordHelp').text('Password is too weak (min 8 chars).').css('color', 'red').fadeOut(100).fadeIn(400);
            isValid = false;
        } else {
            $('#password').removeClass('is-invalid');
            $('#passwordHelp').text('Must be at least 8 characters.').css('color', 'muted');
        }

        // --- 3. Prevent submission if validation failed ---
        if (!isValid) {
            e.preventDefault(); // Stop the form from submitting to the server
            // Optional: Show a general confirmation message or alert
            console.log("Frontend validation failed. Check fields.");
        }
        
        // If 'isValid' is true, the form will submit normally to the Flask route.
    });

});