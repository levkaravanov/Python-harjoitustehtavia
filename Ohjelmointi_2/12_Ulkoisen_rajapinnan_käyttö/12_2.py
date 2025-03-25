import requests

city_name = input("Anna kaupungin nimi: ")
limit = 5
API_key = "ee35f837d1942ff4161408732bc92951"

city = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={API_key}"

try:
    vastaus = requests.get(city)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        if json_vastaus:
            kaupunki = json_vastaus[0]
            nimi = kaupunki['name']
            lat = kaupunki['lat']
            lon = kaupunki['lon']

            weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_key}"
            vastaus = requests.get(weather)
            if vastaus.status_code == 200:
                json_vastaus = vastaus.json()
                if json_vastaus:
                    astet = json_vastaus['main']['temp']
                    säätila = json_vastaus['weather'][0]['description']

                    print(f"Nyt sää kaupungissa {nimi} on {säätila}, {round(astet)}°C")
                else:
                    print("Säätietoja ei löytynyt.")
            else:
                print("Säätietoja ei voitu hakea.")
        else:
            print("Kaupunkia ei löytynyt.")
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")