import json
import requests
import datetime

def get_weather(city):
    try:
        url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": "96d9fb570356b99223f270108248b609",
            "units": "metric"
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()

        #print(json.dumps(data, indent=2, ensure_ascii=False))
        wether ={"city": city, "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") ,"temperature" :data["main"]["temp"], "humidity": data["main"]["humidity"], "clouds": data["clouds"]["all"]}
        return wether
    except requests.exceptions.Timeout:
        print("Сервер перегружен")
    except requests.exceptions.ConnectionError:
        print("Проблемы с интернетом")


result = get_weather(city="Moscow")
print(result)

try:
    with open("history.json", "r", encoding="utf-8") as f:
        history = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    history = []

history.append(result)

with open("history.json", "w", encoding="utf-8") as f:
    json.dump(history, f, ensure_ascii=False, indent=2)


