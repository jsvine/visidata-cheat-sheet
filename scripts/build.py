#!/usr/bin/env python
from jinja2 import Template
import argparse
import yaml
import re
import sys
import os

from uniquekeys import UniqueKeyLoader

PAPERSIZES = [ "letter", "A4" ]

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--meta",
        type = argparse.FileType("r"),
        default = "input/metadata.yaml",
        required = False,
    )
    parser.add_argument(
        "--data",
        type = argparse.FileType("r"),
        default = "input/cheat-sheet.yaml",
        required = False,
    )
    parser.add_argument(
        "--template",
        type = argparse.FileType("r"),
        default = "input/template.html"
    )
    parser.add_argument("--langs")
    parser.add_argument("--stdout", action = "store_true")
    return parser.parse_args(args)

def main():
    args = parse_args(sys.argv[1:])
    tmpl = Template(args.template.read())
    meta = yaml.load(args.meta, Loader = UniqueKeyLoader)
    sections = yaml.load(args.data, Loader = UniqueKeyLoader)
    
    langs = args.langs or meta.keys()

    for lang in langs:
        res = tmpl.render(
            sections = sections,
            meta = meta[lang],
            lang = lang,
            all_langs = list(langs),
            all_sizes = PAPERSIZES,
        )

        if args.stdout:
            print(res)
        else:
            os.makedirs(f"docs/{lang}", exist_ok = True)
            dest = f"docs/{lang}/index.html"
            with open(dest, "w") as f:
                f.write(res)

if __name__ == "__main__":
    main()
