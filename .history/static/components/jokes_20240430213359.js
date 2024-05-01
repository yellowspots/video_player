
async function displayRandomJoke() {
    const joke = await fetchData('/api/jokes/random');
    const jokeSection = document.getElementById('joke-section');
    jokeSection.innerHTML = `<p>${joke.joke_text}</p>`;
}
