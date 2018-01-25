import yaml

def source(ymlfile):
    opened = open(ymlfile,'r')
    res = yaml.load(opened)
    opened.close()
    return res
