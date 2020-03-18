import glob


def list_files(dir_reg):
    files = []
    for file in glob.glob(f"{dir_reg}", recursive=True):
        files.append(file)
    return files


if __name__ == "__main__":
    list_files("*/*.jpg")
