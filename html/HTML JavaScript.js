// HTML JavaScript.js
// This file explains how to use JavaScript in HTML and provides a simple example.

// To use JavaScript in HTML, include a <script> tag:
// <script src="HTML JavaScript.js"></script>

// Example: Show an alert when the page loads
window.onload = function() {
    // Uncomment the next line to see an alert when the page loads
    // alert('Welcome to the HTML Explanation Website!');
};

// Example: Add interactivity
document.addEventListener('DOMContentLoaded', function() {
    var nav = document.querySelector('nav');
    if(nav) {
        nav.addEventListener('click', function() {
            console.log('Navigation clicked!');
        });
    }
});
