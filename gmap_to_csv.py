import requests
import json
import csv
import io

f = io.open('restaurants.csv', 'w', encoding="utf-8", newline='')
writer = csv.writer(f)
writer.writerow(["name", "latitude", "longitude", "rating", "number of reviews", "affluence"])


radius = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,50000,100000,200000,3000000]



for r in radius:
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=23.8103,90.4125&radius=' + str(r) +'Your_API_Key'


    data = requests.get(url)

    text = data.json()

    for word in text["results"]:
        latitude = word["geometry"]["location"]["lat"]
        longitude = word["geometry"]["location"]["lng"]
        name = word['name']
        
        affluence = word.get("price_level", 'No Price Level')

        rating = word.get('rating', 'Rating missing')
        users_rated = word.get('user_ratings_total', 'No of ratings missing')

        writer.writerow([name, latitude, longitude, rating, users_rated, affluence])


f.close()