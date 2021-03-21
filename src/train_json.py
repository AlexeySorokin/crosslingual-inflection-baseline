import json
from argparse import ArgumentParser

from train import main

argument_parser = ArgumentParser()
argument_parser.add_argument("config_file")

if __name__ == '__main__':
    args = argument_parser.parse_args()
    with open(args.config_file, "r", encoding="utf8") as fin:
        config = json.load(fin)
    args = []
    for key, value in config.items():
        args.append(key)
        if key not in ["--mono", "--shuffle"]:
            args.extend(str(value).split())
    main(args=args)