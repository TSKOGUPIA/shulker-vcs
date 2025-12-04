import argparse
import init

version = "0.2.0a"

parser = argparse.ArgumentParser(description=f"A version control manager like git. Version {version}")
subparsers = parser.add_subparsers(dest="command")

initParser = subparsers.add_parser("init", help="initialize the repository")
initParser.add_argument("--verbose", "-v", action="store_true", help="Lists all processes going behind the scenes")

args = parser.parse_args()

if args.command == "init":
    init.init(args)