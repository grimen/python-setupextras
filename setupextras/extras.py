
# coding: utf-8

# =========================================
#       IMPORTS
# --------------------------------------

import os
import glob
import setuptools

from os import path


# =========================================
#       CONSTANTS
# --------------------------------------

README_IDENTIFIER = 'README'
DEFAULT_REQUIREMENTS = 'requirements.txt'
DEFAULT_SILENT = True

# FIXME: use glob patterns instead
EXCLUDE_FILE_PATHS_WITH_PREFIX = [
    '.git',
    '.tox',
    '.eggs',
    'build',
    'dist',
]
EXCLUDE_FILE_PATHS_WITH_CONTENT = [
    '__pycache__',
    '.egg-info',
]
EXCLUDE_FILE_PATHS_WITH_SUFFIX = [
    '.pyc',
]


# =========================================
#       ERRORS
# --------------------------------------

class Error(Exception):
    pass


# =========================================
#       FUNCTIONS
# --------------------------------------

def get_requirements(
    root_path = None,
    file_name = None,
    silent = None,
):
    file_name = file_name or DEFAULT_REQUIREMENTS

    if silent != False:
        silent = bool(silent) or DEFAULT_SILENT

    try:
        root_path = root_path or path.abspath(os.getcwd())

        requirements_file_path = path.join(root_path, file_name)

        with open(requirements_file_path) as file:
            requirements = [requirement.strip() for requirement in file.readlines()]
            requirements = filter(lambda requirement: len(requirement), requirements)
            requirements = list(requirements)

        return requirements

    except Exception as error:
        if not silent:
            raise Error(error)

        return []

def get_packages(*args, **kwargs):
    silent = kwargs.get('silent', None)

    if silent != False:
        silent = bool(silent) or DEFAULT_SILENT

    try:
        del kwargs['silent']
    except:
        pass

    try:
        packages = setuptools.find_packages(*args, **kwargs)

        return packages

    except Exception as error:
        if not silent:
            raise Error(error)

        return []

def get_data_files(
    data_file_patterns = [],
    root_path = None,
    silent = None,
    exlude_prefix = None,
    exlude_content = None,
    exlude_suffix = None,
):
    if silent != False:
        silent = bool(silent) or DEFAULT_SILENT

    try:
        root_path = root_path or path.abspath(os.getcwd())

        data_file_dirs = []

        for root, dirs, files in os.walk(root_path):
            data_file_dirs.append(root)

        data_files = []

        for data_file_dir in data_file_dirs:
            files = []

            should_be_excluded = any(map(lambda exclude_value: (
                data_file_dir and data_file_dir.startswith(path.join(root_path, exclude_value))
            ), exlude_prefix or EXCLUDE_FILE_PATHS_WITH_PREFIX))

            should_be_excluded = should_be_excluded or any(map(lambda exclude_value: (
                exclude_value in data_file_dir
            ), exlude_content or EXCLUDE_FILE_PATHS_WITH_CONTENT))

            should_be_excluded = should_be_excluded or any(map(lambda exclude_value: (
                data_file_dir and data_file_dir.endswith(exclude_value)
            ), exlude_suffix or EXCLUDE_FILE_PATHS_WITH_SUFFIX))

            if not should_be_excluded:
                for data_file_pattern in data_file_patterns:
                    if not data_file_pattern in files:
                        files += glob.glob(path.join(data_file_dir, data_file_pattern))

                if not files:
                    continue

                target = path.join(root_path, data_file_dir)

                data_files.append((target, files))

        return data_files

    except Exception as error:
        if not silent:
            raise Error(error)

        return []

def get_readme(
    root_path = None,
    silent = True,
):
    if silent != False:
        silent = bool(silent) or DEFAULT_SILENT

    try:
        root_path = root_path or path.abspath(os.getcwd())

        readme = None

        for file_name in os.listdir(root_path):
            if README_IDENTIFIER in file_name:
                readme_file_path = path.join(root_path, file_name)

                try:
                    with open(readme_file_path) as file:
                        readme = file.read()

                        break

                except:
                    pass


        if readme is None:
            if not silent:
                raise Error('No README found in: {0}'.format(root_path))

        return readme

    except Exception as error:
        if not silent:
            raise Error(error)

        return None


# =========================================
#       EXPORTS
# --------------------------------------

__all__ = [
    'get_requirements',
    'get_packages',
    'get_data_files',
    'get_readme',
]
