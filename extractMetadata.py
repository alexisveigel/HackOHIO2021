from exif import Image
with open('1.JPG') as image_file:
    testImage = Image(image_file)

testImage.list_all()