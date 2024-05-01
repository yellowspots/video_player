function renderNavbar() {
    const navbarElement = document.getElementById('navbar');
    navbarElement.innerHTML = `
      <nav class="bg-primary text-white p-4">
        <ul class="flex space-x-4">
          <li><a href="#" class="hover:text-secondary">Home</a></li>
          <li><a href="#" class="hover:text-secondary">Themes</a></li>
          <li><a href="#" class="hover:text-secondary">Search</a></li>
        </ul>
      </nav>
    `;
  }