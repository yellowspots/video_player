document.addEventListener("DOMContentLoaded", () => {
    loadFrontPage();
});

async function loadFrontPage() {
    const videos = await fetchVideos();
    renderVideos(videos, "All Videos");
}

function renderVideos(videos, title) {
    const container = document.getElementById('content');
    container.innerHTML = `
        <h2 class="text-2xl font-bold mb-4">${title}</h2>
        <div>${videos.map(video => `
            <div onclick="loadDetailView(${video.video_id})" class="p-4 hover:bg-pink-200 cursor-pointer">
                <img src="${video.preview_image_url}" alt="${video.title}" class="w-32 h-20">
                <div class="text-lg">${video.title}</div>
            </div>
        `).join('')}</div>
    `;
}

async function loadDetailView(videoId) {
    const video = await fetchVideoById(videoId);
    const container = document.getElementById('content');
    container.innerHTML = `
        <h2 class="text-2xl font-bold mb-4">${video.title}</h2>
        <img src="${video.preview_image_url}" alt="${video.title}" class="w-full max-w-4xl">
        <p>${video.description}</p>
        <button onclick="loadFrontPage()" class="mt-4 px-4 py-2 bg-pink-500 text-white">Back to List</button>
    `;
}

async function loadFilteredView(theme) {
    const videos = await fetchVideos(theme);
    renderVideos(videos, `Filtered Videos: ${theme}`);
}

async function showRandomJoke() {
    const joke = await fetchRandomJoke();
    alert(joke.joke_text);
}
