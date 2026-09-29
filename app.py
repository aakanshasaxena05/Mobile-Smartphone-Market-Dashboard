import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Mobile & Smartphone Market Dashboard",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- DATA ----------------
india = pd.DataFrame({
    "Brand": ["vivo","Samsung","OPPO","Xiaomi","Apple","Others"],
    "Shipments_M": [6.3,5.9,4.6,4.5,3.5,9.1],
    "Share_%": [18,17,14,13,10,28]
})

global_df = pd.DataFrame({
    "Brand": ["Samsung","Apple","Xiaomi","OPPO","vivo","Others"],
    "Shipments_M": [62.7,55.7,31.2,28.9,21.2,76.6],
    "Share_%": [22.7,20.2,11.3,10.5,7.7,27.7],
    "YoY_%": [8.1,14.9,-26.4,-17.1,-19.6,-13.1]
})

india_q = pd.DataFrame({
    "Quarter": ["Q1 2025","Q2 2025","Q3 2025","Q4 2025","Q1 2026","Q2 2026"],
    "vivo": [20,21,21,21,20,18],
    "Samsung": [16,16,16,16,16,17],
    "OPPO": [15,14,14,13,15,14],
    "Xiaomi": [12,13,13,12,12,13],
    "Apple": [9,10,9,10,9,10],
})

