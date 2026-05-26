"""
Global CSS — MediAI Fresh UI Redesign
Palette: deep violet-blue base + vivid cyan-mint + coral accent + amber
"""
import streamlit as st


def inject_styles():
    st.markdown("""
<style>
/* ══════════════════════════════════════════════════════════
   FONTS
══════════════════════════════════════════════════════════ */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');

/* ══════════════════════════════════════════════════════════
   DESIGN TOKENS
══════════════════════════════════════════════════════════ */
:root {
  --bg-base:      #0d0f1a;
  --bg-surface:   #13162a;
  --bg-card:      #181c35;
  --bg-hover:     #1e2340;
  --border:       rgba(255,255,255,0.07);
  --border-glow:  rgba(100,210,255,0.2);

  --cyan:      #00d4ff;
  --cyan-soft: #4de8ff;
  --cyan-dim:  rgba(0,212,255,0.15);
  --mint:      #00e5a0;
  --mint-soft: #4dffc4;
  --mint-dim:  rgba(0,229,160,0.15);
  --coral:     #ff6b6b;
  --coral-dim: rgba(255,107,107,0.15);
  --amber:     #ffb347;
  --amber-dim: rgba(255,179,71,0.15);
  --violet:    #a78bfa;
  --violet-dim:rgba(167,139,250,0.15);

  --text-primary:   #f0f4ff;
  --text-secondary: rgba(240,244,255,0.6);
  --text-muted:     rgba(240,244,255,0.35);

  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 18px;
  --radius-xl: 24px;

  --shadow-glow-cyan: 0 0 20px rgba(0,212,255,0.15);
  --shadow-glow-mint: 0 0 20px rgba(0,229,160,0.15);
  --shadow-card: 0 4px 24px rgba(0,0,0,0.4);
}

/* ══════════════════════════════════════════════════════════
   BASE RESET
══════════════════════════════════════════════════════════ */
html, body, [data-testid="stApp"] {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  background: var(--bg-base) !important;
  color: var(--text-primary) !important;
}

/* animated mesh gradient background */
[data-testid="stApp"]::before {
  content: '';
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
  background:
    radial-gradient(ellipse 80% 50% at 10% 10%, rgba(0,212,255,0.06) 0%, transparent 60%),
    radial-gradient(ellipse 60% 60% at 90% 80%, rgba(0,229,160,0.05) 0%, transparent 60%),
    radial-gradient(ellipse 50% 40% at 50% 50%, rgba(167,139,250,0.04) 0%, transparent 60%);
}

/* ══════════════════════════════════════════════════════════
   HIDE STREAMLIT CHROME
══════════════════════════════════════════════════════════ */
#MainMenu, footer, header              { visibility: hidden !important; }
[data-testid="stDecoration"]           { display: none !important; }
[data-testid="stSidebarCollapseButton"]{ display: none !important; }
[data-testid="collapsedControl"]       { display: none !important; }
button[data-testid="baseButton-header"]{ display: none !important; }
[data-testid="stSidebarNav"]           { display: none !important; }

/* ══════════════════════════════════════════════════════════
   SIDEBAR — FORCE OPEN
══════════════════════════════════════════════════════════ */
[data-testid="stSidebar"][aria-expanded="false"],
[data-testid="stSidebar"] {
  display: flex !important;
  visibility: visible !important;
  transform: translateX(0) !important;
  width: 280px !important;
  min-width: 280px !important;
  max-width: 280px !important;
  background: linear-gradient(160deg, #0e1225 0%, #111630 50%, #0d1020 100%) !important;
  border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebarContent"] { padding: 0 !important; width: 100% !important; }
[data-testid="stSidebar"] * {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  color: var(--text-primary) !important;
}

/* Sidebar buttons — base */
[data-testid="stSidebar"] .stButton > button {
  background: transparent !important;
  border: none !important;
  border-radius: var(--radius-sm) !important;
  color: var(--text-secondary) !important;
  font-size: 13.5px !important;
  font-weight: 500 !important;
  padding: 10px 14px !important;
  margin-bottom: 2px !important;
  text-align: left !important;
  width: 100% !important;
  transition: all 0.2s ease !important;
  box-shadow: none !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
  background: rgba(255,255,255,0.06) !important;
  color: var(--text-primary) !important;
  transform: translateX(2px) !important;
  box-shadow: none !important;
}
[data-testid="stSidebar"] .stButton > button:focus {
  box-shadow: none !important; outline: none !important;
}

/* active nav */
[data-testid="stSidebar"] .nav-active .stButton > button {
  background: linear-gradient(90deg, rgba(0,212,255,0.12), rgba(0,229,160,0.08)) !important;
  border-left: 3px solid var(--cyan) !important;
  color: var(--cyan-soft) !important;
  font-weight: 600 !important;
  padding-left: 11px !important;
}

/* emergency */
[data-testid="stSidebar"] .btn-emergency .stButton > button {
  background: var(--coral-dim) !important;
  border: 1px solid rgba(255,107,107,0.25) !important;
  color: #ffaaaa !important;
  font-weight: 600 !important;
}
[data-testid="stSidebar"] .btn-emergency .stButton > button:hover {
  background: rgba(255,107,107,0.22) !important;
}

/* logout */
[data-testid="stSidebar"] .btn-logout .stButton > button {
  background: rgba(255,255,255,0.04) !important;
  border: 1px solid var(--border) !important;
  color: var(--text-muted) !important;
  font-size: 12px !important;
  padding: 7px 10px !important;
}
[data-testid="stSidebar"] .btn-logout .stButton > button:hover {
  background: rgba(255,255,255,0.08) !important;
  color: var(--text-primary) !important;
}

/* ══════════════════════════════════════════════════════════
   SIDEBAR HTML COMPONENTS
══════════════════════════════════════════════════════════ */
.sb-logo {
  padding: 22px 18px 16px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 6px;
  display: flex; align-items: center; gap: 12px;
}
.sb-logo-icon {
  width: 42px; height: 42px; flex-shrink: 0;
  background: linear-gradient(135deg, #00d4ff, #00e5a0);
  border-radius: 13px;
  display: flex; align-items: center; justify-content: center;
  font-size: 20px;
  box-shadow: 0 4px 16px rgba(0,212,255,0.35);
}
.sb-logo-name {
  font-family: 'Playfair Display', serif !important;
  font-size: 19px; font-weight: 800;
  background: linear-gradient(90deg, #00d4ff, #00e5a0);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  letter-spacing: -0.3px;
}
.sb-logo-sub {
  font-size: 9px; letter-spacing: 2px;
  text-transform: uppercase; color: var(--text-muted) !important;
  -webkit-text-fill-color: var(--text-muted);
  margin-top: 1px;
}

.sb-section-label {
  font-size: 9px; letter-spacing: 1.8px; text-transform: uppercase;
  color: var(--text-muted) !important; padding: 14px 18px 4px; display: block;
}

.sb-divider { border: none; border-top: 1px solid var(--border); margin: 6px 14px; }

.sb-stats {
  display: grid; grid-template-columns: 1fr 1fr; gap: 6px; padding: 2px 12px 10px;
}
.sb-stat {
  background: rgba(255,255,255,0.03);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm); padding: 8px 10px;
  transition: border-color 0.2s;
}
.sb-stat:hover { border-color: var(--border-glow); }
.sb-stat-label { font-size: 9px; color: var(--text-muted) !important; text-transform:uppercase; letter-spacing:.5px; }
.sb-stat-value { font-size: 16px; font-weight: 700; color: white !important; margin-top: 2px; }
.sb-stat-unit  { font-size: 9px; color: var(--text-muted) !important; }

.sb-appt {
  margin: 0 12px 8px;
  background: linear-gradient(90deg, rgba(0,212,255,0.08), rgba(0,229,160,0.06));
  border: 1px solid rgba(0,212,255,0.2);
  border-radius: var(--radius-md); padding: 10px 13px;
}
.sb-appt-label { font-size: 9px; color: rgba(0,212,255,0.6) !important; text-transform:uppercase; letter-spacing:1px; }
.sb-appt-date  { font-size: 12.5px; font-weight: 700; color: var(--cyan) !important; }
.sb-appt-doc   { font-size: 11px; color: var(--text-muted) !important; margin-top: 1px; }

.sb-user {
  margin: 2px 12px 8px;
  background: rgba(255,255,255,0.03);
  border: 1px solid var(--border);
  border-radius: var(--radius-md); padding: 10px 13px;
  display: flex; align-items: center; gap: 10px;
}
.sb-avatar {
  width: 35px; height: 35px; border-radius: 50%; flex-shrink: 0;
  background: linear-gradient(135deg, #00d4ff, #a78bfa);
  display: flex; align-items: center; justify-content: center;
  font-size: 14px; font-weight: 700; color: white !important;
  box-shadow: 0 0 12px rgba(0,212,255,0.3);
}
.sb-user-name  { font-size: 13px; font-weight: 600; color: var(--text-primary) !important; }
.sb-user-role  { font-size: 10.5px; color: var(--text-muted) !important; margin-top: 1px; }

.sb-version {
  display: inline-flex; align-items: center; gap: 5px;
  background: rgba(0,212,255,0.08);
  border: 1px solid rgba(0,212,255,0.18);
  border-radius: 20px; padding: 3px 10px;
  font-size: 10px; color: var(--cyan) !important; margin: 4px 16px 2px;
}
.sb-footer {
  font-size: 10px; color: var(--text-muted) !important;
  line-height: 1.7; padding: 4px 16px 18px;
}

/* ══════════════════════════════════════════════════════════
   AUTH PAGE
══════════════════════════════════════════════════════════ */
.auth-hero {
  text-align: center; padding: 48px 0 28px;
}
.auth-logo-ring {
  width: 80px; height: 80px; margin: 0 auto 18px;
  background: linear-gradient(135deg, rgba(0,212,255,0.15), rgba(0,229,160,0.15));
  border: 2px solid rgba(0,212,255,0.3);
  border-radius: 24px;
  display: flex; align-items: center; justify-content: center;
  font-size: 36px;
  box-shadow: 0 0 40px rgba(0,212,255,0.2), inset 0 1px 0 rgba(255,255,255,0.1);
}
.auth-title {
  font-family: 'Playfair Display', serif !important;
  font-size: 36px; font-weight: 800;
  background: linear-gradient(90deg, #00d4ff 0%, #00e5a0 50%, #a78bfa 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  letter-spacing: -1px; margin-bottom: 6px;
}
.auth-sub {
  font-size: 13px; color: var(--text-muted); letter-spacing: .5px;
}
.auth-features {
  display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;
  margin-top: 20px;
}
.auth-feature-chip {
  background: rgba(255,255,255,0.04); border: 1px solid var(--border);
  border-radius: 20px; padding: 5px 14px;
  font-size: 11.5px; color: var(--text-secondary);
}

/* ══════════════════════════════════════════════════════════
   MAIN LAYOUT
══════════════════════════════════════════════════════════ */
.page-header {
  display: flex; align-items: flex-start; justify-content: space-between;
  margin-bottom: 20px; padding-bottom: 16px;
  border-bottom: 1px solid var(--border);
}
.page-title {
  font-family: 'Playfair Display', serif !important;
  font-size: 26px; font-weight: 800; color: var(--text-primary);
  letter-spacing: -0.5px; margin-bottom: 2px;
}
.page-subtitle { font-size: 13px; color: var(--text-muted); }

/* ══════════════════════════════════════════════════════════
   CARDS
══════════════════════════════════════════════════════════ */
.glass-card {
  background: rgba(24,28,53,0.8);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: 20px 22px;
  backdrop-filter: blur(12px);
  box-shadow: var(--shadow-card);
  transition: border-color 0.2s, box-shadow 0.2s;
}
.glass-card:hover {
  border-color: var(--border-glow);
  box-shadow: var(--shadow-card), var(--shadow-glow-cyan);
}

.metric-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 14px 16px;
  transition: all 0.2s;
  cursor: pointer;
}
.metric-card:hover {
  border-color: rgba(0,212,255,0.3);
  background: rgba(0,212,255,0.05);
  transform: translateY(-1px);
}
.metric-label { font-size: 10px; color: var(--text-muted); text-transform:uppercase; letter-spacing:.8px; margin-bottom:5px; }
.metric-value { font-size: 22px; font-weight: 700; color: white; letter-spacing:-0.5px; }
.metric-unit  { font-size: 11px; color: var(--text-muted); margin-left: 2px; }
.metric-status{ font-size: 11px; margin-top: 4px; display:flex; align-items:center; gap:4px; }
.status-ok    { color: var(--mint); }
.status-warn  { color: var(--amber); }
.status-dot   { width:6px; height:6px; border-radius:50%; display:inline-block; flex-shrink:0; }

/* ══════════════════════════════════════════════════════════
   WELCOME / QUICK START
══════════════════════════════════════════════════════════ */
.welcome-wrap { text-align: center; padding: 50px 20px 36px; }
.welcome-pulse {
  width: 72px; height: 72px; margin: 0 auto 20px;
  background: linear-gradient(135deg, rgba(0,212,255,0.15), rgba(0,229,160,0.15));
  border: 1px solid rgba(0,212,255,0.25);
  border-radius: 20px;
  display: flex; align-items: center; justify-content: center;
  font-size: 30px;
  animation: pulse-glow 3s ease-in-out infinite;
  box-shadow: 0 0 0 0 rgba(0,212,255,0.3);
}
@keyframes pulse-glow {
  0%, 100% { box-shadow: 0 0 0 0 rgba(0,212,255,0.3); }
  50%       { box-shadow: 0 0 0 12px rgba(0,212,255,0); }
}
.welcome-title {
  font-family: 'Playfair Display', serif !important;
  font-size: 30px; font-weight: 800;
  background: linear-gradient(90deg, #f0f4ff, #00d4ff, #00e5a0);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  margin-bottom: 10px; letter-spacing: -0.5px;
}
.welcome-sub {
  font-size: 14px; color: var(--text-muted);
  max-width: 420px; margin: 0 auto 32px; line-height: 1.75;
}

/* Quick prompt cards */
.qcard {
  background: rgba(255,255,255,0.03);
  border: 1px solid var(--border);
  border-radius: var(--radius-md); padding: 14px 16px;
  cursor: pointer; transition: all 0.2s; text-align: left;
}
.qcard:hover {
  background: rgba(0,212,255,0.06);
  border-color: rgba(0,212,255,0.3);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.3), 0 0 12px rgba(0,212,255,0.1);
}
.qcard-icon  { font-size: 22px; margin-bottom: 8px; }
.qcard-title { font-size: 13px; font-weight: 600; color: var(--text-primary); margin-bottom: 4px; }
.qcard-desc  { font-size: 11.5px; color: var(--text-muted); line-height: 1.5; }

/* ══════════════════════════════════════════════════════════
   CHAT BUBBLES
══════════════════════════════════════════════════════════ */
.chat-message {
  display: flex; gap: 12px; align-items: flex-start;
  margin-bottom: 18px; animation: msgIn 0.3s ease;
}
@keyframes msgIn {
  from { opacity:0; transform:translateY(10px); }
  to   { opacity:1; transform:translateY(0); }
}
.chat-message.user { flex-direction: row-reverse; }
.msg-avatar {
  width: 34px; height: 34px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 14px; flex-shrink: 0; margin-top: 2px;
}
.avatar-ai {
  background: linear-gradient(135deg, rgba(0,212,255,0.2), rgba(0,229,160,0.2));
  border: 1px solid rgba(0,212,255,0.25);
}
.avatar-user {
  background: linear-gradient(135deg, #a78bfa, #00d4ff);
  color: white !important; font-weight: 700; font-size: 13px;
}
.msg-bubble {
  max-width: 74%; padding: 13px 17px;
  border-radius: 16px; font-size: 13.5px; line-height: 1.7;
}
.bubble-ai {
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  color: var(--text-primary); border-top-left-radius: 4px;
}
.bubble-user {
  background: linear-gradient(135deg, rgba(0,212,255,0.15), rgba(167,139,250,0.15));
  border: 1px solid rgba(0,212,255,0.2);
  color: var(--text-primary); border-top-right-radius: 4px;
}
.msg-disclaimer {
  font-size: 11px; color: var(--text-muted);
  margin-top: 8px; padding-top: 8px;
  border-top: 1px solid rgba(255,255,255,0.07);
}

/* ══════════════════════════════════════════════════════════
   BADGES
══════════════════════════════════════════════════════════ */
.badge {
  display: inline-flex; align-items: center; gap: 4px;
  font-size: 11px; padding: 4px 11px; border-radius: 20px; font-weight: 600;
  letter-spacing: .3px; margin-right: 6px;
}
.badge-cyan  { background: rgba(0,212,255,0.12); color: var(--cyan);  border: 1px solid rgba(0,212,255,0.25); }
.badge-mint  { background: rgba(0,229,160,0.12); color: var(--mint);  border: 1px solid rgba(0,229,160,0.25); }
.badge-coral { background: var(--coral-dim);     color: #ffaaaa;       border: 1px solid rgba(255,107,107,0.3);}
.badge-amber { background: var(--amber-dim);     color: var(--amber);  border: 1px solid rgba(255,179,71,0.3); }
.badge-violet{ background: var(--violet-dim);    color: var(--violet); border: 1px solid rgba(167,139,250,0.3);}

/* backward compat */
.badge-teal  { background: rgba(0,229,160,0.12); color: var(--mint);  border: 1px solid rgba(0,229,160,0.25); }
.badge-blue  { background: rgba(0,212,255,0.12); color: var(--cyan);  border: 1px solid rgba(0,212,255,0.25); }
.badge-warn  { background: var(--amber-dim);     color: var(--amber);  border: 1px solid rgba(255,179,71,0.3); }

/* ══════════════════════════════════════════════════════════
   INFO / WARN BOXES
══════════════════════════════════════════════════════════ */
.info-box {
  background: rgba(0,212,255,0.07);
  border: 1px solid rgba(0,212,255,0.2);
  border-left: 3px solid var(--cyan);
  border-radius: var(--radius-md); padding: 12px 16px;
  font-size: 13px; color: #a8e6f0; margin-bottom: 16px;
}
.warn-box {
  background: rgba(255,107,107,0.07);
  border: 1px solid rgba(255,107,107,0.2);
  border-left: 3px solid var(--coral);
  border-radius: var(--radius-md); padding: 12px 16px;
  font-size: 13px; color: #ffcccc; margin-bottom: 16px;
}

/* ══════════════════════════════════════════════════════════
   SECTION HEADERS
══════════════════════════════════════════════════════════ */
.section-header {
  font-family: 'Playfair Display', serif !important;
  font-size: 24px; font-weight: 800; color: var(--text-primary);
  letter-spacing: -0.4px; margin-bottom: 4px;
}
.section-sub { font-size: 13px; color: var(--text-muted); margin-bottom: 22px; }

/* ══════════════════════════════════════════════════════════
   VITAL DETAIL CARD
══════════════════════════════════════════════════════════ */
.vital-detail-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg); padding: 20px 22px; margin-bottom: 16px;
  transition: border-color 0.2s;
}
.vital-detail-card:hover { border-color: var(--border-glow); }

/* mcard compat */
.mcard { background: rgba(255,255,255,0.03); border: 1px solid var(--border); border-radius: var(--radius-md); padding: 13px 16px; transition: all 0.2s; }
.mcard:hover { border-color: rgba(0,212,255,0.3); background: rgba(0,212,255,0.04); transform: translateY(-1px); }
.mcard-label { font-size: 10px; color: var(--text-muted); text-transform:uppercase; letter-spacing:.6px; margin-bottom:4px; }
.mcard-value { font-size: 20px; font-weight: 700; color: white; letter-spacing:-0.5px; }
.mcard-unit  { font-size: 11px; color: var(--text-muted); margin-left:2px; }
.mcard-status{ font-size: 10.5px; margin-top:4px; }
.status-normal { color: var(--mint); }
.status-warning { color: var(--amber); }

/* ══════════════════════════════════════════════════════════
   STREAMLIT WIDGET OVERRIDES
══════════════════════════════════════════════════════════ */
/* Inputs */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stNumberInput"] input {
  background: rgba(255,255,255,0.04) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-md) !important;
  color: var(--text-primary) !important;
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 13.5px !important;
  transition: border-color 0.2s !important;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stTextArea"] textarea:focus {
  border-color: rgba(0,212,255,0.4) !important;
  box-shadow: 0 0 0 3px rgba(0,212,255,0.08) !important;
}

/* Select box */
[data-testid="stSelectbox"] > div > div {
  background: rgba(255,255,255,0.04) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-md) !important;
  color: var(--text-primary) !important;
}

/* Main area buttons */
section.main .stButton > button {
  background: linear-gradient(135deg, #00d4ff, #00e5a0) !important;
  color: #0d0f1a !important;
  border: none !important;
  border-radius: var(--radius-md) !important;
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-weight: 700 !important;
  font-size: 13.5px !important;
  letter-spacing: .3px !important;
  transition: all 0.2s !important;
  box-shadow: 0 4px 16px rgba(0,212,255,0.25) !important;
}
section.main .stButton > button:hover {
  transform: translateY(-1px) !important;
  box-shadow: 0 6px 24px rgba(0,212,255,0.35) !important;
  opacity: 0.95 !important;
}

/* Tabs */
[data-testid="stTabs"] button {
  color: var(--text-muted) !important;
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-weight: 500 !important;
  font-size: 13px !important;
}
[data-testid="stTabs"] button[aria-selected="true"] {
  color: var(--cyan) !important;
  border-bottom-color: var(--cyan) !important;
}

/* Sliders */
[data-testid="stSlider"] > div > div > div {
  background: linear-gradient(90deg, var(--cyan), var(--mint)) !important;
}

/* Checkboxes */
[data-testid="stCheckbox"] label { color: var(--text-secondary) !important; font-size: 13px !important; }

/* Expander */
[data-testid="stExpander"] > details > summary {
  background: rgba(255,255,255,0.03) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-md) !important;
  color: var(--text-primary) !important;
  font-weight: 500 !important;
}
[data-testid="stExpander"] > details > summary:hover {
  border-color: var(--border-glow) !important;
  background: rgba(0,212,255,0.04) !important;
}

/* Dataframe */
[data-testid="stDataFrame"] {
  border-radius: var(--radius-md) !important;
  overflow: hidden !important;
}

/* Dividers */
hr { border-color: var(--border) !important; }

/* Streamlit success / error / warning / info */
[data-testid="stAlert"] {
  border-radius: var(--radius-md) !important;
  border: none !important;
}

/* Plotly transparent bg */
.js-plotly-plot .plotly, .js-plotly-plot .plotly .svg-container { background: transparent !important; }

/* ══════════════════════════════════════════════════════════
   SCROLLBAR
══════════════════════════════════════════════════════════ */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(0,212,255,0.15); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(0,212,255,0.3); }
</style>
""", unsafe_allow_html=True)
