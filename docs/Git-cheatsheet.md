# Git & Bash Cheatsheet

## Bash intro

### access CLI with : 
git bash
/ is root and ~ is home
pwd - list directories 
cd - change directory (ex: cd R, cd .., cd)
ls - list files in current directory (ex: ls -a, ls -al)
mkdir - create directory
touch - create empty file
cp - copy file (ex: cp file where, cp -r directory where)
re - remove (ex:rm file, rm -r directory)
mv - move (ex: mv file where)
mv - rename (ex: mv file new_name)
echo - print text
date - print current date


## Git intro

### initial setup:
git config --global user.name "mendelevium"
git config --global user.email "mendelevium@gmail.com"
git config --list
exit

### create repo:
mkdir ~/test-repo
cd ~/test-repo
git init
git remote add origin http://github.com/mendelevium/test-repo.git/

### fork repo:
to clone in the current directory:
git clone https://github.com/mendelevium/test-repo.git/

### basic cmd:
git add . (add all files to index)
git add -u (update)
git add -A (both previous)
git commit -m “message” (commit to local repo)
git push -u origin master (send to Github)
git checkout -b branchname (create branch)
git branch (return actual branch name) 
git checkout master (switch back to master ranch)
