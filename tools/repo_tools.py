from git import Repo
import os

def clone_repository(repo_url, path="./repos/project"):

    if os.path.exists(path):
        return path

    Repo.clone_from(repo_url, path)

    return path