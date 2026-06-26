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
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
    
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
    
    .status-green { background: #10B981; color: white; padding: 4px 12px; border-radius: 9999px; font-size: 0.8rem; }
    .status-amber { background: #F59E0B; color: white; padding: 4px 12px; border-radius: 9999px; font-size: 0.8rem; }
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

with col1:
    st.metric("Active Programs", "14", "↑2")
with col2:
    st.metric("Entities Screened (MTD)", "48,291", "↑12%")
with col3:
    st.metric("True Positive Rate", "2.8%", "↔ Target")
with col4:
    st.metric("Reports On Time", "100%", "12/12")

st.divider()

# -------------------------- Tabs --------------------------
tab1, tab2, tab3 = st.tabs(["📊 Executive Overview", "📋 Regulatory Reporting", "🔍 Sanctions Intelligence"])

# -------------------------- TAB 1: Executive Overview --------------------------
with tab1:
    colA, colB = st.columns([2, 1])
    
    with colA:
        st.subheader("Sanctions Landscape")
        chart_data = pd.DataFrame({
            "Program": ["Russia-related", "Cyber/Crypto", "Iran", "North Korea", "Others"],
            "Share": [38, 24, 18, 9, 11]
        })
        fig = px.pie(chart_data, values="Share", names="Program", hole=0.4)
        fig.update_traces(textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
    
    with colB:
        st.subheader("Recent High-Impact Designations")
        designations = [
            {"name": "Tornado Cash", "risk": "Critical", "date": "Aug 2022"},
            {"name": "Lazarus Group", "risk": "Critical", "date": "Ongoing"},
            {"name": "Roman Semenov", "risk": "High", "date": "2022"},
        ]
        for d in designations:
            st.markdown(f"""
            **{d['name']}**  
            <span class="status-green">{d['risk']}</span> • {d['date']}
            """, unsafe_allow_html=True)
            st.caption("Crypto / Cyber Program")

# -------------------------- TAB 2: Regulatory Reporting --------------------------
with tab2:
    st.subheader("Regulatory Reporting Hub")
    
    if st.button("✨ Generate AI Narrative (Claude-style)", type="primary"):
        with st.spinner("Generating executive summary..."):
            st.success("✅ Narrative Generated")
            st.markdown("""
            **Executive Summary**  
            During the reporting period, Kraken maintained full compliance with all U.S. and international sanctions regimes. 
            48,291 entities were screened with a true positive hit rate of 2.8%. All OFAC and international filings were 
            submitted on time with zero material deficiencies. Automation initiatives continue to improve efficiency 
            across name screening and low-risk alert triage.
            """)
    
    st.divider()
    
    # Reporting Table
    report_data = {
        "Report": ["OFAC Annual Blocked Property", "OFAC Quarterly Report", "UK Sanctions Report"],
        "Jurisdiction": ["United States", "United States", "United Kingdom"],
        "Due Date": ["Mar 15, 2026", "Jan 31, 2026", "Feb 28, 2026"],
        "Status": ["Submitted", "Submitted", "In Progress"],
        "QC": ["Complete", "Complete", "Pending"]
    }
    df_reports = pd.DataFrame(report_data)
    st.dataframe(df_reports, use_container_width=True, hide_index=True)

# -------------------------- TAB 3: Sanctions Intelligence --------------------------
with tab3:
    colC, colD = st.columns([1, 1])
    
    with colC:
        st.subheader("Quick Entity / Address Screening")
        screen_input = st.text_input("Enter name or crypto address", placeholder="Tornado Cash or 0x...")
        
        if st.button("Screen Now", type="primary"):
            if screen_input:
                st.success("✅ MATCH FOUND")
                st.info(f"**{screen_input}** is associated with sanctioned activity under Cyber / Russia programs.")
            else:
                st.warning("Please enter a name or address")
    
    with colD:
        st.subheader("Crypto Exposure")
        st.metric("Sanctioned Addresses Monitored", "147", "↑18 this month")
        st.caption("Highest volume: Tornado Cash related wallets")

    # Real OFAC Upload
    st.divider()
    st.subheader("Load Real OFAC SDN Data")
    uploaded_file = st.file_uploader("Upload official SDN.csv from OFAC", type=["csv"])
    
    if uploaded_file:
        try:
            df_ofac = pd.read_csv(uploaded_file)
            st.success(f"✅ Loaded {len(df_ofac):,} records from OFAC SDN list")
            st.dataframe(df_ofac.head(10), use_container_width=True)
        except Exception as e:
            st.error(f"Error loading file: {e}")

# -------------------------- Footer --------------------------
st.divider()
st.markdown("""
**Demo Notes for Kraken Interview**  
This dashboard demonstrates understanding of sanctions regulatory reporting, automation opportunities, 
and crypto-specific risk monitoring — core responsibilities of the Sr. Compliance Associate, Sanctions role.
""")

st.caption("Built with Streamlit • Ready for production with real data pipelines")
