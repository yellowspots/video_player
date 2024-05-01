from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="/Users/gene/thought_arc/static"), name="static")
