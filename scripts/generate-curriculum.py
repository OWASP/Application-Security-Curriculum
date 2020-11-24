#!/usr/bin/env python3

import argparse
import os
import yaml

blooms = {1: 'Remember', 2: 'Understand', 3: 'Apply', 4: 'Analyze', 5: 'Evaluate', 6: 'Create'}

def main(folder: str, single_source_file: str = None) -> None:
    # select source file to parse
    if single_source_file:
        data = source_load(single_source_file)

        if data:
            curriculum = {}
            for requirement in data:
                if 'concepts' in requirement:
                    print("Requirement {} has concepts".format(requirement['req_id']))
                    for concept in requirement['concepts']:
                        try:
                            if concept['concept'] in curriculum:
                                # add these terms to existing terms
                                for term in concept['terms']:
                                    print("Processing term: {}".format(term))
                                    if term in curriculum[concept['concept']]:
                                        print("Term is already present in concept")
                                        if curriculum[concept['concept']][term] < concept['level']:
                                            curriculum[concept['concept']][term] = concept['level']
                                    else:
                                        print("Term not present in concept")
                                        curriculum[concept['concept']][term] = concept['level']
                            else:
                                # add concept and terms to curriculum
                                print("New concept: {}".format(concept['concept']))
                                curriculum[concept['concept']] = {term: concept['level'] for term in concept['terms']}
                        except KeyError:
                            print("Requirement {} has a malformed concepts list".format(requirement['req_id']))
                else:
                    pass

            print(curriculum)
    else:
        for discovered_source_file in os.scandir(folder):
            current_source = source_load(discovered_source_file)

def source_load(file_to_load: str) -> object:
    data = None
    with open(file_to_load, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    return data

if __name__ == "__main__":
    # get absolute path to this script for walking this repo
    script_directory = os.path.dirname(os.path.abspath(__file__))
    source_directory = os.path.normpath(os.path.join(script_directory, "../src"))

    parser = argparse.ArgumentParser(description="Parse source files for YAML output.")
    parser.add_argument(
        "-s",
        "--source-file",
        type=str,
        default="",
        help="source files to parse to update yaml from.",
    )

    args = parser.parse_args()
    main(source_directory, args.source_file)