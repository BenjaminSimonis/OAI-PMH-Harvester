from sickle import Sickle
from sickle.oaiexceptions import IdDoesNotExist

from constants import oai_url, oai_id
from downloader import download

sickle = Sickle(oai_url)
counter = 0
skip = 0
while True:
    counter += 1
    oaid = oai_id + str(counter)
    try:
        record = sickle.GetRecord(identifier=oaid, metadataPrefix='oai_dc')
        if download(str(counter), str(record)):
            skip = 0
        else:
            skip += 1
    except IdDoesNotExist:
        skip += 1
    if skip > 500:
        break
print("Finished")
