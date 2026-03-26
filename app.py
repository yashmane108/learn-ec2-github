from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "App Running 🚀 Testing Todays test nice bro"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
