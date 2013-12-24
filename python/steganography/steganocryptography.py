__author__ = 'yigit'

"""
hiding encrypted data in an image file
"""

import stepic
from PIL import Image

SECRET_MSG = "CONFIDENTIAL INFORMATION"
# X is original image
# Y is encoded image
X = "moon.jpg"
Y = "steganomoon.png" #stepic works better with png files!


def create_encoded_image(input, message, output):
    """
    creates an encoded image (output file)
    """
    i = Image.open(input)
    i2 = stepic.encode(i, message)
    i2.save(output),


def decode_message(file):
    """
    returns the message in the file
    """
    i = Image.open(file)
    data = stepic.decode(i)
    msg = data.decode()
    return msg


create_encoded_image(X, SECRET_MSG, Y)
data = decode_message(Y)

if data == SECRET_MSG:
    print "[+] match"
else:
    print "[-] not a match"