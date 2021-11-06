from GPSPhoto import gpsphoto
import os

#function to output [photo, lat, lon]
def getLatLon(photo):
    data = gpsphoto.getGPSData(photo)
    latitude = data['Latitude']
    longitude = data['Longitude']
    set = [latitude, longitude]
    return set

fileList = []
alexisDirectory = 'C:\HackOHIO2021\AEPjpegs'
for files in os.listdir(alexisDirectory):
    example = alexisDirectory + "\\" + files
    set = getLatLon(example)
    name = [files]
    table = name + set
    print(table)


#i = 0 #counter
#while i < listSize: #build list of coords
    #print(getLatLon(fileList(i)))
    #i += 1


