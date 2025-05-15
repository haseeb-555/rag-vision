import cohere
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the API key from .env
api_key = os.getenv("COHERE_API_KEY")

# Initialize Cohere client
co = cohere.Client(api_key)

# Text to embed
texts = [
    "Write a short poem about stars and the night sky.",
    "The quick brown fox jumps over the lazy dog."
]

# Generate embeddings using embed-v4.0 model
response = co.embed(
    model='embed-v4.0',
    texts=texts
)

# Print the embeddings
for i, embedding in enumerate(response.embeddings):
    print(f"Embedding for text {i+1} (length {len(embedding)}):")
    print(embedding[:10], "...")  # print first 10 values for brevity
