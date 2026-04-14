#!/usr/bin/env python3

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Just remove "healthcare and research minded " from the text
old = "I'm a healthcare and research minded data analyst"
new = "I'm a data analyst"

if old in content:
    print(f"Found: {old}")
    content = content.replace(old, new)
    print(f"Replaced with: {new}")
else:
    print(f"Not found: {old}")
    print("Trying just the beginning...")
    
    if "I'm a healthcare" in content:
        print('Found "I am a healthcare"')
        content = content.replace("I'm a healthcare and research minded ", "I'm a ")
        print("Replacement done")

# Also fix "multi source" to "multi-source"
if "multi source" in content:
    print('Found "multi source"')
    content = content.replace("multi source", "multi-source")
    print('Replaced with "multi-source"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File updated")
