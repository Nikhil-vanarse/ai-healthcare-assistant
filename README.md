# 🩺 MediAI — AI Healthcare Assistant (Groq + SQLite)

A full-featured AI-powered healthcare assistant built with **Streamlit**, **Groq (Llama 3.3 70B)**, and **SQLite**.

---

## 📁 Project Structure

```
mediAI/
├── app.py                            # Entry point — DB init, auth gate, routing
├── requirements.txt
├── .env.example
├── .streamlit/config.toml            # Dark theme
│
├── database/
│   ├── db.py                         # SQLite schema + connection manager
│   ├── user_queries.py               # Auth, profiles, medications, allergies,
│   │                                 #   conditions, appointments
│   └── data_queries.py               # Chat sessions/messages, vitals, symptom
│                                     #   checks, drug searches, wellness plans
│
├── pages/
│   ├── auth.py                       # Login / Register
│   ├── chat.py                       # AI chat — messages persisted to DB
│   ├── symptom_checker.py            # Symptom form — results saved to DB
│   ├── vitals.py                     # Vitals dashboard + log form → DB
│   ├── drug_info.py                  # Drug search — saved to DB
│   ├── wellness.py                   # Nutrition / exercise / mental plans → DB
│   ├── profile.py                    # Full health profile (meds, allergies…)
│   └── history.py                    # View all saved records
│
├── components/
│   ├── sidebar.py                    # Nav + user card + upcoming appt badge
│   └── styles.py                     # Global CSS (dark medical theme)
│
└── utils/
    ├── claude_api.py                 # Groq streaming API integration
    └── health_data.py                # Constants and sample data
```

---

## 🗄️ Database Schema (SQLite — 12 tables)

| Table               | Purpose                                      |
|---------------------|----------------------------------------------|
| `users`             | Accounts (username, password hash, email)    |
| `user_profiles`     | Demographics, emergency contact, doctor info |
| `vitals_records`    | Timestamped HR, BP, glucose, SpO₂, weight…  |
| `chat_sessions`     | Named conversation threads per user          |
| `chat_messages`     | Every user + AI message, linked to session   |
| `symptom_checks`    | Symptom checker inputs + AI response         |
| `drug_searches`     | Drug name, info type, AI response            |
| `wellness_plans`    | Nutrition / exercise / mental AI plans       |
| `medications`       | Current medication list                      |
| `allergies`         | Allergen, reaction, severity                 |
| `medical_conditions`| Chronic / past conditions with status        |
| `appointments`      | Upcoming / past doctor appointments          |

The DB file is created automatically at `data/mediAI.db` on first run.

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set your Groq API key (free at https://console.groq.com)
export GROQ_API_KEY="gsk_your_key_here"

# 3. Run
streamlit run app.py
```

Or add your key to `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "gsk_your_key_here"
```

---

## ✨ Features

| Page | What it does | DB tables used |
|------|-------------|----------------|
| **Auth** | Register / login with hashed passwords | `users`, `user_profiles` |
| **AI Chat** | Streaming chat, sessions saved & resumable | `chat_sessions`, `chat_messages` |
| **Symptom Checker** | Structured form → AI analysis → saved | `symptom_checks` |
| **Vitals Dashboard** | Charts + log form for real readings | `vitals_records` |
| **Drug Information** | Drug search + interaction checker → saved | `drug_searches` |
| **Wellness & Nutrition** | Personalized plans → saved | `wellness_plans` |
| **My Profile** | Full health record management | `user_profiles`, `medications`, `allergies`, `medical_conditions`, `appointments` |
| **My History** | View / resume / delete all saved records | All tables |

---

## 🔒 Security

- Passwords stored as `SHA-256(salt + password)` — never plaintext
- All queries use parameterised statements — no SQL injection risk
- Every query verifies `user_id` ownership before returning data
- WAL journal mode + foreign keys enforced

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| UI | Streamlit 1.35+ |
| AI | Groq API · Llama 3.3 70B |
| Database | SQLite 3 (built-in, zero setup) |
| Charts | Plotly 5 |
| Language | Python 3.10+ |

---

> ⚕️ **Medical Disclaimer**: MediAI provides health information only — not diagnosis or treatment. Always consult a qualified healthcare professional. In an emergency, call 911 / 112 immediately.
