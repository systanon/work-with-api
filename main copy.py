import json

json_data = '''
    {
  "currency": "PLN",
  "vat_rate": 0.23,
  "items": [
    { "name": "Notes A5", "qty": 2, "unit_price": 7.50 },
    { "name": "Długopis", "qty": 3, "unit_price": 2.20 },
    { "name": "Marker", "qty": 1, "unit_price": 5.90 }
  ]
}
'''

data = json.loads(json_data)



def calculateBill(data):
    currency = data["currency"]
    vat_rate = data["vat_rate"]
    res = {}
    total = 0   
    for item  in data["items"]: 
      res[item["name"]] = {
         "sum": round(item["qty"] * item["unit_price"], 2) ,
         "count": item["qty"]
      }
      total = total + (item["qty"] * item["unit_price"])
    for item in res.items():   
      print(f"{item[0]} x {item[1]["count"]} = {item[1]["sum"]}" )
    print("-------------------------------------------------------")
    print(f"Netto: {total}")
    print(f"Vat: {vat_rate * total}")
    print(f"Brutto: {total + (vat_rate* total)}")

def main():
  calculateBill(data)



  
if __name__ == "__main__":
    main()