// components/themeSelector.js
async function displayThemes() {
    const themes = await fetchData('/api/themes');
    const mainContent = document.getElementById('main-content');
    mainContent.innerHTML = `<select onchange="filterVideosByTheme(this.value)">
        ${themes.map(theme => `<option value="${theme.theme_id}">${theme.theme_name}</option>`).join('')}
    </select>`;
}

function filterVideosByTheme(themeId) {
    // Implementation needed to filter videos based on selected theme
    console.log("Filtering videos for theme:", themeId);
}
