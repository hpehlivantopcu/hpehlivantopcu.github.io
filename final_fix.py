#!/usr/bin/env python3

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The apostrophe in the file is a Unicode right single quotation mark (U+2019)
# Use the correct character in the regex
old_pattern = "I'm a healthcare and research minded data analyst"  # This uses the fancy apostrophe
new_pattern = "I'm a data analyst"  # Regular apostrophe

# Replace using the Unicode character
content = content.replace("I'm a healthcare and research minded data analyst", "I'm a data analyst")

# Also while we're at it, let's update "who turns messy" to "who transforms messy"
content = content.replace("who turns messy", "who transforms messy")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacements complete!")

# Verify
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
    if "healthcare and research minded" in content:
        print("ERROR: Still contains healthcare reference")
    else:
        print("SUCCESS: Healthcare reference removed!")
