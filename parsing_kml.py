from pykml import parser
import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np

# Path to data folder
<<<<<<< HEAD
adnan_path  = 'C:/Users/adnanreddy/Downloads/HOhio/'

# Extract Transformers.kmz to file Transformers (I used 7Zip), inside should be doc.kml
poles = adnan_path + 'Poles/doc.kml'
transformers = adnan_path + 'Transformers/doc.kml'
conductors = adnan_path + 'Primary_Conductor/doc.kml'
=======
user_path  = '/Users/hafsagureye/Documents/HOhio/'

# Extract Transformers.kmz to file Transformers (I used 7Zip), inside should be doc.kml
poles = user_path + 'Poles/doc.kml'
transformers = user_path + 'Transformers/doc.kml'
>>>>>>> b1744e9a1d06087c2a4e3d2a0ff24903086c50dc


# /Users/kateherz/Documents/HACKOHIO2021/

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

# with open(conductors) as f:
#   docC = parser.parse(f).getroot()

# namesC = []
# latC = []
# longC = []
# for e in docC.Document.Folder.Placemark:
#   coor = e.Point.coordinates.text.split(',')
#   latC.append(coor[0])
#   longC.append(coor[1])

# plt.title("Latitude and Longtitude")  # Add a title to the axes.
# plt.ylabel('Latitude')
# plt.xlabel('Longtitude')
# plt.grid(True)
# plt.axis()

lat_numsP = []
for x in latP:
  lat_numsP.append(float(x))

long_numsP = []
for x in longP:
  long_numsP.append(float(x))

lat_numsT = []
for x in latT:
  lat_numsT.append(float(x))

long_numsT = []
for x in longT:
  long_numsT.append(float(x))

<<<<<<< HEAD
# lat_numsC = []
# for x in latC:
#   lat_numsC.append(float(x))

# long_numsC = []
# for x in longC:
#   long_numsC.append(float(x))

# plt.scatter(lat_nums,long_nums,.5)
# plt.scatter(lat_numsT,long_numsT,.5)

# plt.show()

df_p = pd.DataFrame()
df_p['Latitude'] = lat_numsP
df_p['Longitude'] = long_numsP

df_t = pd.DataFrame()
df_t['Latitude'] = lat_numsP
df_t['Longitude'] = long_numsP

# df_c = pd.DataFrame()
# df_c['Latitude'] = lat_numsC
# df_c['Longitude'] = long_numsC
=======
plt.scatter(lat_nums,long_nums,.5, label = "Pole")
plt.scatter(lat_numsT,long_numsT,.5, label = "Transformers")
plt.legend(loc='upper right', shadow=True, fontsize='medium')
>>>>>>> b1744e9a1d06087c2a4e3d2a0ff24903086c50dc

df_p.to_csv(path_or_buf='poles.csv')
df_t.to_csv(path_or_buf='transformers.csv')
# df_c.to_csv(path_or_buf='conductors.csv')