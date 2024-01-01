"""

Bustes HTML browser cache on files using query strings.
To create a cache buster query string, write this in a file:

'?cachebuster=NEWHASH'

When executing this program, 'NEWHASH' will be replaced with a 16-charcter hexadecimal hash, suffixed by an 'H'.
If executing this script again, the hash will be changed into a new one.
This program needs a buster.config file to work. This is a text file which indicates in what files to perform cache busting
An example buster.config:

**TARGETS
*.css
*.js
**EXCLUDED
dir\special_file.js
This file will bust the caches of all CSS and JavaScript files, except for the file dir\special_file.js
This file's filtering is based on Python's fnmatch.

"""


class InvalidBusterConfigError(Exception):
    pass


def main():
    import os
    import re
    import argparse
    from fnmatch import fnmatch
    from random import randint
    BUSTER_CONFIG_PATH = ".github/workflows/buster.config"

    parser = argparse.ArgumentParser(prog="Cache Buster", description="Bustes HTML browser cache on files using query strings.", epilog="Since I couldn't get newline to work with argparse, read what this script does in the code.")
    parser.add_argument("--noinput", action="store_true", help="Run this file without asking for input. All filenames' query string will be cache busted")
    args = parser.parse_args()
    noinput = args.noinput

    try:
        config = open(BUSTER_CONFIG_PATH, "r")
    except FileNotFoundError:
        print("buster.config not found. Create a default config file? ALL files in this folder will be targeted. (s/n)")
        if(input("-> ") != "s"):
            return
        config = open(BUSTER_CONFIG_PATH, "x")
        config.write("**TARGETS\n*")
        config.close()
        config = open(BUSTER_CONFIG_PATH, "r")
    current_type = None
    targets = []
    excluded = []
    for i, line in enumerate(config):
        line = line.rstrip("\n")
        if(line.startswith("**")):
            match line:
                # I like enums, but for some reason I don't like them in Python
                case "**TARGETS":
                    current_type = "t"
                case "**EXCLUDED":
                    current_type = "e"
                case _:
                    raise InvalidBusterConfigError(f"buster.config error at line {i + 1}: If a line starts with two asterisks, it must be '**TARGETS' or '**EXCLUDED'.")
        else:
            match current_type:
                case "t":
                    targets.append(line)
                case "e":
                    excluded.append(line)
                case _:
                    raise InvalidBusterConfigError(f"buster.config error at line {i + 1}: This file must start with '**TARGETS' or '**EXCLUDED'.")
    config.close()

    if(__debug__):
        _files_targeted = 0
        _caches_busted = 0

    file_filters = []
    if(not noinput):
        print("Indicate the filenames whose query string to cache bust.")
        print("Separate multiple filenames with a newline and end with an empty prompt.")
        print("Write nothing to cache bust all filenames.")
        while True:
            filename = input("-> ")
            if filename:
                file_filters.append(filename)
            else:
                break

    re_pattern = re.compile(r"(" + "|".join(file_filters) + r")(\?cachebuster=(?:(?:NEWHASH)|(?:[0-9a-f]{16}H)))")

    for root, _, files in os.walk("."):
        for filename in files:
            path = os.path.join(root, filename)[2:]

            if(path == os.path.basename(__file__) or path == BUSTER_CONFIG_PATH):
                continue # Skip iteration
            if(all(not fnmatch(path, x) for x in targets)):
                continue # Skip iteration
            if(any(fnmatch(path, x) for x in excluded)):
                continue # Skip iteration
            
            current = open(path, "rt")
            try:
                data = current.read()
            except UnicodeDecodeError:
                current.close()
                continue # Skip iteration
            current.close()
            
            if(__debug__):
                _files_targeted += 1
                print("Targeted", path)
            
            splitted = re.split(re_pattern, data).copy()
            for i in range(2, len(splitted), 3):
                splitted[i] = f"?cachebuster={randint(0, (16 ** 16) - 1):016x}H"
                if(__debug__):
                    _caches_busted += 1
            data = "".join(splitted)

            current = open(path, "wt")
            current.write(data)
            current.close()
    
    if(__debug__):
        if(_files_targeted == 0):
            print(f"WARNING: No files were targeted, {_caches_busted} caches were busted. Try modifying the buster.config file.")
        else:
            print(f"Successfully targeted {_files_targeted} files and busted {_caches_busted} caches.")
        if(not noinput):
            input()


if(__name__ == "__main__"):
    try:
        main()
    except Exception as err:
        input(err)
