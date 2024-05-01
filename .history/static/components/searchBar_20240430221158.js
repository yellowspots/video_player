function renderSearchBar() {
    const mainContent = document.getElementById('main-content');
    mainContent.innerHTML = `
      <div class="m-4">
        <input type="text" id="search-input" class="border border-gray-300 p-2 w-full" placeholder="Search videos...">
        <button id="search-button" class="bg-primary text-white p-2 mt-2">Search</button>
      </div>
    `;
    
    const searchButton = document.getElementById('search-button');
    searchButton.addEventListener('click', performSearch);
  }
  
  function performSearch() {
    const searchTerm = document.getElementById('search-input').value;
    // Implement search logic using the searchTerm
  }