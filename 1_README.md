1. Create a git repo 'mlproject'
2. Install Anaconda
3. create a dir 'c:/1_ML_YOUTUBE-VS"
4. Open Anaconda CMD prompt
5. cd to dir 'c:/1_ML_YOUTUBE-VS"
6. type in command to open vscode - 'code .'
7. create environment:
   - open cmd terminal on the project in vsacode
   - enter command:  'conda create -p venv python==3.8 -y'
     This will create environment with name 'venv' and install dependency packages inside the root project
   - 'conda activate C:\Rohit\vscode-codes\1_ml-youtube-vs\venv'
     CMD terminal will show environment instead of 'base'.
8. Save to git:
   - git init
   - git add README.md
   - git commit -m "first commit"
   - git branch -M main
   - git push -u origin main
   - git remote -v, git config --global user.email ( TO SET -> git config --global user.  email "rohit.tew@gmail.com")
   - add '.gitignore' file in github ui of python type. (will have 'venv')
   - do 'git pull' in the terminal






