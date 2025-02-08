import zipfile
import pathlib


def makeArchive(filePaths, folder):
    destPath = pathlib.Path(folder, "archived.zip")
    with zipfile.ZipFile(destPath, 'w') as archive:
        for filePath in filePaths:
            filePath = pathlib.Path(filePath)
            archive.write(filePath, arcname=filePath.name)


if __name__ == "__main__":
    makeArchive(["data.txt", "java.txt"], "dest")

