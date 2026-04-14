#!/usr/bin/env python3

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('Starting updates...')

# List of replacements to make
replacements = [
    # Fix the opening phrase
    ("I'm a healthcare and research minded data analyst who turns messy, multi source data into <span class=\"highlight\">clean, trustworthy",
     "I'm a data analyst who transforms messy, multi-source data into <span class=\"highlight\">clean, trustworthy dashboards and"),
    
    # Fix the remaining part (if not caught by above)
    ("through validation, documentation, and strong follow through.",
     "I specialize in building semantic data models, defining KPIs, and delivering insights that stakeholders can act on."),
    
    # Update second main paragraph - the part about stakeholders
    ("combining <span class=\"highlight\">SQL, Python, Excel, and Power BI</span> to answer business questions and surface actionable trends.",
     "use <span class=\"highlight\">SQL, Python, Excel, and Power BI</span>. My strength is translating business questions into structured analyses and communicating findings clearly to both technical and non-technical stakeholders."),
    
    # Fix the academic foundation paragraph
    ("which helps me work comfortably in regulated or high accuracy environments.",
     "giving me experience with data quality standards, statistical rigor, and working effectively in high-accuracy environments."),
]

for old, new in replacements:
    if old in content:
        print(f'  ✓ Found and replacing: {old[:60]}...')
        content = content.replace(old, new)
    else:
        print(f'  ✗ NOT found: {old[:60]}...')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\nAll replacements complete. File saved.')

# Verify
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
    
print('\nFinal verification:')
if 'transforms messy' in content:
    print('  ✓ Contains "transforms messy" - GOOD!')
if 'healthcare and research minded' in content:
    print('  ✗ Still contains "healthcare and research minded" - NEEDS FIX')
if 'semantic data models' in content:
    print('  ✓ Contains "semantic data models" - GOOD!')
