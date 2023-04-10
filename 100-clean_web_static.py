#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["34.224.2.20", "100.26.252.182"]


def do_clean(numb=0):
    """removes outdated archives.
    Args:
        number (int):  number of archives to keep.
    """
    numb = 1 if int(numb) == 0 else int(numb)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(numb)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(numb)]
        [run("rm -rf ./{}".format(a)) for a in archives]
