
__author__ = 'yigit'

"""
hiding encrypted data in an image file
"""

import stepic
from PIL import Image
from Crypto.Hash import SHA256

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

def test_if_match(data, secret_msg):
    """
    test if strings are a match and print
    """
    if data == secret_msg:
        print "[+] match"
    else:
        print "[-] not a match"

def sha_crypt_msg(input):
    """
    encrypts the input string with SHA256 and then returns hash
    """
    hash = SHA256.new()
    hash.update(input)
    output = hash.hexdigest()
    return output

msg = sha_crypt_msg(SECRET_MSG)
create_encoded_image(X, msg, Y)
data = decode_message(Y)
test_if_match(data, msg)