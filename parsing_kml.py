from pykml import parser
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Path to data folder
adnan_path  = '/Users/kateherz/HackOHIO2021/'

# Extract Transformers.kmz to file Transformers (I used 7Zip), inside should be doc.kml
poles = adnan_path + 'Poles/doc.kml'
transformers = adnan_path + 'Transformers/doc.kml'



with open(poles) as f:
    docP = parser.parse(f).getroot()

namesP = []
latP = []
longP = []
for e in docP.Document.Folder.Placemark:
  coor = e.Point.coordinates.text.split(',')
  latP.append(coor[0])
  longP.append(coor[1])

with open(transformers) as f:
    docT = parser.parse(f).getroot()

namesT = []
latT = []
longT = []
for e in docT.Document.Folder.Placemark:
  coor = e.Point.coordinates.text.split(',')
  latT.append(coor[0])
  longT.append(coor[1])




plt.title("Latitude and Longtitude")  # Add a title to the axes.
plt.ylabel('Latitude')
plt.xlabel('Longtitude')
plt.grid(True)
plt.axis()

lat_nums = []
for x in latP:
  lat_nums.append(float(x))

long_nums = []
for x in longP:
  long_nums.append(float(x))

lat_numsT = []
for x in latT:
  lat_numsT.append(float(x))

long_numsT = []
for x in longT:
  long_numsT.append(float(x))

plt.scatter(lat_nums,long_nums,.5)
plt.scatter(lat_numsT,long_numsT,.5)

plt.show()