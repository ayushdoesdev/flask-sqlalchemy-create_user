from app_init import app


@app.route("/")
def index():
    return {
        "message": "Hello World 2!"
    }