#!/usr/bin/env python3

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the index
idx = content.find('healthcare and research minded')
if idx >= 0:
    # Get the surrounding text
    start = max(0, idx - 50)
    end = min(len(content), idx + 100)
    snippet = content[start:end]
    
    print('Found at position:', idx)
    print('Snippet:')
    print(repr(snippet))  # repr shows all special characters
    print()
    print('Checking for exact phrase:')
    test_phrase = "I'm a healthcare and research minded data analyst who turns messy, multi source data into"
    if test_phrase in content:
        print('✓ Exact phrase found')
    else:
        print('✗ Exact phrase NOT found')
        # Try to find what's actually there
        idx2 = content.find("healthcare")
        if idx2 >= 0:
            print('But found "healthcare" at:', idx2)
            snippet2 = content[idx2-30:idx2+150]
            print(repr(snippet2))
