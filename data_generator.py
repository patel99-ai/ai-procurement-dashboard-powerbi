import csv
import random
from datetime import datetime, timedelta

# 50 realistic suppliers
suppliers = [
    ("GlobalTech Systems", "IT", "China"), ("CloudBase Inc.", "IT", "USA"),
    ("DataCore Solutions", "IT", "India"), ("NetSphere Ltd.", "IT", "Germany"),
    ("ByteWave Technologies", "IT", "USA"), ("SkyHost Pro", "IT", "Ireland"),
    ("FastFreight Co.", "Logistics", "Mexico"), ("SkyLog Partners", "Logistics", "USA"),
    ("OceanShip Ltd.", "Logistics", "Singapore"), ("SwiftCargo Inc.", "Logistics", "UAE"),
    ("RapidRoute LLC", "Logistics", "Canada"), ("GlobalMove Co.", "Logistics", "Netherlands"),
    ("MetalWorks Ltd.", "Raw Materials", "Russia"), ("PrimeParts Mfg.", "Raw Materials", "India"),
    ("SteelCore Inc.", "Raw Materials", "Brazil"), ("AlloyCraft Ltd.", "Raw Materials", "South Korea"),
    ("IronPeak Mfg.", "Raw Materials", "Turkey"), ("MetalMax Co.", "Raw Materials", "China"),
    ("CleanSpace Services", "Facilities", "USA"), ("BuildRight Co.", "Facilities", "UK"),
    ("FacilityPro Ltd.", "Facilities", "Canada"), ("SpaceWorks Inc.", "Facilities", "Australia"),
    ("MediSupply Co.", "Healthcare", "USA"), ("PharmaCare Ltd.", "Healthcare", "Switzerland"),
    ("HealthBridge Inc.", "Healthcare", "Germany"), ("MedCore Solutions", "Healthcare", "India"),
    ("PowerGen Ltd.", "Energy", "Norway"), ("SolarMax Inc.", "Energy", "USA"),
    ("GreenWatt Co.", "Energy", "Denmark"), ("EnergyPrime Ltd.", "Energy", "UAE"),
    ("AdMax Agency", "Marketing", "USA"), ("BrandCore Ltd.", "Marketing", "UK"),
    ("MediaPulse Inc.", "Marketing", "Australia"), ("CreativeHub Co.", "Marketing", "Canada"),
    ("LegalEdge LLP", "Legal", "USA"), ("CompliancePro Ltd.", "Legal", "UK"),
    ("LawBridge Inc.", "Legal", "Singapore"), ("JurisCore Co.", "Legal", "Germany"),
    ("TravelEase Inc.", "Travel", "USA"), ("FlightPro Ltd.", "Travel", "UAE"),
    ("StayBridge Co.", "Travel", "France"), ("TripCore Inc.", "Travel", "India"),
    ("OfficePlus Ltd.", "Office Supplies", "USA"), ("DeskPro Inc.", "Office Supplies", "China"),
    ("SupplyBase Co.", "Office Supplies", "India"), ("PrintCore Ltd.", "Office Supplies", "Germany"),
    ("ConsultPro Inc.", "Consulting", "USA"), ("StratEdge Ltd.", "Consulting", "UK"),
    ("AdvisoryCore Co.", "Consulting", "Singapore"), ("InsightBridge LLC", "Consulting", "Australia")
]

departments = ["Engineering", "Operations", "Finance", "HR", "Marketing",
               "Manufacturing", "Legal", "Procurement", "IT", "Sales"]

payment_terms = ["Net 30", "Net 45", "Net 60", "Net 90", "2/10 Net 30"]

invoice_descriptions = {
    "IT": ["Cloud server hosting monthly fee", "Software license renewal",
           "Cybersecurity audit services", "IT infrastructure upgrade",
           "SaaS platform subscription", "Network equipment purchase",
           "Data storage solution", "IT support and maintenance"],
    "Logistics": ["International freight forwarding", "Last mile delivery services",
                  "Warehouse storage monthly fee", "Cross border shipping charges",
                  "Fleet maintenance services", "Cold chain logistics",
                  "Express courier services", "Port handling charges"],
    "Raw Materials": ["Steel rods bulk purchase", "Aluminum sheets order",
                      "Copper wire batch delivery", "Plastic components supply",
                      "Chemical compounds order", "Rubber seals batch",
                      "Iron ore bulk shipment", "Carbon fiber materials"],
    "Facilities": ["Office cleaning monthly contract", "Building maintenance services",
                   "HVAC system repair", "Security services monthly",
                   "Pest control quarterly", "Elevator maintenance",
                   "Parking management fees", "Waste disposal services"],
    "Healthcare": ["Medical supplies monthly order", "PPE equipment bulk purchase",
                   "Lab testing services", "Employee health screening",
                   "Medical equipment lease", "Pharmacy supplies order",
                   "First aid kit restocking", "Occupational health services"],
    "Energy": ["Electricity supply monthly bill", "Solar panel maintenance",
               "Gas supply quarterly", "Energy audit services",
               "Generator fuel supply", "Wind turbine maintenance",
               "Power backup services", "Utility management fees"],
    "Marketing": ["Digital advertising campaign", "Social media management",
                  "Brand design services", "Market research report",
                  "PR agency monthly retainer", "Event management services",
                  "Content creation services", "SEO optimization services"],
    "Legal": ["Contract review services", "Compliance audit fees",
              "Legal consultation monthly", "Patent filing fees",
              "Trademark registration", "Litigation support services",
              "Regulatory filing fees", "Corporate governance advisory"],
    "Travel": ["Business class flights booking", "Hotel accommodation corporate",
               "Car rental services", "Travel insurance premium",
               "Visa processing fees", "Airport transfer services",
               "Conference registration fees", "Per diem expenses"],
    "Office Supplies": ["Printer paper bulk order", "Office furniture purchase",
                        "Stationery monthly supply", "Printer cartridge order",
                        "Desk equipment purchase", "Filing cabinet order",
                        "Whiteboard and markers", "Coffee machine supplies"],
    "Consulting": ["Strategy consulting project", "Business process review",
                   "Change management advisory", "Financial consulting services",
                   "Operations improvement project", "Digital transformation advisory",
                   "Supply chain consulting", "HR transformation project"]
}

