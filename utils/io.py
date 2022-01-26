import os

def find(path, reg):
    print(reg)
    files = list()

    for (dirpath, dirnames, filenames) in os.walk(path):
        files += [os.path.join(dirpath, file) for file in filenames]
        
    output = list(filter(lambda x: reg in x, files))

    return output

if __name__== "__main__":
    print('Wrong file. Run main.py.')