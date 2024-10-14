import json
import os
from tqdm import tqdm
from discriminator.run_discriminator import run_discriminator
from discriminator.parse_discriminator import parse_discriminator_results
from discriminator.spearman_evaluation import calculate_spearman_correlation

def main():
    # Ground truth order
    ground_truth_order = ["plan_14", "plan_5", "plan_9", "plan_19", 
                          "plan_23", "plan_28", "plan_34", "plan_40", "plan_42", "plan_1"]

    # Base folder for the results
    base_results_folder = "discriminator_results/4"
    
    # List to store Spearman scores for each run
    spearman_scores = []

    # Use tqdm to create a progress bar for the 10 iterations
    for i in tqdm(range(10)):
        # Create a folder for the current trial
        trial_folder = os.path.join(base_results_folder, f"trial_{i + 1}")
        os.makedirs(trial_folder, exist_ok=True)
        
        # Step 1: Run discriminator and save results to the specific trial folder
        run_discriminator(results_folder=trial_folder)  # Pass the trial folder as the results directory
        print("Discriminator results saved in '{trial_folder}'")

        # Step 2: Parse the discriminator results from the specific trial folder
        output_json_file_path = os.path.join(trial_folder, "processed_scores.json")
        output_json_file, scores = parse_discriminator_results(results_folder=trial_folder, output_json_file=output_json_file_path)

        # Step 3: Calculate Spearman rank correlation
        spearman_score = calculate_spearman_correlation(output_json_file, ground_truth_order)
        spearman_scores.append(spearman_score)

    # Save the Spearman scores to a JSON file for analysis
    with open(os.path.join(base_results_folder, "spearman_scores.json"), "w") as json_file:
        json.dump(spearman_scores, json_file, indent=4)

    print(f"Spearman scores saved in '{base_results_folder}/spearman_scores.json'")

if __name__ == "__main__":
    main()