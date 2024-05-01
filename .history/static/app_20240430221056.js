// Initialize the application
function initApp() {
    renderNavbar();
    renderThemeSelector();
    renderVideoList();
    renderSearchBar();
    renderJokes();
}

// Call the initApp function when the DOM is loaded
document.addEventListener('DOMContentLoaded', initApp);