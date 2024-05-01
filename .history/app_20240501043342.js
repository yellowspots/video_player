window.onload = function() {
    fetchVideos();

    document.getElementById('searchInput').addEventListener('keyup', function(event) {
        fetchVideos(event.target.value);
    });
};

function fetchVideos(searchQuery = '') {
    fetch(`/videos/?search_query=${encodeURIComponent(searchQuery)}`)
        .then(response => response.json())
        .then(videos => displayVideos(videos))
        .catch(error => console.error('Error fetching videos:', error));
}

function displayVideos(videos) {
    const videoList = document.getElementById('videoList');
    videoList.innerHTML = videos.map(video => `
        <div class="col-md-4 mb-3">
            <div class="card">
                <img src="${video.preview_image_url}" class="card-img-top" alt="Thumbnail">
                <div class="card-body">
                    <h5 class="card-title">${video.title}</h5>
                    <p class="card-text">${video.description}</p>
                    <a href="#" class="btn btn-primary">Watch</a>
                </div>
            </div>
        </div>
    `).join('');
}
// ... (existing JavaScript code) ...

function displayVideoList(videos) {
    const videoList = document.getElementById('videoList');
    videoList.innerHTML = '';

    videos.forEach(video => {
        const videoElement = document.createElement('div');
        videoElement.className = 'col-md-4 mb-3';
        videoElement.innerHTML = `
            <div class="card">
                <img src="${video.preview_image_url}" class="card-img-top" alt="${video.title}">
                <div class="card-body">
                    <h5 class="card-title">${video.title}</h5>
                    <p class="card-text">${video.description}</p>
                    <button class="btn btn-primary play-video" data-video-url="${video.video_url}">Play</button>
                </div>
            </div>
        `;
        videoList.appendChild(videoElement);
    });

    // Add event listener to play video buttons
    const playButtons = document.querySelectorAll('.play-video');
    playButtons.forEach(button => {
        button.addEventListener('click', () => {
            const videoUrl = button.getAttribute('data-video-url');
            playVideo(videoUrl);
        });
    });
}

function playVideo(videoUrl) {
    const player = document.getElementById('player');
    player.src = videoUrl;
    player.play();
}

