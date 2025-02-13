import os
import json
from datetime import datetime

# Directory containing blog posts
BLOG_DIR = "blog-posts"
OUTPUT_FILE = "blog-list.json"

# Scan blog directory for HTML files
blog_posts = []
for filename in os.listdir(BLOG_DIR):
    if filename.endswith(".html"):
        # Extract date and title from filename
        parts = filename[:-5].split("_", 1)
        if len(parts) == 2:
            date_str, title = parts
            try:
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                blog_posts.append({
                    "filename": filename,
                    "date": date_obj.strftime("%Y-%m-%d"),
                    "title": title.replace("-", " ")
                })
            except ValueError:
                print(f"Skipping {filename}: Invalid date format")

# Sort posts by date (newest first)
blog_posts.sort(key=lambda x: x["date"], reverse=True)

# Write to JSON file
with open(OUTPUT_FILE, "w") as f:
    json.dump(blog_posts, f, indent=2)

print(f"Generated {OUTPUT_FILE} with {len(blog_posts)} posts.")
