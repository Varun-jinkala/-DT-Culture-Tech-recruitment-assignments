# -DT-Culture-Tech-recruitment-assignments
DeepThought Business Analytics: Target Company Research This repository contains my submission for the DeepThought Business Analytics Assignment. The core objective is to simulate a Business Analyst's real-world research by identifying 25 mid-market companies that match the strict "Federer Profile," while rigorously filtering out unqualified leads
DeepThought Business Analytics: Target Company Research
Welcome to my repository for the DeepThought Business Analytics assignment. This project simulates the real-world responsibilities of a Business Analyst tasked with identifying high-potential, mid-market companies that fit a highly specific, high-intent profile—often referred to internally as the "Federer Profile."

This repository contains the resulting dataset, the methodology used to curate it, the analytical insights derived from the research, and a Python script demonstrating how the final data output is structured.

🎯 Objective: The "Federer Profile"
The core mandate was to research and compile a highly curated list of 25 target companies. To qualify, a company had to meet strict criteria. If a company failed even one of these parameters, it was immediately disqualified.

Positive Criteria (Must Have):

Industry Segment: Strictly B2B SaaS, Data Analytics, EdTech, FinTech, or Cloud Infrastructure.

Company Size: 50 to 500 Employees.

Revenue Estimates: $5 Million to $50 Million Annual Recurring Revenue (ARR).

Ownership Structure: Independent, Bootstrapped, or VC-Backed (Seed to Series C).

Negative Criteria (Must NOT Have):

Wrong Segment: No B2C, D2C, purely service-based, hardware, or E-commerce companies.

Outside Size Bounds: No micro-startups (<50 employees) or large enterprises (>500 employees).

Disqualified Ownership: Strictly no Private Equity (PE) backed, publicly traded, or already acquired companies.

🧠 Sourcing Strategy & Methodology
The ~30% Yield Reality
In professional prospecting, identifying the ideal target is as much about exclusion as it is about inclusion. The assignment correctly noted an expected ~30% yield. This means that to find 25 perfectly matched companies, I had to actively research and disqualify roughly 60 to 75 companies that initially looked promising but failed upon deeper inspection.

The Research Funnel
Top of Funnel (Broad Discovery): Utilized standard business databases (like Crunchbase and Apollo) filtering for the primary keywords (B2B SaaS, Cloud) and the established employee headcount range (50-500).

Middle of Funnel (Negative Filtration): This is where the highest drop-off occurred. I aggressively scrubbed the list against the negative criteria, dropping companies that were heavily service-based or clearly targeting consumers.

Bottom of Funnel (Deep Verification): For the surviving candidates, I cross-referenced their official websites, LinkedIn presence, and PR announcements to verify their funding status. The goal was to ensure no hidden Private Equity backing existed.

Scoring: Each final candidate was given a "Federer Score" (1-10) based on how perfectly they aligned with the ideal $5M-$50M ARR mid-market sweet spot.

📊 Analytical Insights Discovered
During the manual research phase, several key patterns emerged regarding the mid-market SaaS landscape:

The "PE-Backed Trap": The most common point of failure for companies in the $15M-$40M ARR range is ownership. Many companies that present themselves as "independent" SaaS leaders have actually been quietly acquired by majority-stake Private Equity firms. Thoroughly checking the "News" or "Press" sections of a company's website is mandatory to catch this.

The "Mid-Market Mirage" (Headcount vs. Revenue): Employee count is often a flawed proxy for revenue. Highly efficient Cloud Infrastructure companies might generate $20M ARR with only 45 employees (technically failing the size filter), while EdTech companies with 400 employees might only generate $4M ARR because they are highly service-heavy.

Segment Bias: Pure-play B2B SaaS and Data Analytics yielded the highest concentration of valid targets.

🚀 Part B: Scale-Up Proposal (From 25 to 2,500)
Manually verifying the "Federer Profile" is incredibly time-consuming, primarily due to the 70% disqualification rate. To scale this operation for enterprise-level lead generation, the process must transition from manual database queries to an automated data pipeline.

Proposed Automated Architecture:

API Integration: Connect directly to the Apollo.io or Crunchbase Enterprise API to pull a daily, raw feed of thousands of companies strictly bound by the 50-500 employee and $5M-$50M ARR parameters.

Programmatic Disqualification: Run an initial Python script to immediately drop any companies tagged with "Public" or known Private Equity firm names in their funding history.

LLM-Powered Semantic Scraping: Standard database industry tags are often inaccurate. Deploy a web scraper to pull the text from the target's "About Us" and "Pricing" pages. Feed this text into an LLM (like Google's Gemini) with a strict prompt to classify the company: "Is this product sold to businesses (B2B) or consumers (B2C)?" This eliminates manual website reviews.

Human-in-the-Loop QA: The automated system filters the 10,000 raw leads down to the 3,000 that pass all checks. A lean team of Business Analysts then performs the final qualitative verification on the curated list.

🗂️ Repository Structure
DeepThought_Federer_Profile_Dataset.csv: The finalized dataset containing the 25 qualified targets, plus a sample of 15 disqualified companies (documenting the exact reason for their failure, such as "Too Big" or "PE-Owned") to showcase the ~30% yield methodology.

dataset_generator.py: The Python script utilized to structure, score, filter, and export the research data into the final CSV format, demonstrating a systematic approach to data handling.
