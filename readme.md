+ Github

1. Create a new repository on the command line

echo "# empty" >> README.md

git init

git add README.md

git commit -m "first commit"

git branch -M main

git remote add origin https://github.com/VitaminPC/empty.git

git push -u origin main

2. Push an existing repository from the command line

git remote add origin https://github.com/VitaminPC/empty.git

git branch -M main

git push -u origin main


+ Python

1. Init virtual env  
python -m venv .folder
python -m cProfile -s time pract4.py 100001 - узнать какие строки кода сколько по времени выполняются  (1001- количество итераций)