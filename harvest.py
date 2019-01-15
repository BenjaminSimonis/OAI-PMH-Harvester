from sickle import Sickle
from sickle.oaiexceptions import IdDoesNotExist

from constants import oai_url, oai_id
from downloader import download

sickle = Sickle(oai_url)
counter = 1
skip = 0
while True:
    oaid = oai_id + str(counter)
    try:
        record = sickle.GetRecord(identifier=oaid, metadataPrefix='oai_dc')
        if download(str(counter), str(record)):
            skip = 0
        else:
            skip += 1
        counter += 1
    except IdDoesNotExist:
        skip += 1
        if skip > 50:
            break
print("Finished")
