import csv
import pyperclip

def find_restaurant_info(restaurant_name, csv_file_path):
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            if row['Name'].strip().lower() == restaurant_name.strip().lower():
                cost = row['Average Cost']
                cuisines = row['Cuisines']
                result = f"""cost: {cost}, cuisines: "{cuisines}" """
                pyperclip.copy(result)
                return result
        
        return "Restaurant not found"

# Example usage
restaurant_name = "Rupa Bangali Dhaba"
csv_file_path = "database/restaurants/clean_restaurant_2022.csv"
print(find_restaurant_info(restaurant_name, csv_file_path))
