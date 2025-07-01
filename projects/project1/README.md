# Aviation Fleet Risk Analysis

**By:** Stephen Bwanamkubwa, Moringa Data Scientist

## Overview  
Our company is expanding into the aviation market and needs data-driven guidance on safety risk. We analyzed 60+ years of NTSB accident data (1962–2023) using pandas and Matplotlib to identify the lowest-risk aircraft models, operational factors, and geographic hotspots.

## Business Problem  
- **Goal:** Select the safest aircraft for initial fleet acquisition.  
- **Stakeholder:** Head of the New Aviation Division—making high-stakes procurement decisions.

## Data & Methods  
- **Source:** NTSB accident records + U.S. state codes  
- **Cleaning:** Handled missing values, parsed dates, merged lookups  
- **Analysis:**  
  1. Accident frequency and severity by model  
  2. Temporal trends and phase breakdown  
  3. Weather and geographic risk factors  
- **Visuals:** Bar charts, line graphs, and stacked bars in Matplotlib.

## Key Findings  
1. **Lowest-Risk Models:** Ten aircraft (e.g., 10 GXE, 1-131E) with only one recorded accident over six decades.  
2. **Operational Risk:** > 60% of incidents occur during ground operations; ~80% of in-air accidents happen under clear skies.  
3. **Safe Regions:** States like Vermont and Wyoming report fewer than 15 accidents since 1962.

## Recommendations  
1. Acquire proven low-risk models (e.g., 10 GXE, 1-131E).  
2. Base initial fleet in low-incident states (VT, WY).  
3. Enhance ground-operation training (taxi/takeoff/landing protocols).

## Repository Structure  
├─ data/

│ ├─ AviationData.csv

│ └─ USState_Codes.csv

|─Interactive_Dashboard

├─final_analysis.ipynb

├─ visuals/

│ ├─ lowest_risk_models.png

│ └─ … other chart images …

├─presentation.pdf

├─ .gitignore

└─ README.md

## How to Reproduce  
1. Clone the repo and install dependencies:  
   ```bash
   git clone <repo-url>
   cd <repo>
   pip install -r requirements.txt

2. Run the Jupyter notebook 
jupyter lab final_analysis.ipynb

3. View the non-technical presentation:presentation/presentation.pdf

4. Explore the live dashboard: https://public.tableau.com/views/My_Interactive_Dashboard/InteractiveDashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

