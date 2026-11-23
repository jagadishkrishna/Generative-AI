from abc import ABC, abstractmethod
from google import genai
import requests

# Common interface
class LLMProvider(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass

# Gemini cloud provider
class GeminiProvider(LLMProvider):

    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt):
        response = self.client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )
        return response.text

# Ollama local provider
import ollama
class OllamaProvider(LLMProvider):

    def __init__(self, model="mistral:7b"):
        self.model = model

    def generate(self, prompt):
        response = ollama.chat(
            model=self.model, 
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']

# Common client
class LLMClient:

    def __init__(self, provider):
        self.provider = provider

    def generate(self, prompt):
        return self.provider.generate(prompt)
