#!/usr/bin/env python3

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
    
if 'transforms messy' in content:
    print('File HAS been updated successfully!')
elif 'healthcare and research minded' in content:
    print('File still has OLD text')
else:
    print('Cannot determine')
