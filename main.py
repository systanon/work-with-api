import requests
import json

# URL = "https://catfact.ninja/facts?page=5&limit=5"
# URL = "https://restcountries.com/v3.1/all?fields=name,capital,population,region"
URL = "https://restcountries.com/v3.1/region/europe?fields=name,capital,population,region"


# {'name': {'common': 'Comoros', 'official': 'Union of the Comoros', 'nativeName': {'ara': {'official': 'الاتحاد القمري', 'common': 'القمر\u200e'}, 'fra': {'official': 'Union des Comores', 'common': 'Comores'}, 'zdj': {'official': 'Udzima wa Komori', 'common': 'Komori'}}}, 'capital': ['Moroni'], 'region': 'Africa', 'population': 869595}

def getData(url):
   responce = requests.get(url, timeout=15)
   if responce.ok:
      return structuredData(responce.json())
   else:
      print(responce.status_code)
      return []
   
def structuredData(countries):
  res = []
  for country in countries:
     res.append({
        "name": country["name"]["common"],
        "region": country["region"],
        "capital": country["capital"][0] if len(country["capital"]) > 0 else "-",
        "population": country["population"]
     })
  return res
    
def sortData(data):
   return sorted(data, key=lambda  item: item["population"], reverse=True) 

def calculatePopulation(countries):
  return sum([country["population"] for country in countries])
   

def main():
  sorted_data = sortData(getData(URL))
  sum_population = calculatePopulation(sorted_data)
  top_countries = sorted_data[:10]

  # for item in sorted_data:
  #   print(item)

  for index, country in enumerate(top_countries):
     print(f"{index + 1}. {country["capital"]} - capital: {country["name"]} - population: {country["population"]:,}")
  print("\n")   
  print(f"Total population: {sum_population:,}")
  
if __name__ == "__main__":
    main()