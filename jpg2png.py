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

    #決定流水號，若修改的日期與前一個檔案相同時流水號加 1
    if last_modified and last_modified.date() == modified.date():
        num += 1
    else:
        num = 1

    #依據流水號決定檔案
    targetname = "{}.png".format(num)

    #改名
    shutil.move(filename, targetname)

    last_modified = modified
