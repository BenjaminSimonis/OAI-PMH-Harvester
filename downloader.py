import fnmatch
import os
import re
import requests
import wget
import zipfile

from constants import downloadpath
import validator


def download(oaid, rec):
    if ('<error code="idDoesNotExist">' not in rec) or ("hasFile:true" in rec):
        splits = re.split('<dc:identifier xsi:type="tel:URL">|</dc:identifier>', rec)
        for url in splits:
            if "/download/" in url:
                r = requests.get(url)
                d = str(r.headers['Content-disposition'])
                filename = str(re.findall("filename=(.+)", d)[0]).replace('"', '')
                if not os.path.exists(downloadpath + oaid):
                    os.makedirs(downloadpath + oaid)
                    target = downloadpath + oaid + "/" + filename
                    wget.download(url, target)
                    # Wenn kein PDF vorhanden ist, wird zu 99% eine zip datei da sein. Diese soll entpackt und der inhalt validiert werden
                    if fnmatch.filter(os.listdir(downloadpath + oaid), "*.zip"):
                        with zipfile.ZipFile(target, 'r') as zip_ref:
                            zip_ref.extractall(downloadpath + oaid)
                    filelist = os.listdir(downloadpath + oaid)
                    for file in filelist:
                        if ("zip" or "json") not in file:
                            validator.main(downloadpath + oaid + "/" + file, downloadpath + oaid + "/")
                    return True
    else:
        return False
