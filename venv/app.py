import time
import datetime
from zipfile import ZipFile
from pathlib import Path

from constants import *
from Logger.logger import LOGGER

# print(CUR_DIR)
# print(f"{time.asctime(time.gmtime(TIME_ROTATION))} --> last access")
# print(time.asctime(time.gmtime(CUR_DIR.stat().st_mtime)))
# print(CUR_DIR.stat().st_ctime)

p = Path(PATH)

def build_filename(file_creation_date: int) -> str:
    # convert from epoch to datetime
    time = datetime.datetime.fromtimestamp(file_creation_date)
    # format
    time = time.strftime(DATE_FORMAT)
    filename = time + " log"
    return filename

def get_list_files(path: Path) -> list:
    return [f for f in path.iterdir() if f.is_file() and (get_file_age(path) < time.time() - TIME_ROTATION)]

def compress_files(files: list, filename: str, path: Path):
    with ZipFile(filename + ".zip", "w") as zip:
        for file in get_list_files(path):
            zip.write(file, arcname=file.name)
    LOGGER.info("Log compressed successfuly.")

def get_file_age(path) -> int:
    return Path(path).stat().st_ctime

if __name__ == "__main__":
    l = get_list_files(p)
    f = build_filename(CUR_DIR.stat().st_ctime)
    compress_files(l,f,p)





