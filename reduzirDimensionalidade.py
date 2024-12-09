"""Simplified function for converting color images to grayscale.

The functionality was based on the articles on wike and examples of how to process images on the web.

wiki in English:

https://en.wikipedia.org/wiki/Grayscale#Numerical_representations

wiki in Portuguese:
https://pt.wikipedia.org/wiki/N%C3%ADvel_de_cinza#Convertendo_a_cor_em_n%C3%ADvel_de_cinza"""

import os
from PIL import Image

ENTRANCE_DIR = "ImageToImport"
EXIT_DIR = "ImageToExport"

#
# read de coloured image to import
#
def File_to_Import(imageFileName):
    return os.path.join(ENTRANCE_DIR, imageFileName)

#
# write de coloured image to import
#
def File_to_export(imageFileName):
    return os.path.join(EXIT_DIR, imageFileName)

#
# Convert to grayscale
#
def Convert_to_grayScale(coloredImage):
    imageWidth, ImageHigh = coloredImage.size
    grayScaledImage = Image.new("RGB", (imageWidth, ImageHigh))

    for col in range(imageWidth):
        for lin in range(ImageHigh):
            imagePixel = coloredImage.getpixel((col, lin))
            # source: https://en.wikipedia.org/wiki/Grayscale#Numerical_representations
            imageLuminance = (int(imagePixel[0]*0.2126) + int(imagePixel[1]*0.7152) + int(imagePixel[2]*0.0722))
            # https://pt.wikipedia.org/wiki/N%C3%ADvel_de_cinza#:~:text=Em%20computa%C3%A7%C3%A3o%2C%20uma%20imagem%20digital,de%20um%20espa%C3%A7o%20de%20cores.
            # imageLuminance = (int(imagePixel[0]*0.3) + int(imagePixel[1]*0.59) + int(imagePixel[2]*0.11))

            #print(imageLuminance)
            grayScaledImage.putpixel((col, lin), (imageLuminance, imageLuminance, imageLuminance ))
    return grayScaledImage


if __name__== "__main__":
    imageLoaded = Image.open(File_to_Import("RostoColorido_1647x1706.jpg"))
    imageToSave = Convert_to_grayScale(imageLoaded)
    imageToSave.save(File_to_export("RostoGrayScale.jpg"))
    imageToSave.show()
