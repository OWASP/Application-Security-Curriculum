#!/usr/bin/env python3

import argparse
import csv
import os
import yaml


def main(source_directory: str, single_source_file: str) -> None:
    # select source file to parse
    if single_source_file:
        if
        current_source = source_load(single_source_file)
    else:
        for discovered_source_file in os.scandir(source_directory):
            current_source = source_load(discovered_source_file)


# converts all csv file in this folder
def localCSV(folder=script_directory):
    # print folder
    for f in os.listdir(folder):
        if f.endswith('.csv'):
            csvFile = os.path.join(folder, f)
            output = os.path.join(folder, f.replace('.csv', '.yml'))
            print(output)
            singleCSV(csvFile, output)


# converts only one csv file
def singleCSV(csvFile, output=None):
    output = output if output else script_directory + '/' + (csvFile.split('/')[-1].replace('.csv', '.yml'))
    with open(csvFile, 'rb') as csvFile:
        csvToYaml(csvFile, output)


# takes a csvFile name and output file name/path
def csvToYaml(csvFile, output):
    stream = open(output, 'w',encoding="utf-8")
    # https://stackoverflow.com/questions/18897029/read-csv-file-from-url-into-python-3-x-csv-error-iterator-should-return-str
    # need to decode bytes
    csvOpen = csv.reader(codecs.iterdecode(csvFile, 'utf-8'))
    keys = next(csvOpen)
    for row in csvOpen:
        yaml.dump([dict(zip(keys, row))], stream, default_flow_style=False)


def source_load(file_to_load: str) -> object:
    # load the file

    yaml_chunk = {}
    return yaml_chunk


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