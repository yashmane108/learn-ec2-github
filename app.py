from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "App Running 🚀 test1"

@app.route('/deploy')
def deploy():
    os.system("bash /home/ec2-user/cicd/deploy.sh")
    return "Deployment Triggered changes in github 2nd time"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
