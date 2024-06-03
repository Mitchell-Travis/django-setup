import os
import subprocess
import sys

def run_command(command):
    try:
        print(f"Running command: {command}")
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running command: {command}")
        print(e)
        sys.exit(1)

def create_project_folder(folder_name):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    project_path = os.path.join(desktop_path, folder_name)
    os.makedirs(project_path, exist_ok=True)
    os.chdir(project_path)
    print(f"Project folder created at {project_path}")
    return project_path

def create_virtualenv(env_name):
    run_command(f'python3 -m venv {env_name}')

def activate_virtualenv(env_name):
    activate_script = os.path.join(env_name, 'bin', 'activate')
    command = f"source {activate_script} && echo 'Virtual environment activated'"
    run_command(command)

def install_django():
    run_command('pip3 install django')  # Use pip3 instead of pip

def create_django_project(project_name):
    run_command(f'django-admin startproject {project_name}')

def create_django_app(project_name, app_name):
    os.chdir(project_name)
    run_command(f'python3 manage.py startapp {app_name}')  # Use python3 instead of python

def init_git():
    run_command('git init')
    run_command('git add .')
    run_command('git commit -m "Initial commit"')

def push_to_github(repo_url):
    run_command(f'git remote add origin {repo_url}')
    run_command(f'git remote set-url origin {repo_url}')
    run_command('git branch -M main')
    run_command('git push -u origin main')



def main():
    folder_name = input("Enter the folder name: ")
    project_name = input("Enter the Django project name: ")
    app_name = input("Enter the Django app name: ")
    repo_url = input("Enter the GitHub repository URL: ")

    # Input validation
    if not all((folder_name, project_name, app_name, repo_url)):
        print("Please provide all the required inputs.")
        sys.exit(1)

    project_path = create_project_folder(folder_name)
    os.chdir(project_path)
    env_name = f"{project_name}_env"
    create_virtualenv(env_name)
    activate_virtualenv(env_name)
    install_django()
    create_django_project(project_name)
    create_django_app(project_name, app_name)
    init_git()
    push_to_github(repo_url)

if __name__ == "__main__":
    main()