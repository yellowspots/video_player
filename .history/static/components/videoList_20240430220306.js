async function displayVideoList() {
    try {
      const response = await fetch('/api/videos');
      const videos = await response.json();
  
      if (Array.isArray(videos)) {
        const mainContent = document.getElementById('main-content');
        mainContent.innerHTML = videos.map(video => `
          <div class="p-4 border border-gray-200">
            <img src="${video.preview_image_url}" alt="${video.title}" class="w-full">
            <h2 class="text-lg font-bold">${video.title}</h2>
            <p>${video.description}</p>
            <button onclick="displayVideoDetail(${video.video_id})">View Details</button>
          </div>
        `).join('');
      } else {
        console.error('Invalid response format. Expected an array of videos.');
      }
    } catch (error) {
      console.error('Error fetching videos:', error);
    }
  }
  
  function displayVideoDetail(videoId) {
    // Implementation needed for showing video details
    console.log("Displaying details for video:", videoId);
  }