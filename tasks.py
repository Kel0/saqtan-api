import invoke

from pathlib import Path

import glob
import sys, os
import json
import datetime

REQUIRED_COVERAGE = 90


@invoke.task(help={"python": "Install required packages"})
def install(arg):
    arg.run("pip install -r requirements.txt")


@invoke.task(name="format")
def format_(arg):
    with open("apps.txt", "r") as file:
        data = file.readlines()
        data = [json.loads(element)["app_name"] for element in data]
    apps = " ".join(app for app in data)
    autoflake = "autoflake -i --recursive --remove-all-unused-imports --remove-duplicate-keys --remove-unused-variables"
    arg.run(f"{autoflake} {apps}", echo=True)
    arg.run(f"isort --recursive {apps}", echo=True)
    arg.run(f"black {apps}", echo=True)


@invoke.task(
    help={
        "style": "Check style with flake8, isort, and black",
        "typing": "Check typing with mypy",
    }
)
def check(arg, style=True, typing=True):
    with open("apps.txt", "r") as file:
        data = file.readlines()
        data = [json.loads(element)["app_name"] for element in data]
    apps = " ".join(app for app in data)
    if style:
        arg.run(f"flake8 --exclude=poka {apps}", echo=True)
        arg.run(f"isort --diff --recursive {apps} --check-only", echo=True)
        arg.run(f"black --diff {apps} --check", echo=True)
    if typing:
        arg.run(f"mypy --no-incremental --cache-dir=/dev/null {apps}", echo=True)


@invoke.task
def test(arg):
    with open("apps.txt", "r") as file:
        data = file.readlines()
        data = [json.loads(element)["app_name"] for element in data]
    apps = " ".join(app for app in data)
    arg.run(
        f"pytest --cov={apps} --cov-fail-under={REQUIRED_COVERAGE} --cov-report term-missing",
        pty=True,
        echo=True,
    )


@invoke.task
def poka(arg):
    arg.run("git clone https://github.com/whoamTati/poka.git")


@invoke.task
def create(arg, app):
    arg.run(f"mkdir ./{app}")
    arg.run(f"touch ./{app}/__init__.py")
    now_time = datetime.datetime.utcnow()
    with open("apps.txt", "a+") as file:
        print(
            json.dumps({"app_name": app, "created_at": str(now_time)}),
            file=file
        )


@invoke.task(name="packmodels")
def pack_models(arg, dirname="models"):
    base_dir: str = os.path.dirname(os.path.realpath(__file__))
    path_to_dir: list = [x[0] for x in os.walk(base_dir) if x[0].split("/")[-1] == "models"]  # Find path to models dir

    all_files_of_models_dir: list = list(glob.glob(f"{path_to_dir[0]}/*"))  # Get all files
    all_py_files_of_models_dir: list = list(glob.glob(f"{path_to_dir[0]}/*.py"))  # Get all files

    if f"{path_to_dir[0]}/cache" in all_files_of_models_dir:  # if pack_models already exists
        pack_models_file_path: str = f"{path_to_dir[0]}/cache/pack_models.py"  # Set pack_models file path
    else:
        arg.run(f"mkdir {path_to_dir[0]}/cache")
        arg.run(f"touch {path_to_dir[0]}/cache/pack_models.py && touch {path_to_dir[0]}/cache/__init__.py")
        pack_models_file_path: str = f"{path_to_dir[0]}/cache/pack_models.py"

    models: list = [
        model.split("/")[-1][:-3] for model in all_py_files_of_models_dir
        if (model.split("/")[-1] != "__init__.py")
    ]
    
    with open(pack_models_file_path, "a+") as file:
        model: str
        file.truncate(0)
        file.write("# mypy: ignore-errors\n")

        for model in models:
            file.write(f"from .. import {model}  # noqa: F841,F401\n")


@invoke.task(name="packschemas")
def pack_schemas(arg, dirname="schemas"):
    base_dir: str = os.path.dirname(os.path.realpath(__file__))
    path_to_dir: list = [x[0] for x in os.walk(base_dir) if x[0].split("/")[-1] == "schemas"]  # Find path to models dir

    all_files_of_schemas_dir: list = list(glob.glob(f"{path_to_dir[0]}/*"))  # Get all files
    all_py_files_of_schemas_dir: list = list(glob.glob(f"{path_to_dir[0]}/*.py"))  # Get all files

    if f"{path_to_dir[0]}/cache" in all_files_of_schemas_dir:  # if pack_schemas already exists
        pack_schemas_file_path: str = f"{path_to_dir[0]}/cache/pack_schemas.py"  # Set pack_schemas file path
    else:
        arg.run(f"mkdir {path_to_dir[0]}/cache")
        arg.run(f"touch {path_to_dir[0]}/cache/pack_schemas.py && touch {path_to_dir[0]}/cache/__init__.py")
        pack_schemas_file_path: str = f"{path_to_dir[0]}/cache/pack_schemas.py"

    schemas: list = [
        model.split("/")[-1][:-3] for model in all_py_files_of_schemas_dir
        if (model.split("/")[-1] != "__init__.py")
    ]
    
    with open(pack_schemas_file_path, "a+") as file:
        schema: str
        file.truncate(0)
        file.write("# mypy: ignore-errors\n")

        for schema in schemas:
            file.write(f"from .. import {schema}  # noqa: F841,F401\n")



@invoke.task
def hooks(arg):
    invoke_path = Path(arg.run("which invoke", hide=True).stdout[:-1])
    for src_path in Path(".hooks").iterdir():
        dst_path = Path(".git/hooks") / src_path.name
        print(f"Installing: {dst_path}")
        with open(str(src_path), "r") as f:
            src_data = f.read()
        with open(str(dst_path), "w") as f:
            f.write(src_data.format(invoke_path=invoke_path.parent))
        arg.run(f"chmod +x {dst_path}")
