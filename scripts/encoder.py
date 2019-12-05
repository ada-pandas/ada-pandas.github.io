import chardet
import glob
import os

for filename in glob.glob("../data_min/*/*/*"):
    inp = open(filename, "rb")
    lines = inp.read()
    if chardet.detect(lines[:100])['encoding'] == "UTF-16":
        out = open(filename[:-4] + "_decoded.csv", "wb")
        out.write(lines.decode("utf-16").encode("utf-8"))
        inp.close()
        out.close()
        os.remove(filename)
    else:
        inp.close()
        os.rename(filename, filename[:-4] + "_decoded.csv")
