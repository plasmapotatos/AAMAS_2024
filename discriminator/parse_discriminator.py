import os
import re
import json

def parse_discriminator_results(results_folder="discriminator_results", output_json_file="processed_scores.json"):
    """
    Parses discriminator result files to extract scores from <output> tags and optionally saves them to a JSON file.
    
    Args:
        results_folder (str): Path to the folder containing result files.
        output_json_file (str): Path to the output JSON file where parsed scores will be saved.
        
    Returns:
        dict: A dictionary containing the parsed scores with the file names as keys.
    """
    # Dictionary to store the parsed scores
    scores_dict = {}

    # Regex pattern to match the score within <output> tags
    score_pattern = re.compile(r'<output>(\d{1,3})</output>')

    # Loop through all the result files in the results folder
    for result_file in os.listdir(results_folder):
        if result_file.endswith("_result.txt"):
            # Load the result content
            result_path = os.path.join(results_folder, result_file)
            with open(result_path, "r") as f:
                result_content = f.read()

            # Parse the score using the regex pattern
            score_match = score_pattern.search(result_content)
            if score_match:
                score = int(score_match.group(1))
            else:
                score = None  # Handle cases where the score isn't found

            # Store the score in the dictionary with the file name (without extension) as the key
            example_name = result_file.replace("_result.txt", "")
            scores_dict[example_name] = score

    # Save the parsed scores to a JSON file
    with open(output_json_file, "w") as json_file:
        json.dump(scores_dict, json_file, indent=4)

    print(f"Scores saved in '{output_json_file}'")
    return output_json_file, scores_dict

if __name__ == "__main__":
    # Example usage:
    scores = parse_discriminator_results()
    print(scores)