import json
import os
import pickle
import sys

from utils.langfun_request import langfun_request_by_day, query_langfun

if __name__ == "__main__":
    print(
        """"[\n \"Day(\n day = 1,\n current_city = 'from Chattanooga to Atlanta',\n transportation = SelfDriving(\n mode = 'self-driving',\n departure_city = 'Chattanooga',\n arrival_city = 'Atlanta'\n ),\n breakfast = None,\n attraction = Attraction(\n name = 'World of Coca-Cola',\n city = 'Atlanta'\n ),\n lunch = Meal(\n name = 'Baba Au Rhum',\n cuisine = 'Desserts, Pizza, Mexican, BBQ, Fast Food',\n city = 'Atlanta'\n ),\n dinner = Meal(\n name = 'Saffron',\n cuisine = 'Tea, Cafe, Fast Food, Seafood',\n city = 'Atlanta'\n ),\n accommodation = Accomodation(\n name = 'Bright, Modern, Clean, Spacious, Brooklyn Home',\n city = 'Atlanta'\n )\n)\",\n \"Day(\n day = 2,\n current_city = 'Atlanta',\n transportation = '-',\n breakfast = Meal(\n name = \\"Sizzler's Ranch\\",\n cuisine = 'Tea, Cafe, Indian, Italian',\n city = 'Atlanta'\n ),\n attraction = Attraction(\n name = 'Georgia Aquarium',\n city = 'Atlanta'\n ),\n lunch = Meal(\n name = 'Asian Bistro',\n cuisine = 'Tea, Bakery, Seafood',\n city = 'Atlanta'\n ),\n dinner = Meal(\n name = 'Pizza Central',\n cuisine = 'Cafe, Bakery, BBQ, Fast Food, Chinese, Indian',\n city = 'Atlanta'\n ),\n accommodation = Accomodation(\n name = 'Bright, Modern, Clean, Spacious, Brooklyn Home',\n city = 'Atlanta'\n )\n)\",\n \"Day(\n day = 3,\n current_city = 'from Atlanta to Decatur',\n transportation = SelfDriving(\n mode = 'self-driving',\n departure_city = 'Atlanta',\n arrival_city = 'Decatur'\n ),\n breakfast = Meal(\n name = 'Daawat-e-Kashmir',\n cuisine = 'Cafe, Pizza, American, Seafood',\n city = 'Atlanta'\n ),\n attraction = Attraction(\n name = 'Atlanta Botanical Garden',\n city = 'Atlanta'\n ),\n lunch = Meal(\n name = 'Saut\u00e9e Stories',\n cuisine = 'Desserts, Tea, Fast Food, Chinese, Seafood',\n city = 'Atlanta'\n ),\n dinner = Meal(\n name = 'El Pistolero',\n cuisine = 'Pizza, American, Fast Food',\n city = 'Atlanta'\n ),\n accommodation = Accomodation(\n name = 'Bright, Modern, Clean, Spacious, Brooklyn Home',\n city = 'Atlanta'\n )\n)\",\n \"Day(\n day = 4,\n current_city = 'Decatur',\n transportation = '-',\n breakfast = Meal(\n name = 'Cafe Coffee Day',\n cuisine = 'Tea, Cafe, BBQ, Mediterranean',\n city = 'Decatur'\n ),\n attraction = Attraction(\n name = 'Decatur Square',\n city = 'Decatur'\n ),\n lunch = Meal(\n name = 'Dawat-E-Chaman',\n cuisine = 'Chinese, BBQ, Fast Food, Cafe, Mediterranean',\n city = 'Decatur'\n ),\n dinner = Meal(\n name = 'Carnatic Cafe',\n cuisine = 'Cafe, Indian, Desserts',\n city = 'Decatur'\n ),\n accommodation = Accomodation(\n name = 'Cozy Private Room',\n city = 'Decatur'\n )\n)\",\n \"Day(\n day = 5,\n current_city = 'from Decatur to Augusta',\n transportation = SelfDriving(\n mode = 'self-driving',\n departure_city = 'Decatur',\n arrival_city = 'Augusta'\n ),\n breakfast = Meal(\n name = 'Carnatic Cafe',\n cuisine = 'Cafe, Indian, Desserts',\n city = 'Decatur'\n ),\n attraction = Attraction(\n name = 'Clyde Shepherd Nature Preserve',\n city = 'Decatur'\n ),\n lunch = Meal(\n name = 'Cafe Coffee Day',\n cuisine = 'Tea, Cafe, BBQ, Mediterranean',\n city = 'Decatur'\n ),\n dinner = Meal(\n name = 'Shake Eat Up',\n cuisine = 'Pizza, Mexican, BBQ, Fast Food, Chinese, Seafood',\n city = 'Augusta'\n ),\n accommodation = Accomodation(\n name = 'Perfect Chanukah apartment for the whole crew!',\n city = 'Augusta'\n )\n)\",\n \"Day(\n day = 6,\n current_city = 'from Augusta to Chattanooga',\n transportation = SelfDriving(\n mode = 'self-driving',\n departure_city = 'Augusta',\n arrival_city = 'Chattanooga'\n ),\n breakfast = Meal(\n name = \\"B Merrell's\\",\n cuisine = 'Tea, Pizza, Desserts, Fast Food',\n city = 'Augusta'\n ),\n attraction = Attraction(\n name = 'Augusta Riverwalk',\n city = 'Augusta'\n ),\n lunch = Meal(\n name = \\"Vinny Vanucchi's\\",\n cuisine = 'Desserts, Fast Food, Chinese, Indian, Seafood',\n city = 'Augusta'\n ),\n dinner = Meal(\n name = 'Fish Tales Lakeside Grille',\n cuisine = 'Tea, Cafe, Bakery, Desserts',\n city = 'Augusta'\n ),\n accommodation = '-'\n)\",\n \"Day(\n day = 7,\n current_city = 'Chattanooga',\n transportation = '-',\n breakfast = Meal(\n name = \\"B Merrell's\\",\n cuisine = 'Tea, Pizza, Desserts, Fast Food',\n city = 'Augusta'\n ),\n attraction = Attraction(\n name = 'Phinizy Swamp Nature Park',\n city = 'Augusta'\n ),\n lunch = Meal(\n name = \\"Vinny Vanucchi's\\",\n cuisine = 'Desserts, Fast Food, Chinese, Indian, Seafood',\n city = 'Augusta'\n ),\n dinner = Meal(\n name = 'Fish Tales Lakeside Grille',\n cuisine = 'Tea, Cafe, Bakery, Desserts',\n city = 'Augusta'\n ),\n accommodation = '-'\n)\"\n]"""
    )
