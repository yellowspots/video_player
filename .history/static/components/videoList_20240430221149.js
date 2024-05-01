async function renderVideoList() {
    const videos = await fetchVideos();
    const mainContent = document.getElementById('main-content');
    mainContent.innerHTML = `
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 m-4">
            ${videos.map(video => `
                <div class="bg-white shadow p-4">
                    <img src="${video.preview_image_url}" alt="${video.title}" class="mb-2">
                    <h3 class="text-lg font-bold mb-2">${video.title}</h3>
                    <p class="text-gray-600">${video.description}</p>
                    <a href="#" class="block mt-4 text-primary hover:text-secondary" onclick="renderVideoDetail(${video.video_id})">View Details</a>
                </div>
            `).join('')}
        </div>
    `;
}

async function fetchVideos() {
    const response = await fetch('/videos');
    const videos = await response.json();
    return videos;
}

function renderVideoDetail(videoId) {
    // Implement video detail rendering logic
}