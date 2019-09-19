
import base64
import hashlib
import re
import urllib.parse
def basesixty():
    
    print("Input lfi string to encode: ")
    string = input().encode("utf-8")
    encodedstring = base64.b64encode(string)
    print(encodedstring)


def urlencoding():
    print("input lfi string to encode: ")
    string = input().encode("utf-8")
    result = urllib.parse.quote_plus(string, safe='')
    print(result)

def hex():
    print("input lfi string to encode: ")
    string = input().encode("utf-8")
    hexed = string.hex()
    print("payload is: ")
    print(hexed)