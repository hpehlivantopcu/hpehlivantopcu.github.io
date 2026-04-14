#!/usr/bin/env python3

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('Initial check:')
if 'healthcare and research minded' in content:
    print('  - Old text found')
else:
    print('  - Old text NOT found')

if 'transforms messy' in content:
    print('  - New text found')
else:
    print('  - New text NOT found')

# Do the replacement
old_phrase = "I'm a healthcare and research minded data analyst who turns messy, multi source data into"
new_phrase = "I'm a data analyst who transforms messy, multi-source data into"

print(f'\nReplacing:')
print(f'  OLD: {old_phrase}')
print(f'  NEW: {new_phrase}')

content = content.replace(old_phrase, new_phrase)

print('\nAfter replacement:')
if 'transforms messy' in content:
    print('  - New text NOW found!')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('  - File WRITTEN')
else:
    print('  - New text STILL not found')
    # Debug: show what we're looking for
    idx = content.find('healthcare and research minded')
    if idx >= 0:
        print(f'  - Found healthcare text at position {idx}')
        print(f'  - Context: ...{content[max(0,idx-50):idx+100]}...')
