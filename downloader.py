import fnmatch
import os
from urllib.request import Request, urlopen
import wget
import zipfile

from constants import downloadpath
import validator


def download(link, rec):

    req = Request(link)
    r = urlopen(req)
    filename = str(r.headers['content-disposition']).split("filename=")[1].replace('"', '')
    oaid = link.split("/")[-1]
    path = downloadpath + oaid
    if not os.path.exists(path):
        os.makedirs(path)
    target = path + "/" + filename
    wget.download(link, target)
    if fnmatch.filter(os.listdir(path), "*.zip"):
        with zipfile.ZipFile(target, 'r') as zip_ref:
            zip_ref.extractall(path)
    filelist = os.listdir(path)
    for file in filelist:
        if ("zip" or "json") not in file:
            validator.main(path + "/" + file, path + "/")
