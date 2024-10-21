import json
import sys

input_json = sys.stdin.read()
commits = json.loads(input_json)

lines = []
for commit in commits:
    author_username = commit['author']['username']
    message = commit['message'].split('\n')[0]
    block = f"🥷 {author_username}\n💬 {message}"
    lines.append(block)

print("\n\n".join(lines))
