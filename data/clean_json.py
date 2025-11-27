import json
import re
import os

INPUT_FILE = "data/raw_posts.json"
OUTPUT_FILE = "data/raw_posts_clean.json"

def clean_text(s):
    # Remove invalid surrogate unicode (broken emojis)
    return re.sub(r'[\ud800-\udfff]', '', s)

def cleanse(obj):
    if isinstance(obj, dict):
        return {k: cleanse(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [cleanse(i) for i in obj]
    elif isinstance(obj, str):
        return clean_text(obj)
    else:
        return obj

print("Loading JSON:", INPUT_FILE)
data = json.load(open(INPUT_FILE, encoding="utf-8", errors="ignore"))

print("Cleaning text...")
cleaned = cleanse(data)

print("Saving cleaned JSON:", OUTPUT_FILE)
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(cleaned, f, ensure_ascii=False, indent=2)

print("Done! Cleaned file created successfully.")
