from exif import Image
with open('1.JPG', 'rb') as image_file:
    testImage = Image(image_file)

dir(image_file)