import os
from constants import get_constants as c

def parser(filename, dcrecord, path):
    md = dcrecord.getchildren()[1].getchildren()[0].getchildren()
    taglist = []
    mdlist = []
    for set in md:
        tag = str(set.tag).replace('{http://purl.org/dc/elements/1.1/}', 'dc.')
        taglist.append(tag)
        mdlist.append(set.text)
    mdwriter(filename, taglist, mdlist, path)
    pass


def mdwriter(filename, tags, mds, path):
    mddir = path + c().SLASH() + "metadata" + c().SLASH()
    os.makedirs(mddir)
    with open(mddir + "metadata.csv") as mdfile:
        mdfile.write('filename')
        for item in tags:
            mdfile.write(',' + item)
        mdfile.write('\nobjects/')
        mdfile.write(filename)
        for item in mds:
            mdfile.write(',' + item)
    pass
