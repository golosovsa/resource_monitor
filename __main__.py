import argparse
import json
import yaml

from mutable import get_mutable_info
from processes import get_processes_info
from project_meta import get_project_meta
from immutable import get_immutable_info


OPTION_ALL = "all"
OPTION_IMMUTABLE = "immutable"
OPTION_MUTABLE = "mutable"
OPTION_PROCESSES = "processes"

OPTIONS = [OPTION_ALL, OPTION_IMMUTABLE, OPTION_MUTABLE, OPTION_PROCESSES]


def main():
    name, version, description = get_project_meta()

    parser = argparse.ArgumentParser(
        prog=f"{name}",
        description=description,
    )
    parser.add_argument("content", choices=OPTIONS, default=OPTION_ALL)
    parser.add_argument("-v", "--version", action='version', version=version)
    parser.add_argument("-j", "--json", dest="JSON_OUTPUT", action="store_true", help="output in JSON format")

    args = parser.parse_args()
    result = {}

    all_content = args.content == OPTION_ALL

    if all_content or args.content == OPTION_IMMUTABLE:
        result["Immutable_info"] = get_immutable_info()

    if all_content or args.content == OPTION_MUTABLE:
        result["mutable_info"] = get_mutable_info()

    if all_content or args.content == OPTION_PROCESSES:
        result["processes_info"] = get_processes_info()

    if len(result) == 0:
        parser.print_help()
        exit(2)

    if args.JSON_OUTPUT:
        print(json.dumps(result, indent=2))
        return

    print(yaml.dump(result))


if __name__ == "__main__":
    main()
