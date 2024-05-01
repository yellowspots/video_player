// components/videoDetail.js
async function displayVideoDetail(videoId) {
    const video = await fetchData(`/api/videos/${videoId}`);
    const mainContent = document.getElementById('main-content');
    mainContent.innerHTML = `
        <h1>${video.title}</h1>
        <img src="${video.preview_image_url}" alt="${video.title}">
        <p>${video.description}</p>
        <p>Views: ${video.view_count}</p>
        <p>Rating: ${video.user_rating}/5</p>
    `;
}
