import json
from scipy.stats import spearmanr

def calculate_spearman_correlation(generated_scores_file, ground_truth_order):
    """
    Calculates Spearman's Rank Correlation Coefficient between the generated scores and the ground truth order.
    
    Args:
        generated_scores_file (str): Path to the JSON file containing the generated scores.
        ground_truth_order (list): A list representing the correct order of the examples based on the ground truth.
        
    Returns:
        float: Spearman's Rank Correlation Coefficient.
    """
    # Load the generated scores from the JSON file
    with open(generated_scores_file, "r") as json_file:
        generated_scores = json.load(json_file)

    print("Ground truth order:", ground_truth_order)

    # Sort the generated scores in ascending order (smallest score first)
    generated_order = sorted(generated_scores, key=generated_scores.get)
    print("Generated order:", generated_order)

    # Convert both orders to ranks
    ground_truth_ranks = [ground_truth_order.index(example) + 1 for example in ground_truth_order]
    generated_ranks = [ground_truth_order.index(example) + 1 for example in generated_order]
    print("Ground truth ranks:", ground_truth_ranks)
    print("Generated ranks:", generated_ranks)

    # Calculate Spearman's Rank Correlation Coefficient
    correlation, _ = spearmanr(ground_truth_ranks, generated_ranks)

    # Print the result
    print(f"Spearman's Rank Correlation Coefficient: {correlation:.4f}")

    if correlation == 1.0:
        print("The generated order perfectly matches the ground truth.")
    elif correlation > 0.8:
        print("The generated order is very similar to the ground truth.")
    elif correlation > 0.5:
        print("The generated order somewhat matches the ground truth.")
    else:
        print("The generated order is quite different from the ground truth.")

    return correlation

if __name__ == "__main__":
    # Example usage:
    ground_truth_order = ["plan_5", "plan_9", "plan_40", "plan_14", "plan_42", 
                          "plan_28", "plan_1", "plan_23", "plan_34", "plan_19"]

    correlation = calculate_spearman_correlation("processed_scores.json", ground_truth_order)
