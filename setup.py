import os
import json

def get_api_keys():
    openai_api_key = input("Enter your OpenAI API key: ")
    other_api_key = input("Enter your other API key (if any, else leave blank): ")

    keys = {
        "openai_api_key": openai_api_key,
        "other_api_key": other_api_key
    }

    # Create config directory if it doesn't exist
    os.makedirs("config", exist_ok=True)
    
    # Save API keys to config file
    with open("config/api_keys.json", "w") as f:
        json.dump(keys, f)

    print("API keys saved successfully.")

if __name__ == "__main__":
    get_api_keys()
