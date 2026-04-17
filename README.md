# Food Delivery Analysis

A production-style data analyst project that combines Python data preparation with Tableau dashboard storytelling.

## Why This Project

This repository demonstrates an end-to-end analytics workflow:
- clean and transform raw order-history data
- build KPI-ready aggregate tables for BI
- design worksheet-level and executive dashboard-level insights in Tableau

The result is a portfolio-ready project suitable for analyst interviews and hiring assessments.

## Project Highlights

- 21K+ food-delivery orders analyzed
- modular Python pipeline organized by responsibility
- 12 Tableau worksheets
- 4 Tableau dashboards
- reusable processed datasets for Power BI or Tableau

## Repository Structure

- [data/raw](data/raw): raw dataset
- [data/processed](data/processed): cleaned and aggregated outputs used in BI
- [src/food_delivery_analysis](src/food_delivery_analysis): modular Python package
- [scripts](scripts): runnable entry script for data build
- [tableau/workbook](tableau/workbook): Tableau workbook file
- [output/tableau/worksheets](output/tableau/worksheets): worksheet snapshots
- [output/tableau/dashboards](output/tableau/dashboards): dashboard snapshots
- [notebooks](notebooks): exploratory and analysis notebook
- [docs](docs): compact project documentation

## Tech Stack

- Python (Pandas)
- Tableau Public / Tableau Desktop

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Build processed datasets

```bash
python scripts/build_tableau_data.py
```

Generated files:
- [data/processed/tableau_main_data_clean.csv](data/processed/tableau_main_data_clean.csv)
- [data/processed/tableau_executive_summary_clean.csv](data/processed/tableau_executive_summary_clean.csv)
- [data/processed/tableau_restaurant_performance_clean.csv](data/processed/tableau_restaurant_performance_clean.csv)
- [data/processed/tableau_customer_experience_clean.csv](data/processed/tableau_customer_experience_clean.csv)
- [data/processed/tableau_geographic_intelligence_clean.csv](data/processed/tableau_geographic_intelligence_clean.csv)

## Tableau Assets

Workbook:
- [tableau/workbook/food.twb](tableau/workbook/food.twb)

Export guide:
- [output/tableau/EXPORT_GUIDE.md](output/tableau/EXPORT_GUIDE.md)

## Dashboard Snapshots

### Dashboard 1: Executive Overview
![Executive Overview](output/tableau/dashboards/dashboard_1_executive_overview.png)

### Dashboard 2: Restaurant and Revenue Performance
![Restaurant and Revenue Performance](output/tableau/dashboards/dashboard_2_restaurant_revenue_performance.png)

### Dashboard 3: Customer Experience and Operations
![Customer Experience and Operations](output/tableau/dashboards/dashboard_3_customer_experience_operations.png)

### Dashboard 4: Interview Storyboard
![Interview Storyboard](output/tableau/dashboards/dashboard_4_interview_storyboard.png)

## Worksheet Snapshots

### 01 KPI Cards
![KPI Cards](output/tableau/worksheets/01_kpi_cards.png)

### 02 Revenue Trend
![Revenue Trend](output/tableau/worksheets/02_revenue_trend.png)

### 03 Order Funnel
![Order Funnel](output/tableau/worksheets/03_order_funnel.png)

### 04 City Heatmap
![City Heatmap](output/tableau/worksheets/04_city_heatmap.png)

### 05 Top Restaurants
![Top Restaurants](output/tableau/worksheets/05_top_restaurants.png)

### 06 Meal Period Performance Complaint Rate vs AOV
![Meal Period Performance](output/tableau/worksheets/06_meal_period_performance_complaint_rate_vs_aov.png)

### 07 Distance Impact
![Distance Impact](output/tableau/worksheets/07_distance_impact.png)

### 08 Top Revenue Generating Subzones
![Top Revenue Generating Subzones](output/tableau/worksheets/08_top_revenue_generating_subzones.png)

### 09 Top Complaint Drivers Distribution
![Top Complaint Drivers](output/tableau/worksheets/09_top_complaint_drivers_distribution.png)

### 10 Distance vs Delivery Performance
![Distance vs Delivery Performance](output/tableau/worksheets/10_distance_vs_delivery_performance.png)

### 11 Rating Distribution
![Rating Distribution](output/tableau/worksheets/11_rating_distribution.png)

### 12 Restaurant Performance Summary
![Restaurant Performance Summary](output/tableau/worksheets/12_restaurant_performance_summary.png)

## Dashboard Mapping

- [docs/dashboard_structure.md](docs/dashboard_structure.md)

## Notes

This repository intentionally keeps only project-relevant assets and avoids redundant intermediate files so that both technical and non-technical viewers can navigate it quickly.
