"""Simplified function for converting color images to grayscale.

The functionality was based on the articles on wike and examples of how to process images on the web.

wiki in English:

https://en.wikipedia.org/wiki/Grayscale#Numerical_representations

wiki in Portuguese:
https://pt.wikipedia.org/wiki/N%C3%ADvel_de_cinza#Convertendo_a_cor_em_n%C3%ADvel_de_cinza

Image
author: Michael Dam 
"https://unsplash.com/pt-br/@michaeldam?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash"
photo:
"https://unsplash.com/pt-br/fotografias/closeup-photography-of-woman-smiling-mEZ3PoFGs_k?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
      
"""

import os
from PIL import Image

if __name__== "__main__":
    imageLoaded = Image.open("RostoColorido_1647x1706.jpg")
    imageLoaded.show()

    #
    # Convert to grayscale
    #
    imageWidth, ImageHigh = imageLoaded.size
    grayScaledImage = Image.new("RGB", (imageWidth, ImageHigh))

    for col in range(imageWidth):
        for lin in range(ImageHigh):
            imagePixel = imageLoaded.getpixel((col, lin))
            # source: https://en.wikipedia.org/wiki/Grayscale#Numerical_representations
            imageLuminance = (int(imagePixel[0]*0.2126) + int(imagePixel[1]*0.7152) + int(imagePixel[2]*0.0722))
            # https://pt.wikipedia.org/wiki/N%C3%ADvel_de_cinza#:~:text=Em%20computa%C3%A7%C3%A3o%2C%20uma%20imagem%20digital,de%20um%20espa%C3%A7o%20de%20cores.
            # imageLuminance = (int(imagePixel[0]*0.3) + int(imagePixel[1]*0.59) + int(imagePixel[2]*0.11))

            grayScaledImage.putpixel((col, lin), (imageLuminance, imageLuminance, imageLuminance ))

    grayScaledImage.save("GrayScaleFace.jpg")
    grayScaledImage.show()
    #
    # Convert to Binary
    #
    imageWidth, ImageHigh = grayScaledImage.size
    binaryImage = Image.new("RGB", (imageWidth, ImageHigh))

    for col in range(imageWidth):
        for lin in range(ImageHigh):
            imagePixel = grayScaledImage.getpixel((col, lin))
            if imagePixel[0] > 125:
                binaryImage.putpixel((col, lin), (255, 255, 255))
            else:
                binaryImage.putpixel((col, lin), (0, 0, 0))

    binaryImage.save("binaryFace.jpg")
    binaryImage.show()
