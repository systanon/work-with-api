import requests
import os
import json
import threading

URL = "https://restcountries.com/v3.1/region/europe3?fields=name,capital,population,region"

FILE = "fallback.json"

FILE_PATH = os.path.join(os.path.dirname(__file__), FILE)

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)



def saveFallbackDataAsync(data):
    threading.Thread(target=saveFallbackData, args=(data,), daemon=True).start()


def loadFallbackData():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        print("Error load fallback data")
        return []
    else:
        print("Fallback data is loaded")
        return data


def saveFallbackData(data):
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except:
        print("Error save fallback data")
    else:
        print("Fallback data is saved")


def getData(url):
    responce = requests.get(url, timeout=15)
    if responce.ok:
        data = responce.json()
        saveFallbackDataAsync(data)
        return structuredData(data)
    else:
        print(f"The request failed satus: {responce.status_code}")
        fallback = loadFallbackData()
        return structuredData(fallback)


def structuredData(countries):
    res = []
    for country in countries:
        res.append(
            {
                "name": country["name"]["common"],
                "region": country["region"],
                "capital": (
                    country["capital"][0] if len(country["capital"]) > 0 else "-"
                ),
                "population": country["population"],
            }
        )
    return res


def sortData(data):
    return sorted(data, key=lambda item: item["population"], reverse=True)


def calculatePopulation(countries):
    return sum([country["population"] for country in countries])


def main():
    sorted_data = sortData(getData(URL))
    sum_population = calculatePopulation(sorted_data)
    top_countries = sorted_data[:10]

    for index, country in enumerate(top_countries):
        print(
            f"{index + 1}. {country["capital"]} - capital: {country["name"]} - population: {country["population"]:,}"
        )
    print("\n")
    print(f"Total population: {sum_population:,}")


if __name__ == "__main__":
    main()
