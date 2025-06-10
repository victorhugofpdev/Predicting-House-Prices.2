import json
import pandas as pd

def read_json_as_string(file_path):
    with open(file_path, 'r') as file:
        json_string = file.read()
    return json_string

# Example usage
file_path = 'realties.json'
json_string = read_json_as_string(file_path)
dict_json = {"state": [], "city": [], "neighborhood": [],"street": [], "price": [], "area": [], "rooms": [], "bathrooms": [], "garage": [], "description": [], "url": [], "number": [], "done": [], "furnished": [], "type": []} 
for line in json_string.split('\n'):
    try:
        result = line.split(":")
        result_middle = result[1].split(",")
        result_final = result_middle[0]
        result_final = eval(result_final)
    except:
        result_final = 'null'
    if "state" in line:
        dict_json["state"].append(result_final)
    elif "city" in line:
        dict_json["city"].append(result_final)
    elif "neighborhood" in line:
        dict_json["neighborhood"].append(result_final)
    elif "street" in line:
        dict_json["street"].append(result_final)
    elif "realty_number" in line:
        dict_json["number"].append(result_final)
    elif "realty_square_footage"in line:
        dict_json["area"].append(result_final)
    elif "realty_price" in line:
        try:
           dict_json["price"].append(result_final)
        except:
           dict_json["price"].append('null')
    elif "realty_description"in line:
        dict_json["description"].append(result_final)
    elif "realty_parking_spaces" in line:
        try:
           dict_json["garage"].append(result_final)
        except:
           dict_json["garage"].append('null')
    elif "realty_bathrooms" in line:
        dict_json["bathrooms"].append(result_final)
    elif "realty_bedrooms" in line:
        dict_json["rooms"].append(result_final)
    elif "realty_done" in line:
        dict_json["done"].append(result_final)
    elif "realty_furnished" in line:
        dict_json["furnished"].append(result_final)
    elif "realty_url" in line:
        result_middle = line.split("/")
        result = result_middle[2] + "/" + result_middle[3] + "/" + result_middle[4]
        dict_json["url"].append(result)
    elif "realty_type" in line:
        dict_json["type"].append(result_final)
    
print(dict_json)
df = pd.DataFrame(dict_json)

df.to_csv('realties.csv', index=False)
