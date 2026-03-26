sudo apt install git 

git init

git add .

git commit -m "initial commit"

git remote add origin https://github.com/yashmane108/learn-ec2-github.git

git push -u origin master

you do some changes in app from server
that file stage change to modified
then run 
git add <filename> or git add .
git commit -m "update app.py"
git push origin master
now on github app.py file update

now do some changes on github and you want to update on ec2 server 
git pull origin master
