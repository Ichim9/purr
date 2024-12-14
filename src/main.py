import sys
import os
import toml
from git import Repo
def directory(string):
  return os.path.expanduser(string)

def purr_help():
    helpinf = {
        "list":"Lists your installed packages."
    }
    length = len(list(helpinf.keys()))
    print("--------------------")
    for i in range(0,length):
        k = list(helpinf.keys())[i]
        v = list(helpinf.values())[i]
        print(f"{k} | {v}")
    print("--------------------")
pass

if (not __name__ == '__main__'):
    print("ERROR: Please don't import PURR")
    exit()
try:
    conf = toml.load(directory("~/.purr/purr.toml"))
    pass
except FileNotFoundError:
    default_toml = {"config":{"autoupdate":False},"packages":{}}
    os.system("mkdir ~/.purr")
    with open(directory("~/.purr/purr.toml"), 'w') as f:
        yay = toml.dump(default_toml, f)
    f.close()
    conf = toml.load(directory("~/.purr/purr.toml"))
try:
    if (sys.argv[1] == "list"):
        for i in range(0,len(list((conf["packages"]).keys()))):
            k = list((conf["packages"]).keys())[i]
            v = list((conf["packages"]).values())[i]
            print(f"{k} ({v})")
except IndexError:
    purr_help()
    exit()