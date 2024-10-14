import tiktoken
import base64

# Load an image and convert it to a base64 string
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        base64_string = base64.b64encode(image_file.read()).decode('utf-8')
    return base64_string

# Function to count tokens using tiktoken
def count_tokens(text):
    # Initialize the encoder for GPT-4 (replace with the model you're using)
    encoding = tiktoken.encoding_for_model("gpt-4")
    tokens = encoding.encode(text)
    return len(tokens)

# Example usage
if __name__ == "__main__":
    # Replace with your image path
    image_path = "Screenshot_2024-07-18_at_3.png"
    
    # Convert the image to a base64 string
    base64_string = image_to_base64(image_path)
    print(f"Base64 string length: {len(base64_string)}")
    
    # Count the number of tokens
    num_tokens = count_tokens(base64_string)
    
    print(f"Number of tokens: {num_tokens}")
