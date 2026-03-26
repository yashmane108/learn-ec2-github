from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "App Running 🚀 test1 test2 test3 test4 test5 test6 test7 test8 test9(user bash in bg) test 10 tet749861491 egFei"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
