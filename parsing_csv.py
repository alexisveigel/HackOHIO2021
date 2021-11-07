from pykml import parser
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Path to data folder
user_path  = '/Users/hafsagureye/Documents/HOhio/'

# Extract Transformers.kmz to file Transformers (I used 7Zip), inside should be doc.kml
poles = user_path + 'Poles/doc.kml'
transformers = user_path + 'Transformers/doc.kml'
conductors = user_path + 'Primary_Conductor/doc.kml'


# /Users/kateherz/Documents/HACKOHIO2021/

#retrieve
with open(poles) as f:
     docP = parser.parse(f).getroot()

namesP = []
latP = []
longP = []
for e in docP.Document.Folder.Placemark:
  coor = e.Point.coordinates.text.split(',')
  latP.append(coor[1])
  longP.append(coor[0])

with open(transformers) as f:
     docT = parser.parse(f).getroot()

namesT = []
latT = []
longT = []
for e in docT.Document.Folder.Placemark:
  coor = e.Point.coordinates.text.split(',')
  latT.append(coor[1])
  longT.append(coor[0])

with open(conductors) as f:
     docC = parser.parse(f).getroot()


namesC = []
latC = []
longC = []

for e in docC.Document.Folder.Placemark:
  coor = e.MultiGeometry.LineString.coordinates.text.split(',')
  latC.append(coor[1])
  longC.append(coor[0])


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

lat_numsC = []
for x in latC:
  lat_numsC.append(float(x))

long_numsC = []
for x in longC:
  long_numsC.append(float(x))

df_p = pd.DataFrame()
df_p['Longitude'] = lat_nums
df_p['Latitude'] = long_nums

df_t = pd.DataFrame()
df_t['Latitude'] = lat_numsT
df_t['Longitude'] = long_numsT

df_c = pd.DataFrame()
df_c['Latitude'] = lat_numsC
df_c['Longitude'] = long_numsC

df_p.to_csv(path_or_buf='poles.csv')
df_t.to_csv(path_or_buf='transformers.csv')
df_c.to_csv(path_or_buf='conductors.csv')


plt.scatter(lat_numsC,long_numsC,.5, label = "Conductors")
plt.scatter(lat_nums,long_nums,.5, label = "Pole")
plt.scatter(lat_numsT,long_numsT,.5, label = "Transformers")
plt.legend(loc='upper right', shadow=True, fontsize='medium')

plt.show()