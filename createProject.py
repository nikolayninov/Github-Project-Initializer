import sys
import os
from github import Github  # pip install PyGithub

# Your Github access token
ACCESS_TOKEN = "[TOKEN]"
# Path to the folder where you want to create your projects
PROJECTS_FOLDER = '[PATH]'

OS = sys.platform

project_name = sys.argv[1]
g = Github(ACCESS_TOKEN)
repo = g.get_user().create_repo(project_name)
git_url = f'https://{repo.git_url[6:]}'

# Changing directory to the projets folder
os.chdir(PROJECTS_FOLDER)
# Cloning the repo
os.system(f'git clone {git_url}')
# Changing directory to the repo's folder
os.chdir(repo.name)
# Creating README.md
if OS.startswith('win'):
    os.system('type nul > README.md')
elif OS.startswith('linux') or OS.startswith('darwin'):
    os.system('touch README.md')

os.system('git add .')
os.system('git commit -m "Initial commit"')
os.system('git push -u origin master')

# This line opens the folder of the project with VS Code (You can change it if you want)
os.system('code .')
