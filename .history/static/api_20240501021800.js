async function fetchVideos(theme = null, sort = null) {
    try {
        let url = '/videos/';
        if (theme || sort) {
            const params = new URLSearchParams();
            if (theme) params.append('theme_name', theme);
            if (sort) params.append('sort', sort);
            url += `?${params.toString()}`;
        }
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Failed to fetch videos');
        }
        return await response.json();
    } catch (error) {
        console.error(error);
        // Handle the error here, e.g. show an error message to the user
        throw error; // Rethrow the error to propagate it to the caller
    }
}

async function fetchVideoById(videoId) {
    try {
        const response = await fetch(`/videos/${videoId}`);
        if (!response.ok) {
            throw new Error('Failed to fetch video by ID');
        }
        return await response.json();
    } catch (error) {
        console.error(error);
        throw error;
    }
}

async function fetchRandomVideo() {
    try {
        const response = await fetch('/videos/random/');
        if (!response.ok) {
            throw new Error('Failed to fetch random video');
        }
        return await response.json();
    } catch (error) {
        console.error(error);
        throw error;
    }
}

async function fetchRandomJoke() {
    try {
        const response = await fetch('/jokes/random/');
        if (!response.ok) {
            throw new Error('Failed to fetch random joke');
        }
        return await response.json();
    } catch (error) {
        console.error(error);
        throw error;
    }
}
