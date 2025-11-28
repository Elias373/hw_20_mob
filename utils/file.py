import os

def abs_path_from_project(relative_path: str):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../..', relative_path)
    )

def path_from_project(relative_path: str):
    return os.path.join(os.path.dirname(__file__), '../..', relative_path)