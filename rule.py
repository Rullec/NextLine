'''
define rule for cleaning string
'''
import re

def rule(str):
    #print(str.encode('utf-8'))

    # remove -
    str = re.sub(r"-\n", "", str)

    # remove \n
    str = re.sub(r"\x02", "", str)
    str = re.sub("\r\n", " ", str)

    # remove space after dot
    str = re.sub("\. ", ".", str)

    # remove space before (
    str = re.sub(" \(", "(", str)

    return str