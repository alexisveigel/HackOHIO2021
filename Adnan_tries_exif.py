from PIL import Image
from PIL.ExifTags import TAGS

adnan_path  = "C:/Users/adnanreddy/Downloads/HOhio/"
file = adnan_path+'1.JPG'
image = Image.open(file)
exifdata = image.getexif()

"""
def get_exif(image_file_path):
    exif_table = {}
    image = Image.open(image_file_path)
    info = image.getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        exif_table[decoded] = value
        gps_info = {}
        for key in exif_table['GPSInfo'].keys():
            decode = GPSTAGS.get(key,key)
            gps_info[decode] = exif_table['GPSInfo'][key]
    return gps_info
"""
image = Image.open(file)
exif = image.getexif()

print(exif['GPSInfo'])

#print(get_exif(file))
print('>> Here! <<')