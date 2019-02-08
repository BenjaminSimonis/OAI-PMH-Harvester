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
    if not os.path.exists(downloadpath + oaid):
        os.makedirs(downloadpath + oaid)
        target = downloadpath + oaid + "/" + filename
        wget.download(link, target)
        if fnmatch.filter(os.listdir(downloadpath + oaid), "*.zip"):
            with zipfile.ZipFile(target, 'r') as zip_ref:
                zip_ref.extractall(downloadpath + oaid)
                filelist = os.listdir(downloadpath + oaid)
                for file in filelist:
                    if ("zip" or "json") not in file:
                        validator.main(downloadpath + oaid + "/" + file, downloadpath + oaid + "/")
