from pykml import parser
import pandas as pd

# Path to data folder
adnan_path  = "C:/Users/hafsagureye/Downloads/HOhio/"

# Extract Transformers.kmz to file Transformers (I used 7Zip), inside should be doc.kml
filename = adnan_path + 'Poles /doc.kml'



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