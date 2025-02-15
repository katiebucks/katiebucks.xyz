import os import re import json from datetime import datetime

Directory containing blog posts

BLOG_DIR = "blogs" OUTPUT_INDEX = "blog-index.html" OUTPUT_JSON = "blog-list.json" MAX_POSTS = 20  # Number of recent posts to display

Function to extract title, date, and snippet from a blog post

def extract_blog_metadata(filepath): with open(filepath, "r", encoding="utf-8") as file: content = file.read()

# Extract title from the first <h1> tag
title_match = re.search(r"<h1>(.*?)</h1>", content)
title = title_match.group(1) if title_match else "Untitled"

# Extract date from filename (assumes YYYY-MM-DD format)
filename = os.path.basename(filepath)
date_match = re.match(r"(\d{4}-\d{2}-\d{2})_", filename)
date = date_match.group(1) if date_match else "Unknown Date"

# Extract snippet (first paragraph or first 200 chars)
snippet_match = re.search(r"<p>(.*?)</p>", content, re.DOTALL)
snippet = snippet_match.group(1)[:200] if snippet_match else content[:200]

return {
    "filename": filename,
    "date": date,
    "title": title,
    "snippet": snippet
}

Collect all blog posts

blog_posts = [] for filename in os.listdir(BLOG_DIR): if filename.endswith(".html"): filepath = os.path.join(BLOG_DIR, filename) metadata = extract_blog_metadata(filepath) blog_posts.append(metadata)

Sort posts by date (newest first)

blog_posts.sort(key=lambda x: x["date"], reverse=True) recent_posts = blog_posts[:MAX_POSTS]

Generate blog list JSON

with open(OUTPUT_JSON, "w", encoding="utf-8") as json_file: json.dump(recent_posts, json_file, indent=2)

Generate blog index HTML

html_content = """<!DOCTYPE html>

<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <link rel='stylesheet' href='styles.css'>
    <title>Blog Index</title>
</head>
<body>
    <header>
        <h1>Latest Blog Posts</h1>
    </header>
    <main>
"""for post in recent_posts: html_content += f""" <section class='blog-preview'> <h2><a href='{BLOG_DIR}/{post['filename']}'>{post['title']}</a></h2> <p><em>{post['date']}</em></p> <p>{post['snippet']}...</p> </section> """

html_content += """ </main>

</body>
</html>
"""Save the generated index file

with open(OUTPUT_INDEX, "w", encoding="utf-8") as index_file: index_file.write(html_content)

print(f"Generated {OUTPUT_INDEX} and {OUTPUT_JSON} with {len(recent_posts)} posts.")

