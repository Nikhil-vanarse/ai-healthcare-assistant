"""components/sidebar.py — Vivid redesigned sidebar"""
import streamlit as st
from database.user_queries import get_appointments, get_medications, get_allergies
from database.data_queries  import get_chat_sessions, get_vitals_history

NAV_GROUPS = [
    ("MAIN", [
        ("chat",            "💬", "AI Health Chat",      "#00d4ff"),
        ("symptom_checker", "🔍", "Symptom Checker",     "#00e5a0"),
        ("vitals",          "📊", "Vitals Dashboard",    "#a78bfa"),
    ]),
    ("TOOLS", [
        ("drug_info",  "💊", "Drug Information",    "#ffb347"),
        ("wellness",   "🧠", "Wellness & Nutrition", "#ff6b6b"),
    ]),
    ("MY RECORDS", [
        ("history", "🗂️", "My History", "#4de8ff"),
        ("profile",  "👤", "My Profile",  "#c4b5fd"),
    ]),
]

EMERGENCY_PROMPT = (
    "What are the warning signs of a heart attack, stroke, and severe "
    "allergic reaction? What should I do immediately in each case?"
)

SIDEBAR_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');

/* ── Force sidebar open ── */
[data-testid="stSidebar"][aria-expanded="false"],
[data-testid="stSidebar"] {
  display:flex!important;visibility:visible!important;
  transform:translateX(0)!important;
  width:282px!important;min-width:282px!important;max-width:282px!important;
  background:linear-gradient(160deg,#0a0e1f 0%,#0d1228 60%,#0a0e1c 100%)!important;
  border-right:1px solid rgba(255,255,255,0.06)!important;
}
[data-testid="stSidebarContent"]{padding:0!important;width:100%!important;}
[data-testid="stSidebar"] *{font-family:'Plus Jakarta Sans',sans-serif!important;color:#f0f4ff!important;}
[data-testid="stSidebarCollapseButton"],[data-testid="collapsedControl"],
button[data-testid="baseButton-header"],[data-testid="stSidebarNav"]{display:none!important;}

/* Base nav buttons */
[data-testid="stSidebar"] .stButton>button{
  background:transparent!important;border:none!important;
  border-radius:10px!important;color:rgba(240,244,255,0.55)!important;
  font-size:13.5px!important;font-weight:500!important;
  padding:9px 14px!important;margin-bottom:2px!important;
  text-align:left!important;width:100%!important;
  transition:all 0.18s ease!important;box-shadow:none!important;
}
[data-testid="stSidebar"] .stButton>button:hover{
  background:rgba(255,255,255,0.06)!important;
  color:rgba(240,244,255,0.9)!important;
  transform:translateX(3px)!important;box-shadow:none!important;
}
[data-testid="stSidebar"] .stButton>button:focus{box-shadow:none!important;outline:none!important;}

/* Active nav button */
[data-testid="stSidebar"] .nav-active .stButton>button{
  background:linear-gradient(90deg,rgba(0,212,255,0.14),rgba(0,212,255,0.04))!important;
  border-left:3px solid #00d4ff!important;
  color:#4de8ff!important;font-weight:700!important;
  padding-left:11px!important;box-shadow:none!important;
}

/* Emergency button */
[data-testid="stSidebar"] .btn-emergency .stButton>button{
  background:rgba(255,107,107,0.1)!important;
  border:1px solid rgba(255,107,107,0.22)!important;
  color:#ffaaaa!important;font-weight:600!important;border-radius:10px!important;
}
[data-testid="stSidebar"] .btn-emergency .stButton>button:hover{
  background:rgba(255,107,107,0.2)!important;transform:none!important;
}

/* Logout */
[data-testid="stSidebar"] .btn-logout .stButton>button{
  background:rgba(255,255,255,0.03)!important;
  border:1px solid rgba(255,255,255,0.07)!important;
  color:rgba(240,244,255,0.45)!important;font-size:12px!important;padding:7px 10px!important;
}
[data-testid="stSidebar"] .btn-logout .stButton>button:hover{
  background:rgba(255,255,255,0.07)!important;color:rgba(240,244,255,0.85)!important;transform:none!important;
}
</style>
"""

def _stats(uid):
    s = {"sessions":0,"meds":0,"vitals":0,"allergies":0}
    try: s["sessions"] = len(get_chat_sessions(uid, limit=200))
    except: pass
    try: s["meds"] = len(get_medications(uid, active_only=True))
    except: pass
    try: s["vitals"] = len(get_vitals_history(uid, limit=200))
    except: pass
    try: s["allergies"] = len(get_allergies(uid))
    except: pass
    return s

def _next_appt(uid):
    try:
        u = get_appointments(uid, upcoming_only=True)
        return u[0] if u else None
    except: return None

def render_sidebar():
    uid      = st.session_state.user_id
    page     = st.session_state.page
    name     = st.session_state.full_name or st.session_state.username or "User"
    username = st.session_state.username or ""
    initial  = name[0].upper()
    stats    = _stats(uid)
    appt     = _next_appt(uid)

    with st.sidebar:
        st.markdown(SIDEBAR_CSS, unsafe_allow_html=True)

        # ── Logo ──────────────────────────────────────────────────────────
        st.markdown(f"""
        <div style="padding:20px 16px 14px;border-bottom:1px solid rgba(255,255,255,0.06);margin-bottom:4px;
          display:flex;align-items:center;gap:12px;">
          <div style="width:42px;height:42px;flex-shrink:0;
            background:linear-gradient(135deg,#00d4ff,#00e5a0);border-radius:13px;
            display:flex;align-items:center;justify-content:center;font-size:20px;
            box-shadow:0 4px 16px rgba(0,212,255,0.35);">🩺</div>
          <div>
            <div style="font-family:'Playfair Display',serif!important;font-size:18px;font-weight:800;
              background:linear-gradient(90deg,#00d4ff,#00e5a0);
              -webkit-background-clip:text;-webkit-text-fill-color:transparent;">MediAI</div>
            <div style="font-size:9px;letter-spacing:2px;text-transform:uppercase;
              color:rgba(240,244,255,0.35)!important;-webkit-text-fill-color:rgba(240,244,255,0.35);
              margin-top:1px;">Health Assistant</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Stats grid ────────────────────────────────────────────────────
        stat_items = [
            ("💬","Chats",    stats['sessions'], "#00d4ff"),
            ("💊","Meds",     stats['meds'],     "#00e5a0"),
            ("📊","Vitals",   stats['vitals'],   "#a78bfa"),
            ("⚠️","Allergies",stats['allergies'],"#ffb347"),
        ]
        st.markdown('<div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;padding:10px 12px;">', unsafe_allow_html=True)
        for icon, lbl, val, color in stat_items:
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);
              border-radius:10px;padding:8px 10px;border-top:2px solid {color}30;">
              <div style="font-size:9px;color:rgba(240,244,255,0.35)!important;text-transform:uppercase;letter-spacing:.4px;">{icon} {lbl}</div>
              <div style="font-size:17px;font-weight:700;color:white!important;margin-top:2px;">{val}</div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # ── Upcoming appointment ───────────────────────────────────────────
        if appt:
            doc  = appt.get("doctor_name","") or "Doctor"
            time = appt.get("appt_time","")   or ""
            spec = appt.get("specialty","")   or ""
            st.markdown(f"""
            <div style="margin:0 12px 8px;
              background:linear-gradient(90deg,rgba(0,212,255,0.08),rgba(0,229,160,0.05));
              border:1px solid rgba(0,212,255,0.18);border-radius:11px;padding:10px 13px;">
              <div style="font-size:9px;color:rgba(0,212,255,0.6)!important;text-transform:uppercase;letter-spacing:1px;margin-bottom:3px;">📅 Next Appointment</div>
              <div style="font-size:12.5px;font-weight:700;color:#00d4ff!important;">{appt['appt_date']}{"  "+time if time else ""}</div>
              <div style="font-size:11px;color:rgba(240,244,255,0.4)!important;margin-top:1px;">{doc}{" · "+spec if spec else ""}</div>
            </div>""", unsafe_allow_html=True)

        # ── Navigation groups ──────────────────────────────────────────────
        for group_label, items in NAV_GROUPS:
            st.markdown(f'<span style="font-size:9px;letter-spacing:1.8px;text-transform:uppercase;color:rgba(240,244,255,0.25)!important;padding:12px 18px 4px;display:block;">{group_label}</span>', unsafe_allow_html=True)
            for page_key, icon, label, color in items:
                is_active = page == page_key
                css_cls = "nav-active" if is_active else ""
                st.markdown(f'<div class="{css_cls}">', unsafe_allow_html=True)
                if st.button(f"{icon}  {label}", key=f"nav_{page_key}", use_container_width=True):
                    st.session_state.page = page_key; st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)

        # ── Emergency ─────────────────────────────────────────────────────
        st.markdown('<hr style="border:none;border-top:1px solid rgba(255,255,255,0.06);margin:8px 14px;">', unsafe_allow_html=True)
        st.markdown('<span style="font-size:9px;letter-spacing:1.8px;text-transform:uppercase;color:rgba(240,244,255,0.25)!important;padding:8px 18px 4px;display:block;">EMERGENCY</span>', unsafe_allow_html=True)
        st.markdown('<div class="btn-emergency">', unsafe_allow_html=True)
        if st.button("🚨  Emergency Guide", use_container_width=True, key="nav_emergency"):
            st.session_state.page = "chat"; st.session_state.quick_prompt = EMERGENCY_PROMPT; st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

        # ── User card ─────────────────────────────────────────────────────
        st.markdown('<hr style="border:none;border-top:1px solid rgba(255,255,255,0.06);margin:8px 14px;">', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="margin:2px 12px 8px;background:rgba(255,255,255,0.03);
          border:1px solid rgba(255,255,255,0.07);border-radius:12px;
          padding:10px 13px;display:flex;align-items:center;gap:10px;">
          <div style="width:36px;height:36px;border-radius:50%;flex-shrink:0;
            background:linear-gradient(135deg,#00d4ff,#a78bfa);
            display:flex;align-items:center;justify-content:center;
            font-size:14px;font-weight:700;color:white!important;
            box-shadow:0 0 14px rgba(0,212,255,0.3);">{initial}</div>
          <div style="flex:1;min-width:0;">
            <div style="font-size:13px;font-weight:600;color:rgba(240,244,255,0.9)!important;
              white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{name}</div>
            <div style="font-size:10.5px;color:rgba(240,244,255,0.35)!important;margin-top:1px;">@{username}</div>
          </div>
        </div>""", unsafe_allow_html=True)

        pc, lc = st.columns(2)
        with pc:
            if st.button("👤 Profile", key="sb_profile", use_container_width=True):
                st.session_state.page = "profile"; st.rerun()
        with lc:
            st.markdown('<div class="btn-logout">', unsafe_allow_html=True)
            if st.button("🚪 Sign Out", key="btn_logout", use_container_width=True):
                for k in ["logged_in","user_id","username","full_name","page","quick_prompt","messages","session_id"]:
                    st.session_state[k] = False if k=="logged_in" else None
                st.session_state.messages=[]; st.session_state.page="chat"; st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        # ── Footer ────────────────────────────────────────────────────────
        st.markdown("""
        <div style="margin:8px 0 0;padding:4px 16px 18px;">
          <span style="display:inline-flex;align-items:center;gap:5px;
            background:rgba(0,212,255,0.08);border:1px solid rgba(0,212,255,0.16);
            border-radius:20px;padding:3px 10px;font-size:10px;color:#00d4ff!important;">
            ⚡ Groq · Llama 3.3 70B
          </span>
          <div style="font-size:10px;color:rgba(240,244,255,0.18)!important;line-height:1.7;margin-top:8px;">
            ⚕️ Health info only — not medical advice.<br>
            Emergencies: call 911 / 112 immediately.
          </div>
        </div>""", unsafe_allow_html=True)
