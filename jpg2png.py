import os
import shutil
from datetime import datetime

def is_imag(filename):
    return any(map(filename.endswith, [".JPG"]))
	
def get_time(filename):
    timestamp = os.path.getmtime(filename)
    return datetime.fromtimestamp(timestamp)

filenames = os.listdir(".")
images = filter(is_imag, filenames)
filenames.sort(key=get_time)
last_modified = None
for filename in filenames:
    modified = get_time(filename)

    # Sorting the files with date, and set serial number if the date is same
    if last_modified and last_modified.date() == modified.date():
        num += 1
    else:
        num = 1

    # Name:{serial number}.png   >   if the date is all the same
    targetname = "{}.png".format(num)
    shutil.move(filename, targetname)

    last_modified = modified
