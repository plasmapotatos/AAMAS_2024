import os
import json
import numpy as np
import csv

def aggregate_trial_results(example_trials, base_folder):
    csv_rows = []
    csv_header = ["Example"]  # Initialize the header for the CSV file

    aggregated_results_base = {
        "Delivery Rate": [],
        "Commonsense Constraint Micro Pass Rate": [],
        "Commonsense Constraint Macro Pass Rate": [],
        "Hard Constraint Micro Pass Rate": [],
        "Hard Constraint Macro Pass Rate": [],
        "Final Pass Rate": []
    }

    for key in aggregated_results_base:
        csv_header.append(f"{key}_mean")
        csv_header.append(f"{key}_std_dev")

    for trial_number in example_trials:
        trial_folder = os.path.join(base_folder, f'example_{trial_number}')
        if not os.path.exists(trial_folder):
            print(f"Folder {trial_folder} does not exist.")
            continue
        
        # Initialize a dictionary to store aggregated results for this example_{trial_number} folder
        aggregated_results = aggregated_results_base.copy()
        
        for trial_subfolder in os.listdir(trial_folder):
            subfolder_path = os.path.join(trial_folder, trial_subfolder)
            if os.path.isdir(subfolder_path) and trial_subfolder.startswith('trial_'):
                result_file_path = os.path.join(subfolder_path, 'final_result.json')
                if os.path.exists(result_file_path):
                    with open(result_file_path, 'r') as file:
                        trial_results = json.load(file)
                        for key in aggregated_results:
                            aggregated_results[key].append(trial_results.get(key, 0))
                else:
                    print(f"No result file found in {subfolder_path}")
        
        # Calculate the mean and standard deviation for each metric
        averaged_results = {}
        csv_row = [f"example_{trial_number}"]  # Start the row with the example folder name
        for key in aggregated_results:
            data = np.array(aggregated_results[key])
            mean = np.mean(data)
            std_dev = np.std(data)
            averaged_results[key] = {"mean": mean, "std_dev": std_dev}
            csv_row.extend([mean, std_dev])
        
        # Save the averaged results to a new JSON file inside the example_{trial_number} folder
        output_file = os.path.join(trial_folder, 'averaged_results.json')
        with open(output_file, 'w') as outfile:
            json.dump(averaged_results, outfile, indent=4)
        
        csv_rows.append(csv_row)

    # Save the results in a CSV file
    csv_output_file = os.path.join(base_folder, 'averaged_results_summary.csv')
    with open(csv_output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_header)
        writer.writerows(csv_rows)

    return True

# Example usage
example_trials = [36]  # Replace with your array of trial numbers
base_folder = "evaluation/examples_trials"  # Replace with the path to your example_trials folder
aggregate_trial_results(example_trials, base_folder)
