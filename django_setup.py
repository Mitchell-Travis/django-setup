import os
import subprocess
import sys

def run_command(command):
    """Run a command in the shell."""
    try:
        print(f"Running command: {command}")
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running command: {command}")
        print(e)
        sys.exit(1)

def create_project_folder(folder_name):
    """Create a folder for the Django project."""
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    project_path = os.path.join(desktop_path, folder_name)
    os.makedirs(project_path, exist_ok=True)
    os.chdir(project_path)
    print(f"Project folder created at {project_path}")
    return project_path

def create_virtualenv(env_name):
    """Create a virtual environment for the project."""
    run_command(f'python3 -m venv {env_name}')

def activate_virtualenv(env_name):
    """Activate the virtual environment."""
    activate_script = os.path.join(env_name, 'bin', 'activate')
    command = f"source {activate_script} && echo 'Virtual environment activated'"
    run_command(command)

def install_django():
    """Install Django in the virtual environment."""
    run_command('pip3 install django')

def create_django_project(project_name):
    """Create a new Django project."""
    run_command(f'django-admin startproject {project_name}')

def create_django_app(project_name, app_name):
    """Create a new Django app within the project."""
    os.chdir(project_name)
    run_command(f'python3 manage.py startapp {app_name}')

def init_git():
    """Initialize a Git repository for version control."""
    run_command('git init')
    run_command('git add .')
    run_command('git commit -m "Initial commit"')

def push_to_github(repo_url):
    """Push the project to a GitHub repository."""
    run_command(f'git remote add origin {repo_url}')
    run_command(f'git remote set-url origin {repo_url}')
    run_command('git branch -M main')
    run_command('git push -u origin main')

def main():
    """Main function to orchestrate the setup process."""
    # Get user input
    folder_name = input("Enter the folder name: ")
    project_name = input("Enter the Django project name: ")
    app_name = input("Enter the Django app name: ")
    repo_url = input("Enter the GitHub repository URL: ")

    # Input validation
    if not all((folder_name, project_name, app_name, repo_url)):
        print("Please provide all the required inputs.")
        sys.exit(1)

    # Create project folder
    project_path = create_project_folder(folder_name)
    os.chdir(project_path)

    # Set up virtual environment
    env_name = f"{project_name}_env"
    create_virtualenv(env_name)
    activate_virtualenv(env_name)

    # Install Django and create project/app
    install_django()
    create_django_project(project_name)
    create_django_app(project_name, app_name)

    # Initialize Git repository and push to GitHub
    init_git()
    push_to_github(repo_url)

if __name__ == "__main__":
    main()
