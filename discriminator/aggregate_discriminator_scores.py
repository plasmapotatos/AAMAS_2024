import os
import json
import numpy as np

def aggregate_discriminator_scores(base_folder):
    aggregated_scores = {}

    # Iterate over each trial_{i} folder
    for trial_subfolder in os.listdir(base_folder):
        subfolder_path = os.path.join(base_folder, trial_subfolder)
        if os.path.isdir(subfolder_path) and trial_subfolder.startswith('trial_'):
            score_file_path = os.path.join(subfolder_path, 'processed_scores.json')
            if os.path.exists(score_file_path):
                with open(score_file_path, 'r') as file:
                    trial_scores = json.load(file)
                    for plan, score in trial_scores.items():
                        if plan not in aggregated_scores:
                            aggregated_scores[plan] = []
                        aggregated_scores[plan].append(score)
            else:
                print(f"No score file found in {subfolder_path}")

    # Calculate the mean and standard deviation for each plan
    final_aggregated_results = {}
    for plan, scores in aggregated_scores.items():
        scores_array = np.array(scores)
        final_aggregated_results[plan] = {
            "mean": np.mean(scores_array),
            "std_dev": np.std(scores_array)
        }

    # Save the aggregated results to a new JSON file
    output_file = os.path.join(base_folder, 'aggregated_scores.json')
    with open(output_file, 'w') as outfile:
        json.dump(final_aggregated_results, outfile, indent=4)

    return final_aggregated_results

# Example usage
base_folder = "discriminator_results/4"  # Replace with the path to your discriminator_results folder
aggregate_discriminator_scores(base_folder)
