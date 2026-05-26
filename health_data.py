"""
Health constants, sample data, and helper functions for MediAI.
"""

# ── Symptom list ──────────────────────────────────────────────────────────────
SYMPTOMS = [
    ("🤕", "Headache"),
    ("🤒", "Fever"),
    ("😮‍💨", "Shortness of breath"),
    ("🤢", "Nausea / Vomiting"),
    ("😴", "Fatigue"),
    ("🦴", "Joint / Bone pain"),
    ("🤧", "Runny nose / Congestion"),
    ("😮", "Cough"),
    ("🤔", "Dizziness"),
    ("💔", "Chest pain / Tightness"),
    ("🌡️", "Chills / Shivering"),
    ("👁️", "Blurred vision"),
    ("🫄", "Stomach / Abdominal pain"),
    ("🦵", "Muscle weakness"),
    ("💧", "Excessive thirst / Urination"),
    ("😤", "Sore throat"),
    ("🧠", "Difficulty concentrating"),
    ("🖐️", "Skin rash / Itching"),
    ("😞", "Loss of appetite"),
    ("👂", "Ear pain / Ringing"),
]

# ── Body systems ──────────────────────────────────────────────────────────────
BODY_SYSTEMS = [
    "Cardiovascular",
    "Respiratory",
    "Digestive / GI",
    "Musculoskeletal",
    "Neurological",
    "Endocrine",
    "Dermatological",
    "Urinary",
    "Reproductive",
    "Mental Health",
]

# ── Symptom duration options ──────────────────────────────────────────────────
DURATIONS = {
    "Just started (< 24 hours)": "less than 24 hours",
    "A few days (2–4 days)": "2–4 days",
    "About a week": "about a week",
    "1–2 weeks": "1–2 weeks",
    "Several weeks (> 2 weeks)": "several weeks",
    "Months": "several months",
    "Chronic (> 6 months)": "over 6 months (chronic)",
}

# ── Sample vitals data for the dashboard ─────────────────────────────────────
SAMPLE_VITALS_HISTORY = {
    "dates": [
        "May 1", "May 5", "May 8", "May 12",
        "May 15", "May 18", "May 20", "May 22",
    ],
    "heart_rate": [74, 71, 76, 73, 70, 72, 75, 72],
    "systolic":   [122, 118, 125, 120, 117, 118, 119, 118],
    "diastolic":  [ 80,  77,  82,  79,  76,  78,  78,  78],
    "glucose":    [ 98,  95, 102,  96,  94,  95,  97,  95],
    "spo2":       [ 98,  99,  97,  98,  99,  98,  99,  98],
    "weight_kg":  [ 78,  78,  77.5, 77.5, 77, 77, 76.8, 76.5],
}

CURRENT_VITALS = {
    "heart_rate":  {"value": 72,    "unit": "bpm",   "label": "Heart Rate",    "status": "normal"},
    "blood_pressure": {"value": "118/78", "unit": "mmHg", "label": "Blood Pressure", "status": "normal"},
    "glucose":     {"value": 95,    "unit": "mg/dL", "label": "Blood Glucose", "status": "normal"},
    "bmi":         {"value": 26.1,  "unit": "",      "label": "BMI",           "status": "warning"},
    "spo2":        {"value": 98,    "unit": "%",     "label": "SpO₂",          "status": "normal"},
    "temp":        {"value": 98.6,  "unit": "°F",    "label": "Temperature",   "status": "normal"},
}

# ── Common drugs database ─────────────────────────────────────────────────────
COMMON_DRUGS = [
    "Ibuprofen", "Paracetamol / Acetaminophen", "Aspirin", "Amoxicillin",
    "Metformin", "Atorvastatin", "Lisinopril", "Omeprazole",
    "Amlodipine", "Cetirizine", "Azithromycin", "Pantoprazole",
    "Sertraline", "Escitalopram", "Levothyroxine", "Doxycycline",
    "Hydrochlorothiazide", "Gabapentin", "Prednisone", "Furosemide",
]

# ── Wellness topics ────────────────────────────────────────────────────────────
WELLNESS_TOPICS = [
    ("🥗", "Heart-Healthy Diet",          "Evidence-based nutrition for cardiovascular health"),
    ("🏃", "Exercise & Physical Activity", "WHO-recommended activity guidelines by age group"),
    ("😴", "Sleep Hygiene",               "Sleep science and strategies for better rest"),
    ("🧘", "Stress Management",           "Evidence-based techniques to reduce chronic stress"),
    ("🚭", "Quit Smoking Support",        "Strategies and resources to stop smoking"),
    ("🫀", "Diabetes Prevention",         "Lifestyle changes to reduce type-2 diabetes risk"),
    ("🧠", "Mental Health Basics",        "Understanding anxiety, depression, and coping tools"),
    ("💪", "Weight Management",           "Healthy, sustainable approaches to weight control"),
]
