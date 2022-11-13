#Follow me @SudoJvck
#First,You need the Callsign of the airplane you want to track
#You can get this @ https://opensky-network.org/aircraft-database
#You will need the Model S Hexcode of the Aircraft
#We will use the FTX Scammer's Private Plane which is 0b142

#First, we need to get the longitude & latitude of the plane
''''
import requests
data = requests.get("https://opensky-network.org/api/states/all?time=0&icao24=HEX CODE OF AIRCRAFT YOU WANT TO TRACK").json()
if data["states"] != None:
  print(f"The longitude of the plane is: {data['states'][0][5]}")
  print(f"The latitude of the plane is: {data['states'][0][6]}")
  
else:
  print("The plane is currently on the ground!")print("The plane is currently on the ground!")
'''

#Import modules below
import requests
import time
import folium

#Define function to display plane routes using folium
def generate_map(points):
    map = folium.Map(location=[0,0], zoom_start=2)
    folium.PolyLine(points, color='black').add_to(map)
    map.save("map.html")
  
points = []

#Make request to OpenNetwork API
#Print values;Even if non to display
#Define 60 second loop
while True:
    data = requests.get("https://opensky-network.org/api/states/all?time=0&icao24=0b142").json()  
  
    if data["states"] != None:
        points.append((data['states'][0][6], data['states'][0][5]))
      
        generate_map(points)
    
    else:
      print("The plane is currently on the ground!") 
      time.sleep(60)

#The output will only display data if the aircraft is in the air
#Status will update every minute
