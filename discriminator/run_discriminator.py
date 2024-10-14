import os
from agents.prompts import DISCRIMINATOR_PROMPT
from utils.request_utils import prompt_gpt4
from tqdm import tqdm

def run_discriminator(examples_folder="evaluation/examples", results_folder="discriminator_results"):
    """
    Runs the discriminator on examples from the specified folder and yields results for each example.
    
    Args:
        examples_folder (str): Path to the folder containing example files.
        results_folder (str): Path to the folder where results will be saved.

    Yields:
        tuple: A tuple containing the example file name and the result of the discriminator.
    """
    # Load the eval_script from "evaluation/commonsense_constraint.py"
    print("Loading evaluation script...")
    with open("evaluation/commonsense_constraint.py", "r") as f:
        eval_script = f.read()

    # Create the results folder if it doesn't exist
    if not os.path.exists(results_folder):
        os.mkdir(results_folder)

    # Loop through all the .txt files in the examples folder
    for example_file in tqdm(sorted(os.listdir(examples_folder))):
        if example_file.endswith(".txt"):
            # Load the example content
            example_path = os.path.join(examples_folder, example_file)
            with open(example_path, "r") as f:
                example = f.read()

            # Format the DISCRIMINATOR_PROMPT with the eval_script and example
            prompt = DISCRIMINATOR_PROMPT.format(eval_script=eval_script, example=example)
            #print(prompt)
            # Get the result by prompting GPT-4
            result = prompt_gpt4(prompt)
            print(result)

            # Save the result to a file in the results folder
            result_filename = f"{example_file.replace('.txt', '')}_result.txt"
            result_filename = f"{example_file.replace('.txt', '')}_result.txt"
            result_path = os.path.join(results_folder, result_filename)
            with open(result_path, "w") as result_file:
                result_file.write(result)

            # Yield the result as it's generated
            #yield example_file, result

if __name__ == "__main__":
    # Example usage of the function:
    for example_file, result in run_discriminator():
        print(f"Processed: {example_file}")
        print(f"Result: {result}")