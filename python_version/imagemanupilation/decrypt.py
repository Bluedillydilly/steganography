from PIL import Image
import numpy

def decrypt(image=Image.open("testPNG.png")):
    """
       Gets a message from an image. WIP
    """
    message = ""
    image.show()
    pix_array = numpy.array(image)
    print(pix_array)
    for i in range(40):
        image.load()[i, i] = (0, 0, 0, 0)


decrypt()
