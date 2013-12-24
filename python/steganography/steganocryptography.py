__author__ = 'yigit'

"""
hiding encrypted data in an image file
"""

import stepic
from PIL import Image

SECRET_MSG = "CONFIDENTIAL INFORMATION"


i = Image.open("moon.jpg")
i2=stepic.encode(i,SECRET_MSG)
i2.save("steganomoon.jpg","JPEG")

i2=Image.open("steganomoon.jpg")
i2.show()
i.show()