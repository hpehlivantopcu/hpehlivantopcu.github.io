#!/usr/bin/env python3

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find and replace the specific line with healthcare mention
for i, line in enumerate(lines):
    if 'healthcare and research minded' in line:
        print(f'Found healthcare line at {i}: {line[:80]}...')
        # Replace the healthcare phrase
        new_line = line.replace(
            "I'm a healthcare and research minded data analyst who turns messy, multi source data into",
            "I'm a data analyst who transforms messy, multi-source data into"
        )
        lines[i] = new_line
        print(f'Updated to: {new_line[:80]}...')
        break

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Done!')
