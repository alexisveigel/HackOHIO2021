from GPSPhoto import gpsphoto
import pandas as pd


#create function
def getLatLon(photo):
    data = gpsphoto.getGPSData(photo)
    latitude = data['Latitude']
    longitude = data['Longitude']
    set = [photo, latitude, longitude]
    return set

coordList = getLatLon('1.JPG')
print(coordList)