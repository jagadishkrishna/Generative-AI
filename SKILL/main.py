
import os
from dotenv import load_dotenv # type: ignore
from google import genai # type: ignore

# Step 1: Load environment variables
load_dotenv()

# Step 2: Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

# Step 3: Create Gemini client
client = genai.Client(api_key=api_key)

# Step 4: Send prompt to Gemini
response = client.models.generate_content(
  model="gemini-3.5-flash-lite",
    contents="What is Artificial Intelligence? Explain in simple words."
)

# Step 5: Display response
print("\nLLM Response:")
print(response.text)