from pathlib import Path

import tomllib

PROJECT_TOML_PATH = (Path(__file__).parent / "pyproject.toml")


def _get_project_field(project_toml: dict, field: str) -> str:
    return project_toml["tool"]["poetry"][field]


def get_project_meta() -> (str, str, str):
    """ return project name, version, description """

    with PROJECT_TOML_PATH.open("rt", encoding="utf-8") as fin:
        project_toml = fin.read()

    project_toml = tomllib.loads(project_toml)
    name = _get_project_field(project_toml, "name")
    version = _get_project_field(project_toml, "version")
    description = _get_project_field(project_toml, "description")

    return name, version, description

