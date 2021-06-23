#!/usr/bin/env python3

import glob, os, zipfile

files = glob.glob("*.whl")

for old_name in files:
    new_name = old_name + ".zip"
    os.rename(old_name, new_name)
    print(old_name + "->" + new_name)
    with zipfile.ZipFile(new_name) as existing_zip:
         existing_zip.extractall(str(new_name).replace(".zip","").replace(".whl",""))
    os.remove(new_name)

