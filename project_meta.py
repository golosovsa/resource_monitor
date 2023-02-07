from pathlib import Path

import tomli

PYPROJECT_TOML_PATH = (Path(__file__).parent / "pyproject.toml")


def _get_pyproject_field(pyproject_toml: dict, field: str) -> str:
    return pyproject_toml["tool"]["poetry"][field]


def get_project_meta() -> (str, str, str):
    """ return project name, version, description """

    with PYPROJECT_TOML_PATH.open("rt", encoding="utf-8") as fin:
        pyproject_toml = fin.read()

    pyproject_toml = tomli.loads(pyproject_toml)
    name = _get_pyproject_field(pyproject_toml, "name")
    version = _get_pyproject_field(pyproject_toml, "version")
    description = _get_pyproject_field(pyproject_toml, "description")

    return name, version, description

