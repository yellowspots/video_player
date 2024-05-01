async function renderJokes() {
    const joke = await fetchRandomJoke();
    const jokeSection = document.getElementById('joke-section');
    jokeSection.innerHTML = `
      <div class="bg-secondary text-white p-4 mt-8">
        <h3 class="text-lg font-bold mb-2">Dad Joke of the Day</h3>
        <p>${joke.joke_text}</p>
      </div>
    `;
  }
  
  async function fetchRandomJoke() {
    const response = await fetch('/jokes/random');
    const joke = await response.json();
    return joke;
  }