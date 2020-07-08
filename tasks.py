import datetime
import glob
import json
import os
from pathlib import Path

import invoke
from loguru import logger

PACKAGE_NAME = "saqtan-api"
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
    arg.run(f"{autoflake} {apps} ../{PACKAGE_NAME}", echo=True)
    arg.run(f"isort --recursive {apps} ../{PACKAGE_NAME}", echo=True)
    arg.run(f"black {apps} ../{PACKAGE_NAME}", echo=True)


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
        print(json.dumps({"app_name": app, "created_at": str(now_time)}), file=file)


@invoke.task(name="packmodels")
def pack_models(arg, dirname="models"):
    try:
        print("Packing your models...")
        sucess_string = ""

        base_dir: str = os.path.dirname(os.path.realpath(__file__))
        path_to_dir: list = [
            x[0] for x in os.walk(base_dir) if x[0].split("/")[-1] == "models"
        ]  # Find path to models dir

        all_files_of_models_dir: list = list(
            glob.glob(f"{path_to_dir[0]}/*")
        )  # Get all files
        all_py_files_of_models_dir: list = list(
            glob.glob(f"{path_to_dir[0]}/*.py")
        )  # Get all files

        if (
            f"{path_to_dir[0]}/cache" in all_files_of_models_dir
        ):  # if pack_models already exists
            pack_models_file_path: str = f"{path_to_dir[0]}/cache/pack_models.py"  # Set pack_models file path
        else:
            sucess_string += "Created directory cache in models directory\n"
            sucess_string += "Created pack_models.py module in models/cache directory\n"

            arg.run(f"mkdir {path_to_dir[0]}/cache")
            arg.run(
                f"touch {path_to_dir[0]}/cache/pack_models.py && touch {path_to_dir[0]}/cache/__init__.py"
            )
            pack_models_file_path: str = f"{path_to_dir[0]}/cache/pack_models.py"

        models: list = [
            model.split("/")[-1][:-3]
            for model in all_py_files_of_models_dir
            if (model.split("/")[-1] != "__init__.py")
        ]

        with open(pack_models_file_path, "a+") as file:
            model: str
            file.truncate(0)
            file.write("# mypy: ignore-errors\n")

            for model in models:
                file.write(f"from .. import {model}  # noqa: F841,F401\n")

        sucess_string += (
            "Success. Your models packed successfully in models/cache directory"
        )
        print(sucess_string)
    except Exception as e:
        print(f"Fail. Something went wrong. ERROR: {e}")
        logger.error(e)


@invoke.task(name="packschemas")
def pack_schemas(arg, dirname="schemas"):
    try:
        print("Packing your schemas...")
        sucess_string = ""

        base_dir: str = os.path.dirname(os.path.realpath(__file__))
        path_to_dir: list = [
            x[0] for x in os.walk(base_dir) if x[0].split("/")[-1] == "schemas"
        ]  # Find path to models dir

        all_files_of_schemas_dir: list = list(
            glob.glob(f"{path_to_dir[0]}/*")
        )  # Get all files
        all_py_files_of_schemas_dir: list = list(
            glob.glob(f"{path_to_dir[0]}/*.py")
        )  # Get all files

        if (
            f"{path_to_dir[0]}/cache" in all_files_of_schemas_dir
        ):  # if pack_schemas already exists
            pack_schemas_file_path: str = f"{path_to_dir[0]}/cache/pack_schemas.py"  # Set pack_schemas file path
        else:
            sucess_string += "Created directory cache in schemas directory\n"
            sucess_string += (
                "Created pack_schemas.py schemas in schemas/cache directory\n"
            )

            arg.run(f"mkdir {path_to_dir[0]}/cache")
            arg.run(
                f"touch {path_to_dir[0]}/cache/pack_schemas.py && touch {path_to_dir[0]}/cache/__init__.py"
            )
            pack_schemas_file_path: str = f"{path_to_dir[0]}/cache/pack_schemas.py"

        schemas: list = [
            model.split("/")[-1][:-3]
            for model in all_py_files_of_schemas_dir
            if (model.split("/")[-1] != "__init__.py")
        ]

        with open(pack_schemas_file_path, "a+") as file:
            schema: str
            file.truncate(0)
            file.write("# mypy: ignore-errors\n")

            for schema in schemas:
                file.write(f"from .. import {schema}  # noqa: F841,F401\n")

        sucess_string += (
            "Success. Your schemas packed successfully in schemas/cache directory"
        )
        print(sucess_string)

    except Exception as e:
        print(f"Fail. Something went wrong. ERROR: {e}")
        logger.error(e)


