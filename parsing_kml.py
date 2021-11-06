from pykml import parser
import pandas as pd

adnan_path  = "C:/Users/adnanreddy/Downloads/HOhio/"

filename = adnan_path+'Transformers/doc.kml'



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

print(df.head())