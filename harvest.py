from urllib.error import HTTPError

from lxml import etree
from sickle import Sickle

from constants import get_constants as c
from downloader import download

sickle = Sickle(c().OAI_URL())
skip = 0
while True:
    try:
        records = sickle.ListRecords(metadataPrefix='oai_dc', set='hasFile:true')
    except HTTPError as e:
        print(e)
        skip += 1
    else:
        for record in records:
            root = etree.fromstring(str(record))
            downloadlink = root.getchildren()[1].getchildren()[0].getchildren()[-2].text
            if download(downloadlink, root):
                skip = 0
            else:
                skip += 1
    if skip > 500:
        break
print("Finished")
