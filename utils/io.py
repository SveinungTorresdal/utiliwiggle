import os


def get_filepaths_by_extension(path: str, file_extension: str):
    files = []

    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend([os.path.join(dirpath, file) for file in filenames if file.endswith(file_extension)])

    return files

if __name__ == "__main__":
    print('Wrong file. Run main.py.')
