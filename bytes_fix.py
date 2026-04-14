#!/usr/bin/env python3

with open('index.html', 'rb') as f:
    content = f.read()

# The exact bytes: I + UTF-8 right quote (e2 80 99) + m  
old_bytes = b'I\xe2\x80\x99m a healthcare and research minded data analyst'
new_bytes = b'I\xe2\x80\x99m a data analyst'

if old_bytes in content:
    print('Found the phrase with Unicode apostrophe')
    content = content.replace(old_bytes, new_bytes)
    print('Replaced!')
else:
    print('Phrase not found - checking what we have...')
    
# Also fix 'who turns' to 'who transforms'
if b'who turns messy' in content:
    print('Found "who turns messy"')
    content = content.replace(b'who turns messy', b'who transforms messy')
    print('Replaced with "who transforms messy"')

with open('index.html', 'wb') as f:
    f.write(content)

print('File saved')

# Verify in UTF-8
with open('index.html', 'r', encoding='utf-8') as f:
    content_text = f.read()
    if 'healthcare and research minded' in content_text:
        print('WARNING: Still contains healthcare reference')
    else:
        print('SUCCESS: Removed healthcare reference!')
