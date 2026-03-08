import subprocess


def run_tests(repo_path):

    result = subprocess.run(
        ["pytest"],
        cwd=repo_path,
        capture_output=True,
        text=True
    )

    return {
        "return_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr
    }