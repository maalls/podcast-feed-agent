from podcastfy.client import generate_podcast
# import json from feeds.json
import json
# load model name from .env file
import os
from dotenv import load_dotenv
load_dotenv()
# load environment variables
MODEL = os.getenv('MODEL', 'gpt-4')
print(f"Using model: {MODEL}")
# check if feeds.json exists and load it
feeds = []
try:
    with open('feeds.json', 'r') as f:
        feeds = json.load(f)
except FileNotFoundError:
    print("feeds.json not found. Please create it with a list of podcast URLs.")
    exit(1)
except json.JSONDecodeError:
    print("feeds.json is not a valid JSON file. Please check its contents.")
    exit(1)

# making sure feeds is a list of urls
if not isinstance(feeds, list):
    print("feeds.json should be a list of URLs.")
    exit(1)


custom_config = {
    "output_language": 'French'
}

audio_file = generate_podcast(urls=feeds,
    llm_model_name=MODEL,
    api_key_label="API_KEY",
    conversation_config=custom_config,)