@invoke.task(name="createModel")
def create_model(arg, model_name):
    try:
        print(f"Creating model {model_name}...")
        success_string = ""

        base_dir: str = os.path.dirname(os.path.realpath(__file__))
        path_to_models_dir: list = [
            x[0] for x in os.walk(base_dir) if x[0].split("/")[-1] == "models"
        ]
        path_to_new_model = f"{path_to_models_dir[0]}/{model_name}"

        arg.run(f"touch {path_to_new_model}")

        with open(path_to_new_model, "a+") as model_file:
            model_file.write(
                "from sqlalchemy import Column, Float, Integer, String\n\n"
            )
            model_file.write("from ..database import Database\n\n\n")
            model_file.write(
                f"class {model_name.capitalize()[:-3]}(Database.Base):\n   "
            )
            model_file.write(f' __tablename__ = "{model_name.capitalize()[:-3]}"')

        success_string += f"Model {model_name} successfully created"
        print(success_string)

        arg.run("inv packmodels")  # Pack models after create new

    except Exception as e:
        print(f"Fail. Something went wrong. ERROR: {e}")
        logger.error(e)


@invoke.task(name="createSchema")
def create_schema(arg, schema_name):
    try:
        print(f"Creating schema {schema_name}...")
        success_string = ""

        base_dir: str = os.path.dirname(os.path.realpath(__file__))
        path_to_schemas_dir: list = [
            x[0] for x in os.walk(base_dir) if x[0].split("/")[-1] == "schemas"
        ]
        path_to_new_schema = f"{path_to_schemas_dir[0]}/{schema_name}"

        arg.run(f"touch {path_to_new_schema}")

        with open(path_to_new_schema, "a+") as schema_file:
            schema_file.write("from pydantic import BaseModel\n")

        success_string += f"Schema {schema_name} successfully created"
        print(success_string)

        arg.run("inv packschemas")  # Pack schemas after create new

    except Exception as e:
        print(f"Fail. Something went wrong. ERROR: {e}")
        logger.error(e)


@invoke.task(name="packutils")
def pack_utils(arg, dirname="utils"):
    try:
        print("Packing your utils...")
        sucess_string = ""

        base_dir: str = os.path.dirname(os.path.realpath(__file__))
        path_to_dir: list = [
            x[0] for x in os.walk(base_dir) if x[0].split("/")[-1] == "utils"
        ]  # Find path to utils dir

        all_files_of_utils_dir: list = list(
            glob.glob(f"{path_to_dir[0]}/*")
        )  # Get all files
        all_py_files_of_utils_dir: list = list(
            glob.glob(f"{path_to_dir[0]}/*.py")
        )  # Get all files

        if (
            f"{path_to_dir[0]}/cache" in all_files_of_utils_dir
        ):  # if pack_utils already exists
            pack_utils_file_path: str = f"{path_to_dir[0]}/cache/pack_utils.py"  # Set pack_utils file path
        else:
            sucess_string += "Created directory cache in utils directory\n"
            sucess_string += "Created pack_utils.py module in utils/cache directory\n"

            arg.run(f"mkdir {path_to_dir[0]}/cache")
            arg.run(
                f"touch {path_to_dir[0]}/cache/pack_utils.py && touch {path_to_dir[0]}/cache/__init__.py"
            )
            pack_utils_file_path: str = f"{path_to_dir[0]}/cache/pack_utils.py"

        utils: list = [
            util.split("/")[-1][:-3]
            for util in all_py_files_of_utils_dir
            if (util.split("/")[-1] != "__init__.py")
        ]

        with open(pack_utils_file_path, "a+") as file:
            util: str
            file.truncate(0)
            file.write("# mypy: ignore-errors\n")

            for util in utils:
                file.write(f"from .. import {util}  # noqa: F841,F401\n")

        sucess_string += (
            "Success. Your utils packed successfully in utils/cache directory"
        )
        print(sucess_string)

        arg.run("inv packutils")
    except Exception as e:
        print(f"Fail. Something went wrong. ERROR: {e}")
        logger.error(e)


@invoke.task(name="createUtil")
def create_util(arg, util_name):
    try:
        print(f"Creating util: {util_name}...")
        success_string: str = ""

        base_dir: str = os.path.dirname(os.path.realpath(__file__))
        path_to_utils_dir: list = [
            x[0] for x in os.walk(base_dir) if x[0].split("/")[-1] == "utils"
        ]
        path_to_new_util = f"{path_to_utils_dir[0]}/{util_name}"

        arg.run(f"touch {path_to_new_util}")

        with open(path_to_new_util, "a+") as util_file:
            util_file.write("from loguru import logger\n")
            util_file.write("from sqlalchemy.orm import Session\n\n")
            util_file.write("from Database.models.cache import pack_models\n\n")
            util_file.write("class UtilClass(object):\n   pass")

        success_string += f"Util {util_name} created successfully"
        print(success_string)

    except Exception as e:
        print(f"Fail. Something went wrong. ERROR: {e}")
        logger.error(e)


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
