import subprocess
import sys
import os

fname = sys.argv[1]

def decompress(fname, suf, cmd):
    os.system("mv %s %s" % (fname, fname+suf))
    os.system("%s %s" %(cmd,fname)+suf)

#ftype -> (suf, cmd)
dict_ = {
        "RAR":( ".rar", "unrar e"),
        "Zoo":( ".zoo", "zoo -extract"),
        "rzip":( ".rz", "rzip -d"),
        "ARJ archive":( ".arj", "arj e"),
        "KGB Archiver":( ".kgb", "kgb"),
        "Microsoft Cabinet archive":( ".CAB","cabextract "),
        "PPMD":( ".ppmd","ppmd d "),
        "Zip archive":( ".zip","unzip "),
        "POSIX tar":( ".tar","tar xf "),
        "gzip":( ".gz","gzip -d "),
        "7-zip":( ".7z","7z e "),
        "XZ":( ".xz","xz -d "),
        "bzip2":(".bz2","bzip2 -d ")
    }

while True:
    ftype = subprocess.check_output(["file", fname]).split(":")[1].strip()
    print ftype
    if ftype.startswith("ARC"):
        out = subprocess.check_output(["nomarch", fname]).split()[0].strip()
        fname = out.strip()
    else:
        in_dict = False
        for key in dict_:
            if ftype.startswith(key):
                decompress(fname, *(dict_[key]))
                in_dict = True
        if not in_dict: break

