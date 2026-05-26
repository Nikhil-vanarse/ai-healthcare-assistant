"""MediAI — main entry point"""
import streamlit as st

st.set_page_config(
    page_title="MediAI - AI Healthcare Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

from database.db import init_db
init_db()

from components.sidebar    import render_sidebar
from components.styles     import inject_styles
from pages.auth            import render_auth
from pages.chat            import render_chat
from pages.symptom_checker import render_symptom_checker
from pages.vitals          import render_vitals
from pages.drug_info       import render_drug_info
from pages.wellness        import render_wellness
from pages.profile         import render_profile
from pages.history         import render_history

def _init_session():
    for k,v in {"logged_in":False,"user_id":None,"username":None,"full_name":None,
                "page":"chat","quick_prompt":None,"messages":[],"session_id":None}.items():
        if k not in st.session_state:
            st.session_state[k] = v

def main():
    inject_styles()
    _init_session()

    if not st.session_state.logged_in:
        st.markdown("<style>[data-testid='stSidebar']{display:none!important;}</style>", unsafe_allow_html=True)
        render_auth()
        return

    render_sidebar()
    routes = {
        "chat":render_chat,"symptom_checker":render_symptom_checker,
        "vitals":render_vitals,"drug_info":render_drug_info,
        "wellness":render_wellness,"profile":render_profile,"history":render_history,
    }
    routes.get(st.session_state.page, render_chat)()

if __name__ == "__main__":
    main()
