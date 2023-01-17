import os.path

import OS


def check_path_is_folder(path):
    if not os.path.exists(path):
        raise Exception('Path does not exist')
    if not os.path.isdir(path):
        raise Exception('Path is not a directory')


def get_files_from_path(path):
    file_names = []
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if not os.path.isdir(full_path):
            file_names.append(entry)
        return file_names
