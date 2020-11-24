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
                if requirement['module'] not in curriculum:
                    print("New module found: {}, adding to curriculum".format(requirement['module']))
                    curriculum[requirement['module']] = {}

                module = curriculum[requirement['module']]

                if 'units' in requirement:
                    print("Requirement {} has units".format(requirement['req_id']))

                    for unit in requirement['units']:
                        try:
                            if unit['unit']:
                                if unit['unit'] in module:
                                    print("Unit '{}' already in module '{}'".format(unit['unit'], requirement['module']))
                                    existing_unit = module[unit['unit']]

                                    # add these terms to existing terms for unit
                                    for term in unit['terms']:
                                        print("Processing term: {}".format(term))
                                        if term in existing_unit:
                                            print("Term is already present in unit, updating knowledge level if needed")
                                            existing_unit[term] = max(existing_unit[term], unit['level'])
                                        else:
                                            print("Term not present in unit, adding")
                                            existing_unit[term] = unit['level']
                                else:
                                    # add unit and terms to module
                                    print("New unit: {}".format(unit['unit']))
                                    module[unit['unit']] = {term: unit['level'] for term in unit['terms']}
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
