import tiktoken


def count_tokens(input_string, model_name):
    # Load the tokenizer for the specified model
    tokenizer = tiktoken.encoding_for_model(model_name)

    # Encode the input string to get the tokens
    tokens = tokenizer.encode(input_string)

    # Return the number of tokens
    return len(tokens)


# Example usage
input_string = "Your input text goes here."

# Count tokens for GPT-4
num_tokens_gpt4 = count_tokens(input_string, "gpt-4")
print(f"Number of tokens for GPT-4: {num_tokens_gpt4}")
