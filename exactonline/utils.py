import base64
import os

def getFileName(path):
    return os.path.basename(path)

def encodeFileToB64(path):

    f = open(path, 'rb')
    fRead = f.read()
    fEncode = base64.encodebytes(fRead)
    fString = fEncode.decode('utf-8')

    return fString