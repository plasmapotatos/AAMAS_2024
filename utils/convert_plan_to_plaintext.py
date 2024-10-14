import json

def convert_json_to_text(json_data):
    data = json.loads(json_data)
    plans = data['plans']

    plain_text = ""
    
    for plan in plans:
        plain_text += f"Query: {plan['query']}, \n\n"
        plain_text += "Travel Plan:\n"
        
        for day_plan in plan['travel_plan']:
            plain_text += f"Days: {day_plan['day']}, \n"
            plain_text += f"Current City: {day_plan['current_city']}, \n"
            
            if day_plan['transportation'] != "-":
                transport = day_plan['transportation']['details']
                plain_text += f"Transportation: {day_plan['transportation']['type']}, from {transport['from']} to {transport['to']}, Departure Time: {transport['departure_time']}, Arrival Time: {transport['arrival_time']}, cost: {transport['cost']}\n"
            else:
                plain_text += "Transportation: -, \n"
            
            meals = day_plan['meals']
            plain_text += f"Breakfast: {meals['breakfast'] if meals['breakfast'] != '-' else '-'}, \n"
            plain_text += f"Attraction: {', '.join(day_plan['attractions']) if day_plan['attractions'] != '-' else '-'}\n"
            plain_text += f"Lunch: {meals['lunch']['location']}, cost: {meals['lunch']['cost']}, cuisines: {meals['lunch']['cuisines'] if meals['lunch'] != '-' else '-'}, \n"
            plain_text += f"Dinner: {meals['dinner']['location']}, cost: {meals['dinner']['cost']}, cuisines: {meals['dinner']['cuisines'] if meals['dinner'] != '-' else '-'}, \n"
            
            if day_plan['accommodation'] != "-":
                acc = day_plan['accommodation']
                plain_text += f"Accommodation: {acc['type']}, {acc['location']}, cost: {acc['cost']}, maximum occupancy: {acc['maximum_occupancy']}, house rules: {acc['house_rules']}, minimum nights: {acc['minimum_nights']}\n"
            else:
                plain_text += "Accommodation: -, \n"
                
            plain_text += f"Number of people = {day_plan['number_of_people']}\n"
            plain_text += f"Total cost = {day_plan['total_cost']}\n"
            plain_text += f"Accommodation minimum nights:  {day_plan['day']}/{day_plan['accommodation']['minimum_nights'] if day_plan['accommodation'] != '-' else '1'}\n\n"
        
        plain_text += f"Total cost across all days = {plan['total_cost_all_days']}\n"
        plain_text += f"Cuisines: The prompt specifies no cuisines, so all cuisines constraints are satisfied\n"
    
    return plain_text

# Replace this with your JSON string
json_data = '''{
  "plans": [
    {
      "query": "Please help me plan a trip from St. Petersburg to Rockford spanning 3 days from March 16th to March 18th, 2022. The travel should be planned for a single person with a budget of $1,700.",
      "travel_plan": [
        {
          "day": 1,
          "current_city": "from St. Petersburg to Rockford",
          "transportation": {
            "type": "Flight",
            "details": {
              "number": "F3573659",
              "from": "St. Petersburg",
              "to": "Rockford",
              "departure_time": "15:40",
              "arrival_time": "17:04",
              "cost": 474
            }
          },
          "meals": {
            "breakfast": "-",
            "lunch": "-",
            "dinner": {
              "location": "Flying Mango, Rockford",
              "cost": 20,
              "cuisines": "American, BBQ, Seafood"
            }
          },
          "accommodation": {
            "type": "Private Room in a two bedroom apt.",
            "location": "Rockford",
            "cost": 210,
            "maximum_occupancy": 2,
            "house_rules": "No visitors & No smoking",
            "minimum_nights": 1
          },
          "number_of_people": 1,
          "total_cost": 704,
          "attractions": "-"
        },
        {
          "day": 2,
          "current_city": "Rockford",
          "transportation": "-",
          "meals": {
            "breakfast": {
              "location": "Grappa - Shangri-Las - Eros Hotel, Rockford",
              "cost": 21,
              "cuisines": "Bakery, Desserts, Italian"
            },
            "lunch": {
              "location": "Gajalee Sea Food, Rockford",
              "cost": 49,
              "cuisines": "Bakery, BBQ"
            },
            "dinner": {
              "location": "Aroma Rest O Bar, Rockford",
              "cost": 58,
              "cuisines": "Bakery, Fast Food, Chinese, American, Seafood"
            }
          },
          "accommodation": {
            "type": "Private Room in a two bedroom apt.",
            "location": "Rockford",
            "cost": 210,
            "maximum_occupancy": 2,
            "house_rules": "No visitors & No smoking",
            "minimum_nights": 1
          },
          "number_of_people": 1,
          "total_cost": 338,
          "attractions": ["Anderson Japanese Gardens, Rockford", "Midway Village Museum, Rockford"]
        },
        {
          "day": 3,
          "current_city": "from Rockford to St. Petersburg",
          "transportation": {
            "type": "Flight",
            "details": {
              "number": "F3573120",
              "from": "Rockford",
              "to": "St. Petersburg",
              "departure_time": "19:00",
              "arrival_time": "22:43",
              "cost": 346
            }
          },
          "meals": {
            "breakfast": {
              "location": "Dial A Cake, Rockford",
              "cost": 29,
              "cuisines": "Cafe, American, Mediterranean, Desserts"
            },
            "lunch": {
              "location": "Subway, Rockford",
              "cost": 26,
              "cuisines": "Bakery, Pizza, BBQ, Desserts"
            },
            "dinner": {
              "location": "Moets Arabica, Rockford",
              "cost": 43,
              "cuisines": "Tea, Bakery, Indian, Fast Food"
            }
          },
          "accommodation": "-",
          "number_of_people": 1,
          "total_cost": 444,
          "attractions": ["Ethnic Heritage Museum, Rockford", "Blackhawk Springs Forest Preserve, Rockford"]
        }
      ],
      "total_cost_all_days": 1486,
      "cuisines_constraints_satisfied": true
    }
  ]
}'''

plain_text_plan = convert_json_to_text(json_data)
print(plain_text_plan)