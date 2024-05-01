async function renderThemeSelector() {
    const themes = await fetchThemes();
    const mainContent = document.getElementById('main-content');
    mainContent.innerHTML = `
        <div class="m-4">
            <label for="theme-select" class="block mb-2">Select a theme:</label>
            <select id="theme-select" class="border border-gray-300 p-2">
                ${themes.map(theme => `<option value="${theme.theme_name}">${theme.theme_name}</option>`).join('')}
            </select>
        </div>
    `;
}

async function fetchThemes() {
    const response = await fetch('/themes');
    const themes = await response.json();
    return themes;
}