# Risk scores per supplier
risk_data = {
    "GlobalTech Systems": (88, "Critical"), "CloudBase Inc.": (42, "Medium"),
    "DataCore Solutions": (35, "Medium"), "NetSphere Ltd.": (25, "Low"),
    "ByteWave Technologies": (18, "Low"), "SkyHost Pro": (20, "Low"),
    "FastFreight Co.": (71, "High"), "SkyLog Partners": (22, "Low"),
    "OceanShip Ltd.": (55, "High"), "SwiftCargo Inc.": (60, "High"),
    "RapidRoute LLC": (28, "Low"), "GlobalMove Co.": (32, "Low"),
    "MetalWorks Ltd.": (65, "High"), "PrimeParts Mfg.": (18, "Low"),
    "SteelCore Inc.": (48, "Medium"), "AlloyCraft Ltd.": (38, "Medium"),
    "IronPeak Mfg.": (62, "High"), "MetalMax Co.": (75, "Critical"),
    "CleanSpace Services": (15, "Low"), "BuildRight Co.": (20, "Low"),
    "FacilityPro Ltd.": (18, "Low"), "SpaceWorks Inc.": (12, "Low"),
    "MediSupply Co.": (22, "Low"), "PharmaCare Ltd.": (28, "Low"),
    "HealthBridge Inc.": (30, "Low"), "MedCore Solutions": (45, "Medium"),
    "PowerGen Ltd.": (25, "Low"), "SolarMax Inc.": (15, "Low"),
    "GreenWatt Co.": (18, "Low"), "EnergyPrime Ltd.": (52, "Medium"),
    "AdMax Agency": (20, "Low"), "BrandCore Ltd.": (22, "Low"),
    "MediaPulse Inc.": (18, "Low"), "CreativeHub Co.": (15, "Low"),
    "LegalEdge LLP": (12, "Low"), "CompliancePro Ltd.": (15, "Low"),
    "LawBridge Inc.": (28, "Low"), "JurisCore Co.": (22, "Low"),
    "TravelEase Inc.": (18, "Low"), "FlightPro Ltd.": (45, "Medium"),
    "StayBridge Co.": (25, "Low"), "TripCore Inc.": (35, "Medium"),
    "OfficePlus Ltd.": (10, "Low"), "DeskPro Inc.": (40, "Medium"),
    "SupplyBase Co.": (30, "Low"), "PrintCore Ltd.": (20, "Low"),
    "ConsultPro Inc.": (15, "Low"), "StratEdge Ltd.": (18, "Low"),
    "AdvisoryCore Co.": (22, "Low"), "InsightBridge LLC": (20, "Low")
}

# Contract data
def get_contract_date():
    today = datetime.now()
    days = random.randint(-30, 365)
    return (today + timedelta(days=days)).strftime("%Y-%m-%d")

def get_contract_value():
    return random.randint(100000, 5000000)

print("Generating 5000 rows of procurement data...")

spend_rows = []
start_date = datetime(2023, 1, 1)

for i in range(5000):
    supplier_info = random.choice(suppliers)
    supplier_name = supplier_info[0]
    category = supplier_info[1]
    country = supplier_info[2]
    department = random.choice(departments)
    descriptions = invoice_descriptions.get(category, ["General procurement"])
    description = random.choice(descriptions)
    amount = random.randint(5000, 500000)
    days_offset = random.randint(0, 729)
    date = (start_date + timedelta(days=days_offset)).strftime("%Y-%m-%d")
    payment = random.choice(payment_terms)
    on_time = random.choices(["Yes", "No"], weights=[75, 25])[0]
    defect_rate = round(random.uniform(0, 8), 1)
    lead_time = random.randint(1, 45)
    risk_score, risk_level = risk_data.get(supplier_name, (30, "Low"))
    risk_score = min(100, max(0, risk_score + random.randint(-5, 5)))
    contract_value = get_contract_value()
    contract_expiry = get_contract_date()
    spend_rows.append([
        i+1, date, supplier_name, category, country,
        department, description, amount, payment,
        on_time, defect_rate, lead_time,
        risk_score, risk_level, contract_value, contract_expiry
    ])

headers = [
    "Invoice_ID", "Date", "Supplier", "Category", "Country",
    "Department", "Invoice_Description", "Amount", "Payment_Terms",
    "On_Time_Delivery", "Defect_Rate_Pct", "Lead_Time_Days",
    "Risk_Score", "Risk_Level", "Contract_Value", "Contract_Expiry_Date"
]

with open("procurement_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(spend_rows)

print("Done! File saved as procurement_data.csv")
print(f"Total rows generated: 5000")
print(f"Total suppliers: 50")
print(f"Categories: IT, Logistics, Raw Materials, Facilities, Healthcare,")
print(f"            Energy, Marketing, Legal, Travel, Office Supplies, Consulting")
print(f"Countries: 20+")
print("Now load procurement_data.csv into Power BI!")