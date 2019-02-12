

def parser(filelist, dcrecord, path):
    md = dcrecord.getchildren()[1].getchildren()[0].getchildren()
    dclist = {}
    for set in md:
        dclist[set.tag] = set.text
    print(dclist)
    pass