from pykml import parser
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Path to data folder
adnan_path  = '/Users/hafsagureye/Documents/HOhio/'

# Extract Transformers.kmz to file Transformers (I used 7Zip), inside should be doc.kml
filename = adnan_path + 'Poles/doc.kml'

# /Users/hafsagureye/Documents/HOhio

with open(filename) as f:
    doc = parser.parse(f).getroot()

names = []
lat = []
long = []
for e in doc.Document.Folder.Placemark:
  coor = e.Point.coordinates.text.split(',')
  lat.append(coor[0])
  long.append(coor[1])

df = pd.DataFrame()
df['latitude'] = lat
df['longitude'] = long

#latArr = []
#longArr = []

#latArr['latitude'] = lat
#longArr['longitude'] = long

print(df.head())

#floatX = lat.astype(float)


#floatY = long.astype(float)
x = 0

y = 0

latF = float(lat[x])

longF = float(long[y])
  
plt.ylabel('Latitiude')
plt.xlabel('Longitude')
plt.title('Latitude and Longitude')

for x in latF:
  for y in longF:
    plt.scatter(lat[x], lat[y])

#for i in longF:
  #float(long[i])

#plt.plot(df['latitude'], df['longitude'],'ro')
#plt.scatter([latF], [longF])
#plt.scatter(latArr, latArr)
plt.xlim(-100, 10)
plt.ylim(-100, 10)

#plt.axis([0, 10], [0, 10])
plt.grid(True)
plt.show()