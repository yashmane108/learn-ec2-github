from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "App Running 🚀 test1 test2 test3 test4"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