# ---------------- STYLE ----------------
st.markdown("""
<style>
.main {background:#f5f7fb;}
.block-container {padding-top:1.2rem; padding-bottom:2rem;}
.hero {
    background: linear-gradient(135deg,#12233f 0%,#254f78 60%,#4e89b8 100%);
    padding:28px 32px; border-radius:20px; color:white; margin-bottom:20px;
}
.hero h1 {font-size:38px; margin:0; font-weight:800;}
.hero p {font-size:16px; margin:8px 0 0; opacity:.88;}
.kpi {
    background:white; padding:20px; border-radius:16px;
    border:1px solid #e5e9f0; box-shadow:0 4px 16px rgba(30,50,80,.06);
}
.kpi-title {font-size:13px;color:#667085;font-weight:700;text-transform:uppercase;}
.kpi-value {font-size:29px;font-weight:800;color:#16233a;margin-top:4px;}
.kpi-sub {font-size:12px;color:#667085;margin-top:4px;}
.section {font-size:22px;font-weight:800;color:#16233a;margin:18px 0 10px;}
.source {font-size:11px;color:#667085;}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
<h1>📱 Mobile & Smartphone Market Dashboard</h1>
<p>Current market snapshot • Q2 2026 • India + Global • Shipment-based analysis</p>
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("Dashboard Controls")
region = st.sidebar.selectbox("Market", ["India", "Global"])
show_table = st.sidebar.checkbox("Show detailed data", True)

if region == "India":
    df = india.copy()
    total = 33.9
    yoy = -13
    leader = "vivo"
    leader_share = 18
else:
    df = global_df.copy()
    total = 276.3
    yoy = -7.4
    leader = "Samsung"
    leader_share = 22.7

# ---------------- KPI CARDS ----------------
c1,c2,c3,c4 = st.columns(4)

def kpi(col, title, value, sub):
    col.markdown(f"""
    <div class="kpi">
      <div class="kpi-title">{title}</div>
      <div class="kpi-value">{value}</div>
      <div class="kpi-sub">{sub}</div>
    </div>
    """, unsafe_allow_html=True)

kpi(c1, "Total Q2 2026 Shipments", f"{total:.1f}M", f"YoY change: {yoy}%")
kpi(c2, "Market Leader", leader, f"{leader_share}% shipment share")
kpi(c3, "Top-2 Combined Share",
    f"{df.iloc[:2]['Share_%'].sum():.1f}%",
    f"{df.iloc[0]['Brand']} + {df.iloc[1]['Brand']}")
if region == "Global":
    fastest = global_df.loc[global_df["YoY_%"].idxmax()]
    kpi(c4, "Highest YoY Growth", fastest["Brand"], f"+{fastest['YoY_%']:.1f}%")
else:
    kpi(c4, "Top-5 Share", f"{india.iloc[:5]['Share_%'].sum():.0f}%", "Q2 2026")

# ---------------- CHARTS ----------------
st.markdown('<div class="section">Market Overview</div>', unsafe_allow_html=True)
left,right = st.columns([1.35,1])

with left:
    if region == "Global":
        fig = px.bar(
            global_df.sort_values("Share_%", ascending=True),
            x="Share_%", y="Brand", orientation="h",
            text="Share_%",
            title="Global Smartphone Shipment Share — Q2 2026",
            labels={"Share_%":"Market Share (%)","Brand":""}
        )
        fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
    else:
        fig = px.bar(
            india.sort_values("Share_%", ascending=True),
            x="Share_%", y="Brand", orientation="h",
            text="Share_%",
            title="India Smartphone Shipment Share — Q2 2026",
            labels={"Share_%":"Market Share (%)","Brand":""}
        )
        fig.update_traces(texttemplate="%{text:.0f}%", textposition="outside")
    fig.update_layout(height=420, margin=dict(l=10,r=20,t=55,b=20),
                      plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig, use_container_width=True)

with right:
    fig2 = px.pie(
        df, names="Brand", values="Shipments_M",
        hole=.55, title=f"{region} Shipment Mix — Q2 2026"
    )
    fig2.update_layout(height=420, margin=dict(l=10,r=10,t=55,b=10))
    st.plotly_chart(fig2, use_container_width=True)

# ---------------- TREND + YOY ----------------
st.markdown('<div class="section">Trend & Vendor Performance</div>', unsafe_allow_html=True)
a,b = st.columns([1.35,1])

with a:
    long_q = india_q.melt(id_vars="Quarter", var_name="Brand", value_name="Share")
    fig3 = px.line(long_q, x="Quarter", y="Share", color="Brand", markers=True,
                   title="India Vendor Share Trend",
                   labels={"Share":"Shipment Share (%)","Quarter":""})
    fig3.update_layout(height=390, plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig3, use_container_width=True)

with b:
    if region == "Global":
        yoy_df = global_df.sort_values("YoY_%")
        fig4 = px.bar(yoy_df, x="YoY_%", y="Brand", orientation="h",
                      text="YoY_%",
                      title="Global Vendor YoY Shipment Change",
                      labels={"YoY_%":"YoY Change (%)","Brand":""})
        fig4.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
    else:
        # Use the latest Omdia shipment counts as the main comparison
        fig4 = px.bar(india.sort_values("Shipments_M"),
                      x="Shipments_M", y="Brand", orientation="h",
                      text="Shipments_M",
                      title="India Vendor Shipments — Q2 2026",
                      labels={"Shipments_M":"Shipments (M)","Brand":""})
        fig4.update_traces(texttemplate="%{text:.1f}M", textposition="outside")
    fig4.update_layout(height=390, plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig4, use_container_width=True)

# ---------------- INSIGHTS ----------------
st.markdown('<div class="section">Key Market Insights</div>', unsafe_allow_html=True)
i1,i2,i3 = st.columns(3)
with i1:
    st.info("🇮🇳 **India:** Omdia reported 33.9M smartphone shipments in Q2 2026, down 13% YoY.")
with i2:
    st.info("🌍 **Global:** IDC's final Q2 2026 figure was 276.3M units, down 7.4% YoY.")
with i3:
    st.info("💾 **Market pressure:** IDC and Omdia both identify rising memory/component costs as a major pressure on prices and demand.")

# ---------------- TABLE ----------------
if show_table:
    st.markdown('<div class="section">Detailed Vendor Data</div>', unsafe_allow_html=True)
    if region == "Global":
        display = global_df.copy()
        display["Shipments_M"] = display["Shipments_M"].map(lambda x:f"{x:.1f}")
        display["Share_%"] = display["Share_%"].map(lambda x:f"{x:.1f}%")
        display["YoY_%"] = display["YoY_%"].map(lambda x:f"{x:+.1f}%")
    else:
        display = india.copy()
        display["Shipments_M"] = display["Shipments_M"].map(lambda x:f"{x:.1f}")
        display["Share_%"] = display["Share_%"].map(lambda x:f"{x:.0f}%")
    st.dataframe(display, use_container_width=True, hide_index=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    '<div class="source">Sources: Omdia India Smartphone Shipments, 21 Jul 2026; '
    'IDC Worldwide Quarterly Mobile Phone Tracker, final Q2 2026, 28 Aug 2026. '
    'Figures are shipment estimates and should not be interpreted as installed-base usage share.</div>',
    unsafe_allow_html=True
)
