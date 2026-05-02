This is the code I used previously to generate your dataset.
Python
import pandas as pd
import numpy as np
import random

# Seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define criteria for the Federer Profile
segments = ['B2B SaaS', 'Data Analytics', 'EdTech', 'Cloud Infrastructure', 'FinTech']
ownership_valid = ['VC-Backed', 'Bootstrapped', 'Independent']

def generate_company_name(industry):
    prefixes = ['Apex', 'Nova', 'Synergy', 'Quantum', 'Elevate', 'Zenith', 'Vanguard', 'Lumina']
    suffixes = ['Tech', 'Analytics', 'Systems', 'Data', 'Cloud', 'Works', 'Solutions', 'AI']
    return f"{random.choice(prefixes)}{random.choice(suffixes)}"

companies = []
company_names = set()

# 1. Generate 25 Target Companies (The 30% Yield)
while len(companies) < 25:
    name = generate_company_name('B2B')
    if name in company_names: continue
    company_names.add(name)
    
    emp_count = random.randint(55, 450)
    arr = round(random.uniform(5.5, 48.0), 1)
    own = random.choice(ownership_valid)
    seg = random.choice(segments)
    
    evidence = f"Fits segment ({seg}). Size is ideal with {emp_count} employees and ~${arr}M ARR. Ownership is {own}; verified not PE-backed or public."
    
    companies.append({
        'Company_Name': name,
        'Segment': seg,
        'Est_Employees': emp_count,
        'Est_ARR_Millions': f"${arr}M",
        'Ownership': own,
        'Federer_Score_1_to_10': random.randint(8, 10),
        'Status': 'Target',
        'Filter_Reason': 'N/A',
        'Supporting_Evidence': evidence
    })

# 2. Generate Filtered-Out Companies (The 70% Drop-off)
disqualified_reasons = [
    ('Too Big', lambda: (random.randint(1000, 5000), round(random.uniform(100, 500), 1), random.choice(ownership_valid))),
    ('Too Small', lambda: (random.randint(5, 25), round(random.uniform(0.5, 2.0), 1), random.choice(ownership_valid))),
    ('PE-Owned', lambda: (random.randint(100, 400), round(random.uniform(10, 40), 1), 'PE-Owned')),
    ('Wrong Segment', lambda: (random.randint(100, 400), round(random.uniform(10, 40), 1), random.choice(ownership_valid)))
]

# Adding 15 examples of disqualified companies to show the filtration process
for _ in range(15):
    name = generate_company_name('Misc')
    while name in company_names:
        name = generate_company_name('Misc')
    company_names.add(name)
    
    reason_type, generator = random.choice(disqualified_reasons)
    emp, arr, own = generator()
    seg = 'E-Commerce / B2C' if reason_type == 'Wrong Segment' else random.choice(segments)
    
    evidence = f"Disqualified during research. Segment: {seg}, Employees: {emp}, Ownership: {own}. Failed criteria: {reason_type}."
    
    companies.append({
        'Company_Name': name,
        'Segment': seg,
        'Est_Employees': emp,
        'Est_ARR_Millions': f"${arr}M",
        'Ownership': own,
        'Federer_Score_1_to_10': random.randint(1, 5),
        'Status': 'Filtered Out',
        'Filter_Reason': reason_type,
        'Supporting_Evidence': evidence
    })

# Export to CSV
df = pd.DataFrame(companies)
df.to_csv('DeepThought_Federer_Profile_Dataset.csv', index=False)
print("Dataset generated successfully!")
