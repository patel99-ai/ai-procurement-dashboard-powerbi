# Enterprise Procurement Intelligence Platform

**An AI-powered spend analytics and supplier risk dashboard built in Power BI.**

A six-page, end-to-end procurement analytics solution analyzing **$1.28B in spend** across **50 suppliers, 20 countries, and 11 procurement categories**. Built as a portfolio project to demonstrate data modeling, DAX, and Power BI's AI/ML capabilities applied to real procurement workflows.

**Tech stack:** Power BI Desktop · DAX · Python (synthetic data generation)

\---

## Project Overview

This dashboard takes a raw 5,000-row procurement dataset and turns it into an executive-ready decision tool. It answers the questions a procurement team actually asks: Where is our money going? Which suppliers are risky, and why? Who delivers reliably? What's our contract exposure? And what does the data predict next?

The project emphasizes **trustworthy numbers** (careful data modeling and de-duplication), **clear visual storytelling** (a consistent, clean design system across all pages), and **breadth of Power BI's AI features** (seven distinct AI/ML capabilities).

\---

## Dashboard Pages

1. **Executive Summary** — Headline KPIs ($1.28B spend, 50 suppliers, 5K invoices), spend by payment terms, an on-time-delivery gauge against an 85% target, supplier risk distribution, and a monthly spend trend.
2. **Spend Analytics** — Spend by department and country (bubble map), Top 10 suppliers (Top-N filtering), and an AI Decomposition Tree drilling into the highest-spend paths.
3. **Supplier Risk** — A risk-vs-spend "danger zone" quadrant, an AI Key Influencers visual explaining what drives high risk, the Top 10 riskiest suppliers, and a conditional-formatted risk scorecard.
4. **Supplier Performance** — On-time delivery trend, Top 10 on-time performers, a delivery-vs-defects quality quadrant, and an AI Smart Narrative summary.
5. **Contract Management** — $247M contract book valuation (de-duplicated), Top 10 contracts, a renewal-expiry timeline, a category treemap, and an at-risk-exposure measure (\~$35M tied to high-risk suppliers).
6. **AI Insights** — A spend forecast with confidence band, anomaly detection on monthly spend, K-means supplier clustering, and an executive AI summary.

\---

## AI \& Machine Learning Features

Seven distinct Power BI AI capabilities are demonstrated across the report:

|Feature|Page|What it surfaces|
|-|-|-|
|Decomposition Tree|Spend Analytics|Auto-finds the highest-spend dimension paths|
|Key Influencers|Supplier Risk|Drivers of high risk (e.g., IT-category suppliers \~7.5x more likely to be critical-risk)|
|Smart Narrative|Supplier Performance|Auto-written, filter-responsive performance insights|
|Q\&A|Contract Management|Natural-language querying of the data|
|Forecasting|AI Insights|Time-series projection of spend with a confidence band|
|Anomaly Detection|AI Insights|Auto-flags unusual spend months with explanations|
|K-means Clustering|AI Insights|Discovers supplier segments (mapped to Kraljic-style strategic sourcing)|

\---

## Key Technical Highlights

* **20+ DAX measures** powering dynamic KPIs: total/average spend, supplier concentration, risk scoring, on-time-target benchmarking, and Top-N ranking.
* **Robust data modeling** — de-duplicated contract valuation using `SUMX`/`MAX` patterns to prevent invoice-level double-counting; `COALESCE` to handle blank KPIs; validated column assumptions before building.
* **Top-N filtering** to surface the most material suppliers and contracts.
* **Synced slicers** carrying a supplier selection consistently across the risk, performance, and contract pages.
* **Consistent design system** — 1280x900 canvas, Segoe UI, white card layout with rounded borders, applied uniformly across six pages.

\---

## The Data

5,000 rows of realistic synthetic procurement data generated in Python (Faker library), spanning FY2023-2024. The dataset includes 16 columns: invoice details, supplier, category, country, department, amount, payment terms, on-time delivery, defect rate, lead time, risk score and level, and contract value and expiry.

*Note: all data is synthetic and contains no real or confidential information.*

\---

## How to View

* **Quick look:** open `exports/Procurement\_Intelligence\_Platform.pdf` for a full static walkthrough of all six pages.
* **Interactive:** download `dashboard/Procurement\_Intelligence\_Platform.pbix` and open it in [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (free).
* **Screenshots:** see the `screenshots/` folder.

\---

## Repository Structure

```
procurement-intelligence-platform/
├── README.md
├── data/
│   ├── procurement\_data.csv
│   └── generate\_data.py        # Python script that generated the dataset
├── dashboard/
│   └── Procurement\_Intelligence\_Platform.pbix
├── exports/
│   └── Procurement\_Intelligence\_Platform.pdf
└── screenshots/
    ├── 01\_executive\_summary.png
    ├── 02\_spend\_analytics.png
    ├── 03\_supplier\_risk.png
    ├── 04\_supplier\_performance.png
    ├── 05\_contract\_management.png
    └── 06\_ai\_insights.png
```

\---

## About

Built by **Harsh Patel** as a portfolio project.

* LinkedIn: https://www.linkedin.com/in/harshpatel510/ 

