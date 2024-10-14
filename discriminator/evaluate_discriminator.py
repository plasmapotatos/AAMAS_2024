import os
import json

# Define the predefined array
predefined_array = ["plan_14", "plan_5", "plan_9"]

# Function to find the highest-rated plan
def find_highest_rated_plan(scores):
    return max(scores, key=scores.get)

# Main function to check the highest rated plans
def check_highest_rated_plans(folder_path):
    found_in_predefined_array = 0

    for i in range(1, 11):  # Loop through trial_1 to trial_10
        trial_folder = os.path.join(folder_path, f"trial_{i}")
        if os.path.exists(trial_folder):
            processed_scores_path = os.path.join(trial_folder, "processed_scores.json")
            if os.path.exists(processed_scores_path):
                with open(processed_scores_path, 'r') as f:
                    scores = json.load(f)
                highest_rated_plan = find_highest_rated_plan(scores)
                if highest_rated_plan in predefined_array:
                    found_in_predefined_array += 1

    return found_in_predefined_array

# Example usage:
folder_path = "discriminator_results/4"  # Replace with the actual folder path
count = check_highest_rated_plans(folder_path)
print(f"The highest-rated plan was found in the predefined array {count} times.")
