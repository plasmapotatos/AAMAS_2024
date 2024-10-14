import os
import subprocess

def run_tests(plans, num_trials):
    for plan_number in plans:
        os.environ['EXAMPLE_PLAN_NUMBER'] = str(plan_number)
        for trial_number in range(1, num_trials + 1):
            os.environ['TRIAL_NUMBER'] = str(trial_number)
            print(f"Running plan {plan_number}, trial {trial_number}...")
            subprocess.run(['scripts/test_prompt_with_plan.sh'], check=True)
            print(f"Completed plan {plan_number}, trial {trial_number}.")

if __name__ == "__main__":
    plans = [36]  # Replace with the actual list of plans you want to test
    num_trials = 3  # Replace with the actual number of trials you want to run for each plan
    run_tests(plans, num_trials)
