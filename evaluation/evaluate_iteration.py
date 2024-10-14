import json

# Parse the JSON data
with open('evaluation/iteration3/data_record_train.json', 'r') as file:
    data = json.load(file)

# Function to calculate summary statistics
def calculate_summary_statistics(data):
    results = []
    for item in data:
        commonsense_constraints = item['commonsense_constraint']
        hard_constraints = item['hard_constraint']
        if not commonsense_constraints: commonsense_constraints = {}
        if not hard_constraints: hard_constraints = {}
        
        # Count true values in commonsense constraints
        true_commonsense = sum(1 for value in commonsense_constraints.values() if value[0] is True)
        total_commonsense = 8
        
        # Count true values in hard constraints
        true_hard = sum(1 for value in hard_constraints.values() if value[0] is True)
        total_hard = 5
        
        # Calculate the summary statistic
        summary_statistic = (true_commonsense + true_hard) / (total_commonsense + total_hard)
        results.append(summary_statistic)
    
    return results

# Calculate the summary statistics
summary_statistics = calculate_summary_statistics(data)

# Sort the summary statistics along with their indices
sorted_stats_with_indices = sorted((stat, idx) for idx, stat in enumerate(summary_statistics))

# Print the sorted statistics
for rank, (stat, idx) in enumerate(sorted_stats_with_indices, start=1):
    print(f"{rank}th minimum value: {stat} at index {idx}")

# Optionally, you can print up to the nth minimum values like this:
n = 3  # Change this value to get more minimum values
for rank, (stat, idx) in enumerate(sorted_stats_with_indices[:n], start=1):
    print(f"{rank}th minimum value: {stat} at index {idx}")
