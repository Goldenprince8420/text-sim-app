echo "__________________________________________________________________"
echo "Pushing Repository..."
git init
git add LICENSE.txt  README.md  app.py  backend.py  content.py  evaluation.html  git_push.sh  index.html  installer.sh  main.py
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Goldenprince8420/text-sim-app.git
git push -u origin main
echo "done!!"