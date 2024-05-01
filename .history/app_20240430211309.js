
document.addEventListener('DOMContentLoaded', function() {
    loadNavbar();
    loadMainContent();
    displayRandomJoke();  // Load a random joke at the footer
});

function loadNavbar() {
    createNavbar();  // This function is defined in navbar.js
}

function loadMainContent() {
    displayVideoList();  // Initially load the list of videos
}

function displayThemes() {
    // This function needs to be implemented to show theme selector and filtered videos
    console.error("Theme display not implemented");
}

function displayRandomJoke() {
    // This function is defined in jokes.js
    displayRandomJoke();  
}

// Additional functions to handle navigation and content loading dynamically
window.displayVideoDetail = function(videoId) {
    // Function to load video details view
    displayVideoDetail(videoId);  // Defined in videoDetail.js
}

window.displayVideoList = function() {
    // Function to go back to the video list view
    displayVideoList();  // Defined in videoList.js
}

window.displayThemes = function() {
    // Load theme selection and video list based on selected theme
    displayThemes();  // Defined in themeSelector.js
}
