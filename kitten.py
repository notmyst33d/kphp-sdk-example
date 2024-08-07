import os
import sys
import requests
import subprocess
from io import BytesIO
from zipfile import ZipFile

KPHP_SDK_VERSION = "20240807"

def install(variant):
    bio = BytesIO(requests.get(f"https://github.com/notmyst33d/kphp-kdb/releases/download/kphp-sdk-{KPHP_SDK_VERSION}/kphp-sdk-{KPHP_SDK_VERSION}-{variant}.zip", allow_redirects=True).content)
    try:
        os.mkdir("sdk")
    except:
        pass
    ZipFile(bio).extractall("sdk")
    os.chmod("sdk/kphp2cpp", 755)

if not os.path.exists("sdk"):
    print("Downloading KPHP SDK")
    variant = "ubuntu"
    if os.path.isfile("/etc/os-release"):
        with open("/etc/os-release", "r") as f:
            variant = list(filter(lambda x: x.startswith("ID="), f.readlines()))[0].replace("ID=", "").rstrip("\r\n")
    try:
        install(variant)
    except:
        install("ubuntu")

subprocess.call(f"./sdk/kphp2cpp -f sdk/KPHP/functions.txt -d . {sys.argv[1]}", shell=True)
