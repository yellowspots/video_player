
function createNavbar() {
    const navbarElement = document.getElementById('navbar');
    navbarElement.innerHTML = `
        <div class="bg-pink-500 text-white p-4">
            <div class="container mx-auto flex justify-between items-center">
                <h1 class="text-lg font-bold">Video Platform</h1>
                <nav>
                    <a href="#" class="text-white px-2" onclick="displayVideoList(); return false;">Home</a>
                    <a href="#" class="text-white px-2" onclick="displayThemes(); return false;">Themes</a>
                    <a href="#" class="text-white px-2" onclick="displayRandomJoke(); return false;">Dad Joke</a>
                </nav>
            </div>
        </div>
    `;
}
