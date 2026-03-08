import os

def get_python_files(repo_path):

    files = []

    for root, dirs, filenames in os.walk(repo_path):

        for file in filenames:

            if file.endswith(".py"):

                files.append(os.path.join(root, file))

    return files