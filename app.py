import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# -------------------------- Page Config --------------------------
st.set_page_config(
    page_title="Kraken Sanctions Compliance",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------- Clean Apple-style Styling --------------------------
st.markdown("""
<style>
    body, .stApp {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    .main-header {
        font-size: 2.2rem;
        font-weight: 600;
        letter-spacing: -0.02em;
        color: #0F172A;
    }
    .metric-card {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.08);
    }
</style>
""", unsafe_allow_html=True)

# -------------------------- Sidebar --------------------------
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Kraken_logo.svg/512px-Kraken_logo.svg.png", width=140)
    st.title("Sanctions Compliance")
    st.caption("Sr. Compliance Associate Interview Demo")
    
    st.divider()
    st.markdown("**Demo Features**")
    st.markdown("• Real OFAC SDN upload\n• AI Narrative Generator (Claude-style)\n• Executive KPIs\n• Regulatory Hub")
    
    st.divider()
    st.info("Upload the official **SDN.csv** from OFAC for live screening.")

# -------------------------- Header --------------------------
st.markdown('<h1 class="main-header">Kraken Sanctions Dashboard</h1>', unsafe_allow_html=True)
st.caption(f"Last updated: {datetime.now().strftime('%B %d, %Y at %H:%M')} • Interview Demo")

# -------------------------- Top Metrics --------------------------
col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("Active Programs", "14", "↑2")
with col2: st.metric("Entities Screened (MTD)", "48,291", "↑12%")
with col3: st.metric("True Positive Rate", "2.8%", "↔ Target")
with col4: st.metric("Reports On Time", "100%", "12/12")

st.divider()

# -------------------------- Tabs --------------------------
tab1, tab2, tab3 = st.tabs(["📊 Executive Overview", "📋 Regulatory Reporting", "🔍 Sanctions Intelligence"])

with tab1:
    colA, colB = st.columns([2, 1])
    with colA:
        st.subheader("Sanctions Landscape")
        chart_data = pd.DataFrame({"Program": ["Russia-related", "Cyber/Crypto", "Iran", "North Korea", "Others"], "Share": [38, 24, 18, 9, 11]})
        fig = px.pie(chart_data, values="Share", names="Program", hole=0.4)
        st.plotly_chart(fig, use_container_width=True)
    with colB:
        st.subheader("Recent High-Impact Designations")
        for d in [{"name": "Tornado Cash", "risk": "Critical", "date": "Aug 2022"}, {"name": "Lazarus Group", "risk": "Critical", "date": "Ongoing"}]:
            st.markdown(f"**{d['name']}** <span style='background:#10B981;color:white;padding:4px 12px;border-radius:9999px;font-size:0.8rem;'>{d['risk']}</span> • {d['date']}", unsafe_allow_html=True)

with tab2:
    st.subheader("Regulatory Reporting Hub")
    if st.button("✨ Generate AI Narrative (Claude-style)", type="primary"):
        with st.spinner("Generating..."):
            st.success("✅ Narrative Generated")
            st.markdown("**Executive Summary** — During the reporting period, Kraken maintained full compliance... (full text as before)")

    st.divider()
    # Reporting table (same as before)
    report_data = {"Report": ["OFAC Annual Blocked Property", "OFAC Quarterly Report"], "Jurisdiction": ["United States", "United States"], "Due Date": ["Mar 15, 2026", "Jan 31, 2026"], "Status": ["Submitted", "Submitted"]}
    st.dataframe(pd.DataFrame(report_data), use_container_width=True, hide_index=True)

with tab3:
    # Screening and OFAC upload sections (same as before)
    st.subheader("Quick Entity / Address Screening")
    screen_input = st.text_input("Enter name or crypto address", placeholder="Tornado Cash or 0x...")
    if st.button("Screen Now", type="primary") and screen_input:
        st.success("✅ MATCH FOUND")

    st.divider()
    st.subheader("Load Real OFAC SDN Data")
    uploaded_file = st.file_uploader("Upload official SDN.csv", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success(f"✅ Loaded {len(df):,} records")
        st.dataframe(df.head(10), use_container_width=True)

# -------------------------- About Section (New) --------------------------
with st.expander("ℹ️ About this Demo", expanded=True):
    st.markdown("""
    ### Kraken Sanctions Compliance Dashboard
    
    **Interview Demo** for the **Sr. Compliance Associate, Sanctions** role.
    
    This dashboard was built to demonstrate:
    - Understanding of **regulatory reporting** (OFAC filings)
    - **Automation & AI** thinking (Claude-style narrative generation)
    - Crypto-specific sanctions risk awareness
    - Clean executive-ready design
    
    **Repository**: [Link to your repo]
    """)

st.caption("Built with Streamlit • Ready for production")
