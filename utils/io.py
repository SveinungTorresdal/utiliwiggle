import os


def get_filepaths_by_extension(path: str, file_extension: str):
    """
    Finds files in designated folder and filters down to a more limited selection.

    @params:
    path: str           | Designated folder
    file_extension: str | Filter for files

    @returns list       | List containing all the filtered filepaths.
    """
    files = []

    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend([os.path.join(dirpath, file) for file in filenames if file.endswith(file_extension)])

    return files


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
