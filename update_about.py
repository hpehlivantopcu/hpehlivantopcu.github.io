#!/usr/bin/env python3
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# First replacement: Update the main about paragraph
content = content.replace(
    "I'm a healthcare and research minded data analyst who turns messy, multi source data into",
    "I'm a data analyst who transforms messy, multi-source data into"
)

# Second replacement: Update the reports text 
content = content.replace(
    "clean, trustworthy reports</span> through validation, documentation, and strong follow through.",
    "clean, trustworthy dashboards and reports</span> that drive business decisions. I specialize in building semantic data models, defining KPIs, and delivering insights that stakeholders can act on."
)

# Third replacement: Update the third paragraph
content = content.replace(
    "I've supported stakeholders with dashboards and recurring reporting across nonprofit programs and telecom combining",
    "I've partnered with teams across nonprofit programs, telecom, and enterprise environments to design Power BI dashboards, develop classification models, and automate reporting workflows using"
)

# Fourth replacement: Update the actionable trends part
content = content.replace(
    "to answer business questions and surface actionable trends.",
    ". My strength is translating business questions into structured analyses and communicating findings clearly to both technical and non-technical stakeholders."
)

# Fifth replacement: Update the last paragraph
content = content.replace(
    "which helps me work comfortably in regulated or high accuracy environments.",
    "giving me experience with data quality standards, statistical rigor, and working effectively in high-accuracy environments."
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('About section updated successfully')

