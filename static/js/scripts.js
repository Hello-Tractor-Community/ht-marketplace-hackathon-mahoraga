document.querySelector('button').addEventListener('click', () => {
    alert('Learn more about JCB Backhoe Loaders!');
});
console.log("Dashboard loaded successfully.");

//document.addEventListener('DOMContentLoaded', function () {
//    const menuBtn = document.getElementById('menu-btn');
//    const sidebar = document.getElementById('sidebar');
//
//    menuBtn.addEventListener('click', () => {
//        sidebar.classList.toggle('active');
//    });
//});


// Ensure the DOM is fully loaded before running the script
document.addEventListener('DOMContentLoaded', function () {
    // Select the menu button and the sidebar
    const menuBtn = document.getElementById('menu-btn');
    const sidebar = document.getElementById('sidebar');

    // Check if both elements exist to avoid runtime errors
    if (menuBtn && sidebar) {
        // Add a click event to toggle the sidebar's visibility
        menuBtn.addEventListener('click', function () {
            sidebar.classList.toggle('hidden'); // Use 'hidden' or 'active' class based on your CSS
        });
    } else {
        console.error('menu-btn or sidebar not found in the DOM.');
    }
});

