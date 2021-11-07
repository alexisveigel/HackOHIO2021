from GPSPhoto import gpsphoto
data = gpsphoto.getGPSData('1.JPG')
print(data['RefLatitude'], data['Longitude'])