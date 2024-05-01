async function fetchVideos(theme = null, sort = null) {
    let url = '/videos/';
    if (theme || sort) {
        const params = new URLSearchParams();
        if (theme) params.append('theme_name', theme);
        if (sort) params.append('sort', sort);
        url += `?${params.toString()}`;
    }
    const response = await fetch(url);
    return await response.json();
}

async function fetchVideoById(videoId) {
    const response = await fetch(`/videos/${videoId}`);
    return await response.json();
}

async function fetchRandomVideo() {
    const response = await fetch('/videos/random/');
    return await response.json();
}

async function fetchRandomJoke() {
    const response = await fetch('/jokes/random/');
    return await response.json();
}
