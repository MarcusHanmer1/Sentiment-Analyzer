import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("news_api_key")

if not api_key:
    print("Error: API key not found")
else:
    print("API key loaded successfully")
    
    query = "Tesla"
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        
        if data["status"] == "ok":
            print("API test successful!")
            print(f"Total articles found for '{query}': {data['totalResults']}")
            
            if data['totalResults'] > 0:
                print(f"Title of first article: {data['articles'][0]['title']}")
            else:
                print("No articles found")
                
        else:
            print(f"API Error: {data['message']}")

    except Exception as e:
        print(f"A script error occurred: {e}")