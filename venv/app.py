import time
import datetime
import logging
from zipfile import ZipFile
from pathlib import Path

from constants import *

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
    filename = time + " | Analysis service log"
    return (filename)

def compress_files(files: list, filename: str):
    with ZipFile(filename, "w") as zip:
        for file in [p for p in p.iterdir() if p.is_file()]:
            zip.write(file, arcname=file.name)
    logging.debug("Log compressed successfuly.")

def get_file_age(path) -> int:
    return Path(path).stat().st_ctime

if __name__ == "__main__":
    f = build_filename(CUR_DIR.stat().st_ctime)
    print(f)




