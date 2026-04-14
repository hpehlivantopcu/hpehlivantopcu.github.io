#!/usr/bin/env python3

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the about section  
about_start = content.find('<section id="about">')
about_end = content.find('</section>', about_start)
about_section = content[about_start:about_end]

print('About section length:', len(about_section))
print()

# Look for the healthcare phrase within the about section
if 'healthcare' in about_section:
    print('Found healthcare in about section')
    idx = about_section.find('healthcare')
    snippet = about_section[max(0, idx-50):idx+150]
    print('Raw bytes:', repr(snippet))
else:
    print('healthcare NOT in about section')

# Let me look at what's in the about section more carefully
lines = about_section.split('\n')
for i, line in enumerate(lines):
    if 'data analyst' in line.lower():
        print(f'Line {i}: {repr(line[:100])}...')
