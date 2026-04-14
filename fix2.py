#!/usr/bin/env python3

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The exact phrase from the about section to replace
old_phrase = "I'm a healthcare and research minded data analyst who turns messy, multi source data into"
new_phrase = "I'm a data analyst who transforms messy, multi-source data into"

print('Attempting replacement...')
print(f'Old phrase: {repr(old_phrase[:60])}...')
print(f'New phrase: {repr(new_phrase[:60])}...')

if old_phrase in content:
    print('✓ Found old phrase')
    content = content.replace(old_phrase, new_phrase)
    print('✓ Replacement done')
else:
    print('✗ Old phrase not found')
    print('Trying character-by-character inspection...')
    # Find healthcare in about section
    about_start = content.find('<section id="about">')
    about_end = content.find('</section>', about_start)
    about_section = content[about_start:about_end]
    
    idx = about_section.find("I'm a")
    if idx >= 0:
        snippet = about_section[idx:idx+100]
        print(f'Found at pos {idx}: {repr(snippet)}')
        # Check byte by byte 
        for i, char in enumerate(snippet[:20]):
            print(f'  chr {i}: {repr(char)} (U+{ord(char):04X})')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('File saved')
