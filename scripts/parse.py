#!/usr/bin/env python3

import argparse
import os

def main(source_directory: str, single_source_file: str) -> None:
    # select source file to parse
    if single_source_file:
        current_source = source_load(single_source_file)
    else
        for discovered_source_file in os.scandir(source_directory)
            current_source = source_load(discovered_source_file)
    

def source_load(file_to_load: str) -> List[source]
    # load the file
    return addon


if __name__ == "__main__":
    # get absolute path to this script for walking this repo
    script_directory = os.path.dirname(os.path.abspath(__file__))
    source_directory = os.path.normpath(os.path.join(script_directory, "../src"))

    parser = argparse.ArgumentParser(description="Parse source files for YAML output.")
    parser.add_argument(
        "-s",
        "--source-file",
        type=str,
        default=""
        help="source files to parse to update yaml from.",
    )

    args = parser.parse_args()
    main(source_directory, args.source_file)