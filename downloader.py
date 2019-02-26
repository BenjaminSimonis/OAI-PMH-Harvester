import fnmatch
import os
from urllib.request import Request, urlopen
import wget
import zipfile

from constants import get_constants as c
from mdparser import parser
import validator

downloadzip = False

def download(link, rec):

    req = Request(link)
    r = urlopen(req)
    filename = str(r.headers['content-disposition']).split("filename=")[1].replace('"', '')
    oaid = link.split("/")[-1]
    path = c().DOWNLOADPATH() + oaid
    if not os.path.exists(path):
        os.makedirs(path)
    target = path + c().SLASH() + filename
    wget.download(link, target)
    if fnmatch.filter(os.listdir(path), "*.zip"):
        filelist = unpack_zip(path)
    else:
        filelist = os.listdir(path)
    parser(filename, rec, path)
    for file in filelist:
        if ("zip" or "json") not in file:
            validator.main(path + c().SLASH() + file, path + c().SLASH())
    for file in filelist:
        if file is not "download.zip":
            os.remove(path + c().SLASH() + file)
    return True


def unpack_zip(path):
    f_list = os.listdir(path)
    for file in f_list:
        if ".zip" in file:
            with zipfile.ZipFile(path, 'r') as zip_ref:
                if downloadzip is False and file is "download.zip":
                    zip_ref.extractall(path)
                    downloadzip = True
                elif file is not "download.zip":
                    zip_ref.extractall(path)
                if file is not "download.zip":
                    os.remove(path + c().SLASH() + file)
            unpack_zip(path)
        else:
            return f_list
