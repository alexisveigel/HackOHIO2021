from GPSPhoto import gpsphoto

#create function
def getLatLon(photo):
    data = gpsphoto.getGPSData(photo)
    latitude = data['Latitude']
    longitude = data['Longitude']
    set = [photo, latitude, longitude]
    return set

coordList = getLatLon('1.JPG')
print(coordList)