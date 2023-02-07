import argparse
import json

from project_meta import get_project_meta
from immutable import get_immutable_info


def main():
    name, version, description = get_project_meta()

    parser = argparse.ArgumentParser(
        prog=f"{name} version {version}",
        description=description,
    )
    parser.add_argument("content", choices=["all", "immutable", "mutable", "processes", "process"], default="all")
    parser.add_argument("-v", "--version", action='version', version=version)
    parser.add_argument("-j", "--json", dest="JSON_OUTPUT", action="store_true", help="output in JSON format")

    args = parser.parse_args()
    result = {}

    print(args)
    all_content = args.content == "all"

    if all_content or args.content == "all":
        result["Immutable info"] = get_immutable_info()

    if len(result) == 0:
        parser.print_help()
        exit(2)

    print(result)

if __name__ == "__main__":
    main()
